#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""词库渲染器 —— 唯一真源 `lexicon/*.md` → 两份产物。

    lexicon/*.md  ──render──▶  assets/terms.json             （供 lookup.py 检索）
                                references/07-term-library.md （人读的中英对照表）

只转换与检查词库格式；改词请编辑 lexicon 源文件。

用法：
    python scripts/render_lexicon.py              # 渲染两份产物
    python scripts/render_lexicon.py --check      # 只体检源，不写盘
    python scripts/render_lexicon.py --quiet      # 少说话

退出码：0 = 成功；1 = 源有问题（重复词 / 字段数不对 / 状态非法 …）。
"""
from __future__ import annotations

import argparse
import collections
import json
import re
import sys
from pathlib import Path

# ⛔ 中文 Windows 的控制台默认编码是 GBK：本脚本与 check_terms.py 都会打印 ✅ / ❌，
#    在 GBK 控制台下会抛 UnicodeEncodeError 并 exit 1（与"源有问题"的退出码撞车）。
#    这里把输出强制成 UTF-8（Python 3.7+）。
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent.parent
LEX_DIR = ROOT / "lexicon"
OUT_JSON = ROOT / "assets" / "terms.json"
OUT_MD = ROOT / "references" / "07-term-library.md"
README = "README.md"

# ⭐ 域的固定顺序 —— 先通用层（跨题材），后题材层。
#    这个顺序决定 07 对照表的章节次序，也决定 lookup.py --list 的输出次序。
DOMAIN_ORDER = [
    # 通用层
    "通用-风格", "通用-光线", "通用-色彩材质", "通用-镜头构图", "通用-背景收尾",
    # 题材层
    "人像", "风景自然", "建筑空间", "产品静物", "食物饮品", "抽象概念", "文字平面",
]
GENERIC_LAYER = {"通用-风格", "通用-光线", "通用-色彩材质", "通用-镜头构图", "通用-背景收尾"}

# 状态四档 —— 与 lexicon/README.md 一致。⛔ 没有「过时」（已废除）。
VALID_STATUS = ("常用", "可用", "少见", "慎用")
STATUS_ORDER = {s: i for i, s in enumerate(VALID_STATUS)}

BAD_CHARS = re.compile(r"[■□�\t]")
# 英文列里不该有的东西：韩文/日文假名（历史事故：跑跑姜饼人｜cookierun kingdom and 韩文残留）
FOREIGN_SCRIPT = re.compile(r"[\uac00-\ud7af\u3040-\u30ff]")

# 中文列允许「没有汉字」的例外 —— 规格/型号（含数字或斜杠）与官方无中文名的品牌。
# ⛔ 只加**确实没有中文名**的；凡是能写中文的一律写中文（`choker｜choker` 就是反例）。
SPEC_LIKE = re.compile(r"^[A-Za-z0-9/.\-+ ]+$")
LATIN_ZH_OK = {"MiSans", "ARRI", "IMAX"}


class Problem(Exception):
    pass


# ══════════════════════════════════════════════
# 解析 lexicon/*.md
# ══════════════════════════════════════════════
def parse_files():
    """返回 (domains, problems)。

    domains = [ {name, file, dims:[{name, groups:[{name, terms:[{zh,en,st,note}]}]}]} ]
    """
    files = sorted(p for p in LEX_DIR.glob("*.md") if p.name != README)
    if not files:
        raise Problem(f"lexicon/ 下没有 .md 源文件（{LEX_DIR}）")

    # 按 DOMAIN_ORDER 排序；不在表里的排到最后并按名字排（提醒补进 DOMAIN_ORDER）
    def sort_key(p):
        stem = p.stem
        return (DOMAIN_ORDER.index(stem) if stem in DOMAIN_ORDER else len(DOMAIN_ORDER), stem)

    files.sort(key=sort_key)

    domains, problems = [], []
    for path in files:
        dom = {"name": path.stem, "file": path.name, "dims": []}
        dim = None
        grp = None
        n = 0

        for ln, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            line = raw.strip()
            if not line:
                continue
            if line.startswith("## "):
                dim = {"name": line[3:].strip(), "groups": []}
                dom["dims"].append(dim)
                grp = None
                continue
            if line.startswith("### "):
                if dim is None:
                    # 域内要素 ≤ 8 个时可省维度层 → 造一个无名维度
                    dim = {"name": "", "groups": []}
                    dom["dims"].append(dim)
                grp = {"name": line[4:].strip(), "terms": []}
                # 同名要素在同一域里出现两次 → 合并（不新建）
                same = next((g for g in dim["groups"] if g["name"] == grp["name"]), None)
                if same is not None:
                    grp = same
                    problems.append(f"{path.name}:{ln} 要素「{grp['name']}」重复声明，已合并")
                else:
                    dim["groups"].append(grp)
                continue
            if line.startswith("# ") or line.startswith("> ") or line.startswith("|"):
                continue
            if line.startswith("<!--"):
                continue
            if "|" not in line:
                problems.append(f"{path.name}:{ln} 不是词条也不是标题，已跳过 :: {line[:60]}")
                continue

            parts = [p.strip() for p in line.split("|")]
            if len(parts) != 4:
                problems.append(
                    f"{path.name}:{ln} 字段数={len(parts)}（应为 4：中文|英文|状态|备注）:: {line[:60]}")
                continue
            zh, en, st, note = parts

            if not zh:
                problems.append(f"{path.name}:{ln} 中文为空")
                continue
            if not en:
                problems.append(f"{path.name}:{ln} 英文为空 :: {zh}")
                continue
            if st not in VALID_STATUS:
                problems.append(
                    f"{path.name}:{ln} 非法状态 {st!r}（应为 {'/'.join(VALID_STATUS)}）:: {zh}")
                continue
            for label, val in (("中文", zh), ("英文", en), ("备注", note)):
                if BAD_CHARS.search(val):
                    problems.append(f"{path.name}:{ln} {label}列含坏字符 :: {val[:40]}")
            if FOREIGN_SCRIPT.search(en):
                problems.append(f"{path.name}:{ln} 英文列含韩/日文字符 :: {zh} → {en}")

            if grp is None:
                problems.append(f"{path.name}:{ln} 词条出现在任何 ### 之前 :: {zh}")
                continue

            grp["terms"].append({"zh": zh, "en": en, "st": st, "note": note})
            n += 1

        dom["count"] = n
        # 丢掉空维度 / 空要素
        for d in dom["dims"]:
            d["groups"] = [g for g in d["groups"] if g["terms"]]
        dom["dims"] = [d for d in dom["dims"] if d["groups"]]
        if n == 0:
            problems.append(f"{path.name} 一条词都没有")
        domains.append(dom)

    return domains, problems


# ══════════════════════════════════════════════
# 体检
# ══════════════════════════════════════════════
def lint(domains):
    """返回 (fails, warns, stats)。"""
    fails, warns = [], []

    # ① 跨域 / 跨格重复
    seen = collections.defaultdict(list)
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                for t in g["terms"]:
                    seen[t["zh"]].append((d["name"], g["name"]))
    dups = {k: v for k, v in seen.items() if len(v) > 1}
    if dups:
        fails.append("重复词 %d 个：\n%s" % (
            len(dups),
            "\n".join("    %-14s %s" % (k, " / ".join("%s@%s" % (a, b) for a, b in v))
                      for k, v in list(dups.items())[:20])))

    # ② 英文同形但中文不同（--kw 检索会串味）
    byen = collections.defaultdict(set)
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                for t in g["terms"]:
                    k = re.sub(r"[\s\-_’'·]", "", t["en"].lower())
                    if k:
                        byen[k].add(t["zh"])
    endup = {k: v for k, v in byen.items() if len(v) > 1}
    if endup:
        warns.append("英文同形但中文不同 %d 组：\n%s" % (
            len(endup),
            "\n".join("    %-28s → %s" % (k[:28], " | ".join(sorted(v)))
                      for k, v in list(endup.items())[:12])))

    # ③ 慎用必须有备注
    no_note = []
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                for t in g["terms"]:
                    if t["st"] == "慎用" and not t["note"]:
                        no_note.append(f"{t['zh']}@{d['name']}/{g['name']}")
    if no_note:
        fails.append("「慎用」缺备注（必须写清原因）%d 条：%s" % (len(no_note), " · ".join(no_note)))

    # ④ 词名里夹英文（人工源的常见手滑）
    #    ⭐ 只报**一个汉字都没有**的（`choker｜choker` 这种真错），
    #    夹在汉字里的拉丁字母大多是正常写法（T恤 / Q版 / f/1.4 / APS-C / MiSans / S 形构图）。
    mixed = []
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                for t in g["terms"]:
                    zh = t["zh"]
                    if re.search(r"[\u4e00-\u9fff]", zh):
                        continue                      # 有汉字 → 正常
                    if zh in LATIN_ZH_OK:
                        continue                      # 官方无中文名的品牌
                    if SPEC_LIKE.match(zh) and re.search(r"[\d/]", zh):
                        continue                      # 规格/型号：f/1.4 / APS-C / IMAX 15/70
                    mixed.append(f"{zh}@{d['name']}/{g['name']}")
    if mixed:
        warns.append("中文列没有汉字 %d 条（应写成中文）：%s" % (len(mixed), " · ".join(mixed)))

    # ⑤ 偏薄的格（只报 1 条 —— 可能是空壳）
    thin = []
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                if len(g["terms"]) == 1:
                    thin.append(f"{d['name']}/{g['name']}")
    if thin:
        warns.append("只有 1 条的格 %d 个（看一眼是不是空壳）：%s" % (len(thin), " · ".join(thin)))

    stats = summarize(domains)
    return fails, warns, stats


def summarize(domains):
    n_terms = sum(d["count"] for d in domains)
    n_dims = sum(len(d["dims"]) for d in domains)
    n_groups = sum(len(di["groups"]) for d in domains for di in d["dims"])
    st = collections.Counter()
    for d in domains:
        for di in d["dims"]:
            for g in di["groups"]:
                for t in g["terms"]:
                    st[t["st"]] += 1
    return {
        "domains": len(domains),
        "dimensions": n_dims,
        "groups": n_groups,
        "terms": n_terms,
        "status_dist": {k: st[k] for k in VALID_STATUS if st[k]},
    }


# ══════════════════════════════════════════════
# 产物 A：assets/terms.json
# ══════════════════════════════════════════════
def build_json(domains, stats):
    terms = []
    by_domain, by_group, by_dim = {}, {}, {}
    for d in domains:
        by_domain[d["name"]] = d["count"]
        for di in d["dims"]:
            by_dim[f"{d['name']}/{di['name']}"] = sum(len(g["terms"]) for g in di["groups"])
            for g in di["groups"]:
                by_group[f"{d['name']}/{g['name']}"] = len(g["terms"])
                for t in g["terms"]:
                    terms.append({
                        "s": d["name"],      # 域
                        "v": di["name"],     # 维度
                        "g": g["name"],      # 要素
                        "zh": t["zh"],
                        "en": t["en"],
                        "st": t["st"],
                        "note": t["note"],
                    })

    return {
        **json.loads((LEX_DIR / "model-support.json").read_text(encoding="utf-8")),
        "source": "本地人工词库 lexicon/*.md（唯一真源）",
        "stats": {
            "unique": stats["terms"],
            "domains": stats["domains"],
            "dimensions": stats["dimensions"],
            "groups": stats["groups"],
        },
        "status_dist": stats["status_dist"],
        "domains": [
            {"name": d["name"], "file": d["file"], "count": d["count"],
             "dimensions": [{"name": di["name"], "count": sum(len(g["terms"]) for g in di["groups"]),
                             "groups": [{"name": g["name"], "count": len(g["terms"])} for g in di["groups"]]}
                            for di in d["dims"]]}
            for d in domains
        ],
        "by_domain": by_domain,
        "by_dimension": by_dim,
        "by_group": by_group,
        "terms": terms,
    }


# ══════════════════════════════════════════════
# 产物 B：references/07-term-library.md
# ══════════════════════════════════════════════
def build_md(domains, stats):
    L = []
    st = stats["status_dist"]
    L.append("# 07 · 词表（AI 绘画提示词库）")
    L.append("")
    L.append("> 本文件由 `scripts/render_lexicon.py` 从唯一真源 `lexicon/*.md` 自动生成，**不要手改**。")
    L.append("> 改词请改 `lexicon/` 下的源文件，然后重跑 `python scripts/render_lexicon.py`。")
    L.append("")
    L.append("**用法**：用 `scripts/lookup.py` 检索，**不要整份读完** —— 本文件只为检索而生。")
    L.append("")
    L.append(f"共 **{stats['terms']} 条**，{stats['domains']} 域 / {stats['dimensions']} 维度 / {stats['groups']} 要素。")
    L.append("")
    L.append("**状态**：" + " · ".join(f"{k} {st[k]}" for k in VALID_STATUS if st.get(k))
             + "　——「慎用」= 有副作用，备注列写明原因，别当普通词用。")
    L.append("")
    L.append("---")

    layer = None
    for d in domains:
        cur_layer = "通用层" if d["name"] in GENERIC_LAYER else "题材层"
        if cur_layer != layer:
            layer = cur_layer
            L.append("")
            L.append(f"# ==== {layer} ====")
        L.append("")
        L.append(f"## {d['name']}")
        for di in d["dims"]:
            if di["name"]:
                L.append("")
                L.append(f"> {di['name']}")
            for g in di["groups"]:
                L.append("")
                L.append(f"### {g['name']}（{len(g['terms'])}）")
                L.append("")
                for t in sorted(g["terms"], key=lambda x: STATUS_ORDER[x["st"]]):
                    line = f"- {t['zh']} → {t['en']}〔{t['st']}〕"
                    if t["note"]:
                        line += f"　— {t['note']}"
                    L.append(line)
    L.append("")
    return "\n".join(L)


# ══════════════════════════════════════════════
# main
# ══════════════════════════════════════════════
def main():
    ap = argparse.ArgumentParser(description="lexicon/*.md → terms.json + 07-term-library.md")
    ap.add_argument("--check", action="store_true", help="只体检源，不写盘")
    ap.add_argument("--quiet", action="store_true", help="只报结论")
    args = ap.parse_args()

    try:
        domains, problems = parse_files()
    except Problem as e:
        print(f"✘ {e}")
        return 1

    fails, warns, stats = lint(domains)

    print(f"词库渲染　　{stats['domains']} 域 / {stats['dimensions']} 维度 / "
          f"{stats['groups']} 要素 / **{stats['terms']} 条**")
    print("=" * 62)
    for d in domains:
        print(f"  {d['count']:5d}  {d['name']}")
    print("  状态：" + " · ".join(f"{k} {v}" for k, v in stats["status_dist"].items()))

    if problems:
        print(f"\n⚠️  解析告警 {len(problems)} 条")
        for p in problems[:30]:
            print("    " + p)
    if warns:
        print()
        for w in warns:
            print(f"⚠️  {w}")
    if fails:
        print()
        for f in fails:
            print(f"❌ {f}")

    if args.check:
        print("\n（--check：未写盘）")
        return 1 if fails or problems else 0

    if fails or problems:
        print("源有问题，未写入任何产物。")
        return 1

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(
        json.dumps(build_json(domains, stats), ensure_ascii=False, indent=1),
        encoding="utf-8")
    OUT_MD.write_text(build_md(domains, stats), encoding="utf-8")
    print(f"\n已写出: {OUT_JSON.relative_to(ROOT)}")
    print(f"已写出: {OUT_MD.relative_to(ROOT)}")

    if fails or problems:
        print("\n❌ 源有问题（上面已列）—— 修完再交付。")
        return 1
    print("\n✅ 完成，源无问题。")
    return 0


if __name__ == "__main__":
    sys.exit(main())
