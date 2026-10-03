# -*- coding: utf-8 -*-
"""词库检索 —— 在人工词库里按域 / 维度 / 要素 / 关键词查候选词，输出中英对照。

四层结构：域（题材方向）→ 维度（问什么）→ 要素（这一格）→ 词条。

用法：
    python scripts/lookup.py --list
    python scripts/lookup.py --list --domain 人像          # 只看人像域的骨架
    python scripts/lookup.py --domain 通用-镜头构图
    python scripts/lookup.py --group 焦外
    python scripts/lookup.py --dim 参照物
    python scripts/lookup.py --kw 逆光
    python scripts/lookup.py --kw rim --domain 通用-光线
    python scripts/lookup.py --group 发型 --limit 30
    python scripts/lookup.py --group 艺术家 --all           # 连「慎用」也展开
    python scripts/lookup.py --status 常用 --domain 人像

状态四档（每个词条必填）：
    常用  → 大多数场景适用
    可用  → 有效，但有明确适用场景
    少见  → 冷门，只在特定风格下用
    慎用  → **有副作用**，默认折叠；展开时必附原因
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# ⛔ 中文 Windows 的控制台默认编码是 GBK：命中「慎用」条目时输出里的 ⛔ 会抛
#    UnicodeEncodeError，**打到一半就中断** —— 拿到的是被截断的结果，还看不出来。
#    这里把输出强制成 UTF-8（Python 3.7+）。
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8")
    except Exception:
        pass

TERMS = Path(__file__).resolve().parent.parent / "assets" / "terms.json"

STATUS_ORDER = ("常用", "可用", "少见", "慎用")


def load():
    if not TERMS.exists():
        sys.exit(f"找不到词表 {TERMS}，先跑 scripts/render_lexicon.py 生成。")
    return json.loads(TERMS.read_text(encoding="utf-8"))


def fmt(rec):
    tail = f"  — {rec['note']}" if rec.get("note") else ""
    return f"{rec['zh']} → {rec['en']}{tail}"


def show_tree(data, domain=None):
    """打印四层骨架。"""
    print("== 词库骨架 ==")
    for dom in data["domains"]:
        if domain and domain not in dom["name"]:
            continue
        print(f"\n[{dom['name']}] 共 {dom['count']} 条")
        for di in dom["dimensions"]:
            if di["name"]:
                print(f"  ## {di['name']}  ({di['count']})")
            pad = "     " if di["name"] else "  "
            for g in di["groups"]:
                print(f"{pad}- {g['name']}  ({g['count']})")
    st = data["stats"]
    print(f"\n总计 {st['unique']} 条 · {st['domains']} 域 / {st['dimensions']} 维度 / {st['groups']} 要素")
    dist = data.get("status_dist", {})
    print("状态：" + " · ".join(f"{k} {dist[k]}" for k in STATUS_ORDER if dist.get(k))
          + "　（「慎用」默认折叠，用 --all 展开）")
    print("\n查法：--domain <域> / --dim <维度> / --group <要素，可部分匹配> / --kw <关键词>")


def main():
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--list", action="store_true", help="列出四层骨架与词条数")
    ap.add_argument("--domain", "--section", dest="domain",
                    help="按域过滤，如 人像 / 通用-光线")
    ap.add_argument("--dim", "--dimension", dest="dim", help="按维度过滤，如 参照物 / 光学")
    ap.add_argument("--group", help="按要素过滤，支持部分匹配，如 焦外 / 发型")
    ap.add_argument("--kw", help="按中英文关键词模糊查")
    ap.add_argument("--status", help="按状态过滤，逗号分隔，如 常用,可用")
    ap.add_argument("--limit", type=int, default=200, help="最多输出多少条，默认 200")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--all", action="store_true", help="连「慎用」也展开（默认折叠）")
    args = ap.parse_args()

    data = load()
    terms = data["terms"]

    if args.list or not any([args.domain, args.dim, args.group, args.kw, args.status]):
        show_tree(data, args.domain)
        return

    sel, title = terms, []
    for label, val, key in (("域", args.domain, lambda r: r["s"]),
                            ("维度", args.dim, lambda r: r["v"]),
                            ("要素", args.group, lambda r: r["g"])):
        if val:
            sel = [r for r in sel if val in key(r)]
            title.append(f"{label}≈{val}")
    if args.kw:
        k = args.kw.lower()
        sel = [r for r in sel if k in r["zh"].lower() or k in r["en"].lower()
               or k in (r.get("note") or "").lower()]
        title.append(f"关键词={args.kw}")
    if args.status:
        want = {s.strip() for s in args.status.split(",") if s.strip()}
        sel = [r for r in sel if r["st"] in want]
        title.append("状态=" + "/".join(sorted(want)))

    if not sel:
        print("没查到。先用 --list 看看域 / 维度 / 要素的名字。")
        return

    if args.json:
        visible = [r for r in sel if r["st"] != "慎用" or args.all]
        print(json.dumps(visible[: args.limit], ensure_ascii=False, indent=1))
        return

    cautions = [r for r in sel if r["st"] == "慎用" and not args.all]
    kept = [r for r in sel if not (r["st"] == "慎用" and not args.all)]

    print(f"# 命中 {len(sel)} 条　({'，'.join(title)})")
    cur = None
    for r in sorted(kept, key=lambda x: STATUS_ORDER.index(x["st"]))[: args.limit]:
        head = f"[{r['s']}] {r['g']}"
        if head != cur:
            print(f"\n{head}")
            cur = head
        mark = {"常用": "", "可用": "〔可用〕", "少见": "〔少见〕", "慎用": "**【慎用】** "}[r["st"]]
        print("  " + mark + fmt(r))

    shown = len(kept[: args.limit])
    if len(kept) > args.limit:
        print(f"\n…还有 {len(kept) - args.limit} 条，用 --limit 调大")

    if cautions:
        print(f"\n⛔ 另有 {len(cautions)} 条**慎用词已折叠** —— 它们有副作用，别当普通词用：")
        for r in cautions[:10]:
            print(f"   {r['zh']} —— {r.get('note') or '有副作用，使用前先确认适用性'}")
        if len(cautions) > 10:
            print(f"   …其余 {len(cautions) - 10} 条用 --all 展开")
        else:
            print("   要看全部（含备注）加 --all")


if __name__ == "__main__":
    main()
