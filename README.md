# Character Prompt Studio

AI 人物设计与生图提示词助手。把一句灵感或一张参考图，整理成包含外貌、服装、构图、材质与光影的可用提示词。

本仓库发布的 Skill 名称为 **ai-image-prompt**，由 joshesye 基于 [huimengshiyezi/ai-image-prompt](https://github.com/huimengshiyezi/ai-image-prompt) 定制扩展。原作者：**AI绘梦师葉子**。保留原始 MIT 许可证及版权声明。

## 能做什么

- **人物设定**：支持面部特写与正面、侧面、背面全身的角色资产布局。
- **冷酷科幻人物**：提供科幻角色的材质、服装、装置与氛围参考。
- **韩式财阀千金**：包含香槟金丝缎、血红天鹅绒、黑丝绒星链三套完整礼服模板；采用 3D 漫剧写实厚涂，左侧大幅胸像、右侧正面／45°／背面全身。
- **分类词库**：包含 3397 条词条，以及适用说明、检索脚本、词库产物生成与完整性检查。
- **模型适配**：依据 Skill 内的模型说明组织提示词，支持持续调整构图、风格与细节。

默认提供提示词。实际生成图片需要宿主工具具备相应能力；多视角人物一致性仍需结合参考图与生成结果检查。

## 安装到 Codex

下载本仓库 ZIP 并解压，将仓库文件夹改名为 `ai-image-prompt`，放到以下位置：

| 系统 | 安装目录 |
| --- | --- |
| macOS / Linux | `~/.codex/skills/ai-image-prompt/` |
| Windows | `%USERPROFILE%\.codex\skills\ai-image-prompt\` |

确认目录中直接包含 `SKILL.md`，不要多套一层文件夹。若已有同名 Skill，请先备份，再替换。重启 Codex 后，在新对话中调用。

也可以把仓库地址发给 Codex：

> 帮我安装这个 Skill：https://github.com/joshesye/Character-Prompt-Studio

## 使用示例

> 使用 ai-image-prompt，生成三个韩式财阀千金的文生图提示词，分别穿香槟金、血红色和黑色礼服，采用 3D 漫剧写实厚涂风格。

> 设计一名冷酷科幻猎魔人，服装有真实磨损，减少装饰性装置，输出角色设定图提示词。

> 参考这张图，保留五官与发型，只更换礼服。左侧大幅脸部胸像，右侧依次为正面、45°侧面和背面全身。

需求里可以写明 **人物身份、视觉风格、构图、使用模型**。生成后可继续要求“减少配饰”“改成冷调光影”或“保持同一人物，只更换服装”。

## 文件说明

- [`SKILL.md`](SKILL.md)：Skill 入口与工作流程。
- [`references/`](references/)：提示词参考与专题模板。
- [`references/09-korean-heiress-gowns.md`](references/09-korean-heiress-gowns.md)：三套韩式财阀千金礼服模板。
- [`lexicon/`](lexicon/)：分类词库源文件。
- [`assets/`](assets/)：结构化词库产物。
- [`scripts/`](scripts/)：词库检索、生成与检查工具。
- [`docs/original-README.md`](docs/original-README.md)：定制前保留的说明，涉及安装方式时以本页 Codex 安装步骤为准。

## 词库检查

在仓库目录使用 Python 3 执行：

```bash
python3 scripts/check_terms.py
```

## 来源与许可

基于 [AI绘梦师葉子的 ai-image-prompt](https://github.com/huimengshiyezi/ai-image-prompt) 定制，包含科幻人物偏好、分类词库与韩式财阀千金等扩展。采用 [MIT License](LICENSE)，再分发时请保留许可证及版权声明。
