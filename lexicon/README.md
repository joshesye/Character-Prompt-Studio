# 分类词库与适用说明

## 范围与优先级

词库只提供候选词，不覆盖用户偏好、角色身份、参考图模式或模型适配。
冷酷科幻人物继续使用 `references/08-cold-sci-fi-characters.md`；东方人物继续使用已有 eastern-character-mj-seedance 技能。
MJ 的英文输出、SD 的正负向词和自然语言模型格式继续遵循现有规则。

## 源文件

- `*.md`（本文件除外）：域 → 维度 → 要素 → 词条。域用文件名，维度用 `##`，要素用 `###`。
- 每条格式：`中文 | 英文 | 状态 | 适用说明`。不得包含额外的 ASCII 竖线。
- 状态：常用（通常适用）、可用（按场景选择）、少见（特定风格）、慎用（必须说明具体局限）。状态不是禁用规则。
- 备注说明什么时候使用、可能出现什么视觉偏差；不作未经核实的平台或版权判断。
- 中英文均可用于输出，语言由目标模型及用户要求决定。旧译别名保留在备注以便检索。
- `旧库补充-*.md` 保留新分类未覆盖的原词，标记为可用；并不意味着这些词已经逐条重新评定。
- `model-support.json` 保留原有 MJ 参数、SD 词组及绘画分类资料；版本是否适用仍以现有模型适配规则为准。
- 同一中文词只收一次；允许添加自定义域。参数词不要无差别套用到自然语言模型。

## 使用方法

先根据角色或画面任务定位域，再选择需要补充的维度；每个维度只取必要词，避免堆叠相互冲突的风格、材质和光线。
已有角色档案中的身份锚点保持不变。查到的候选词不能自动替换固定脸型、发型、服装与武器。

```bash
python scripts/lookup.py --list
python scripts/lookup.py --domain 人像 --group 发型 --limit 20
python scripts/lookup.py --kw 逆光
python scripts/lookup.py --kw rim --json
python scripts/lookup.py --status 慎用 --all
```

`--section` 仍是 `--domain` 的别名；旧大类已经重组，请用 `--list` 确认新域。慎用词默认折叠，用 `--all` 展开。

## 自动生成与完整性检查

```bash
python scripts/render_lexicon.py --check
python scripts/render_lexicon.py
python scripts/check_terms.py
```

只维护本目录源文件，生成器自动刷新 `assets/terms.json` 和 `references/07-term-library.md`。
源有格式错误、重复词或非法状态时不写产物。检查器比较完整 JSON 和完整 Markdown，包括翻译、状态、备注及模型资料；失败时返回非零退出码。
旧命令 `python scripts/build_terms.py` 转调新生成器；不再接受旧的外部源路径和环境变量。

分类源与检索、渲染工具借鉴 huimengshiyezi/ai-image-prompt，commit aa941ff4a710c1c46921192b086777331bb7f3a8（MIT）；本地保留个性化规则与旧词资料。
