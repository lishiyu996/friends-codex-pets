# Codex 桌宠 Skill 筛选

核验日期：2026-10-25。核验范围为 GitHub 的 SKILL.md、README、目录结构、公开示例及仓库元数据；本轮未安装或运行这些制作流水线。

## 推荐结果

| 项目 | 核验到的能力 | 对本项目的用途 |
| --- | --- | --- |
| [OpenAI 官方 hatch-pet](https://github.com/openai/skills/tree/main/skills/.curated/hatch-pet) | 概念或参考图制作基础角色；逐行动画；透明图集组装、视觉检查和 Codex 安装包。支持非像素风格。 | 首选制作流程。先固定经用户认可的角色形象，再展开动作。 |
| [leduy-it/hatch-pet-plus](https://github.com/leduy-it/hatch-pet-plus) | 基于 hatch-pet 的社区插件；多种材质风格；参考图输入；仓库列有 21 个可安装成品包，以及动画、图集和 QA 示例。 | 更适合查看黏土、手办、毛绒等风格的实际呈现，作为制作方案与成品质量的参考。 |
| [wyddy7/codex-pet-generator](https://github.com/wyddy7/codex-pet-generator) | 固定角色参考、逐行动画审批、小尺寸辨识度检查、手工切帧指引、打包和验证脚本。 | 辅助制定验收顺序，防止形象未认可便推进动画和打包。切帧不是自动化。 |

原文入口：[官方 SKILL.md](https://github.com/openai/skills/blob/main/skills/.curated/hatch-pet/SKILL.md)、[plus SKILL.md](https://github.com/leduy-it/hatch-pet-plus/blob/main/plugins/hatch-pet-plus/skills/hatch-pet/SKILL.md)、[generator SKILL.md](https://github.com/wyddy7/codex-pet-generator/blob/main/SKILL.md)。

## 活跃度与证据

- skills CLI 搜索显示官方 hatch-pet 约 3.3K 安装。[目录页](https://skills.sh/openai/skills/hatch-pet)。
- GitHub API 本轮返回 openai/skills 为 28,289 星；这是整个技能集合的星数，不能视为 hatch-pet 单项评价。
- hatch-pet-plus 和 codex-pet-generator 的仓库均为 15 星，社区使用规模较小。后两项没有核验到独立安装量。
- plus 有公开的[多种角色示例](https://github.com/leduy-it/hatch-pet-plus/blob/main/examples/showcase-mascots.png)、[同一机器人六种材质示例](https://github.com/leduy-it/hatch-pet-plus/blob/main/examples/showcase-robot-styles.png)和[动作预览](https://github.com/leduy-it/hatch-pet-plus/blob/main/examples/showcase-lanes.gif)。这些是作者项目的产出，不是本项目已达到的效果。

## 其他候选的取舍

- [feiyu-xj/codex-pets](https://github.com/feiyu-xj/codex-pets)：针对 Q 版角色、背景清理和图集转换。脚本允许复用邻近姿势补帧，不能据此保证每个动作都充分表现；本轮查到 1 星，作为备选。
- [Craybreeding/hatch-pet](https://github.com/Craybreeding/hatch-pet)：参考照片身份一致性和 QA 流程较详细，但作者公开验证样例是两只猫，不能直接推断其真人角色复刻能力；本轮查到 0 星。
- [Sunwood-ai-labs/hatch-pet-skill](https://github.com/Sunwood-ai-labs/hatch-pet-skill)：基于 hatch-pet 的较早版本，默认偏像素式桌宠，与本项目已认可的手办方向存在差异；本轮查到 0 星。
- [RunComfy codex-pet](https://github.com/runcomfy-com/skills/tree/main/codex-pet)：文档描述为生成一个基础姿势后，以程序微变换组装动作。需要独立服务令牌，不优先用于本项目的角色与动作质量目标。
- [ZenMux 的 zenmux-codex-pets](https://github.com/ZenMux/skills/tree/main/skills/zenmux-codex-pets)：用途是安装仓库自带的桌宠，不能直接当成任意角色的制作技能。

## 制作边界

这三套推荐流程都需要绘制、生成或提供角色图。它们改进参考约束、动作制作、验收和打包，不会自动保证演员肖像辨识度，也不能解除图像服务本身的限制。

官方上游与社区增强版公开的图集版本约定存在差异。真正制作安装包前，应先核对本机 Codex 支持的格式，不能混用双方规范。

当前用户要求的是查找 Skill。本轮暂停修改形象 Demo，没有重新调用生图，也没有改动全局技能目录。

## 建议的下一步顺序

1. 以官方 hatch-pet 为制作入口，参考 plus 的真实成品和材质方案。
2. 保留已被认可的四位角色。
3. 瑞秋和钱德勒各自先做一张标准全身角色图；用户未认可前，不制作动画。
4. 标准形象通过后，使用同一基准图制作动作，逐行验收，再输出 Codex 安装包。

## 官方安装入口

可通过官方安装器获取：

```sh
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo openai/skills \
  --path skills/.curated/hatch-pet \
  --dest ~/.agents/skills
```

上面的目标遵循用户的共享技能真源目录约定。安装后还需接入 Codex 的技能入口；实际安装时先检查同名冲突。该命令本轮没有执行。

社区增强版使用其 README 中的插件安装入口；不要将它与官方同名 hatch-pet 目录直接覆盖。
