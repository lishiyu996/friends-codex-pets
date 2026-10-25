# 老友记 Codex 桌宠 · Friends Codex Pets

《老友记》六位主角的非官方 Codex 桌宠素材项目。采用 3D 卡通造型、透明背景与朝画面左侧的单动作循环。

**当前版本：六位角色均提供可安装的 Codex 单动作桌宠包，集中在本仓库。** 瑞秋保留朝左待机眨眼，其余五人沿用现有 v3 动作。每个角色均可单独下载安装；本仓库包含素材、打包工具与制作记录，不包含独立桌宠应用或 Codex 客户端。

<table>
<tr><th>瑞秋 · 待机眨眼</th><th>罗斯 · 抱书与伸手</th><th>乔伊 · 吃披萨</th></tr>
<tr>
<td><img src="制作/瑞秋/qa/previews/瑞秋-朝左待机.gif" width="170" alt="瑞秋朝左待机眨眼"></td>
<td><img src="制作/五人单动作预览/罗斯/罗斯-动作预览-v3.gif" width="170" alt="罗斯抱恐龙书与伸手"></td>
<td><img src="制作/五人单动作预览/乔伊/乔伊-动作预览-v3.gif" width="170" alt="乔伊朝左吃披萨"></td>
</tr>
<tr><th>菲比 · 吉他与音符</th><th>莫妮卡 · 叉腰与抱臂</th><th>钱德勒 · 眨眼</th></tr>
<tr>
<td><img src="制作/五人单动作预览/菲比/菲比-动作预览-v3.gif" width="170" alt="菲比抱吉他，音符上升消失"></td>
<td><img src="制作/五人单动作预览/莫妮卡/莫妮卡-动作预览-v3.gif" width="170" alt="莫妮卡持毛巾叉腰与抱臂"></td>
<td><img src="制作/五人单动作预览/钱德勒/钱德勒-动作预览-v3.gif" width="170" alt="西装版钱德勒眨眼"></td>
</tr>
</table>

## 下载与使用

推荐前往 [v0.2.0 六人安装包](https://github.com/lishiyu996/friends-codex-pets/releases/tag/v0.2.0)，下载任意角色的 ZIP。六位角色都在本仓库，也可以分别下载下表中的安装包。

| 角色 | Codex 安装包 | 安装目录名 |
| --- | --- | --- |
| 瑞秋 | [下载 ZIP](制作/瑞秋/final/瑞秋-MVP-安装包.zip) | `friends-rachel-mvp` |
| 罗斯 | [下载 ZIP](制作/五人Codex安装包/friends-ross-mvp.zip) | `friends-ross-mvp` |
| 乔伊 | [下载 ZIP](制作/五人Codex安装包/friends-joey-mvp.zip) | `friends-joey-mvp` |
| 菲比 | [下载 ZIP](制作/五人Codex安装包/friends-phoebe-mvp.zip) | `friends-phoebe-mvp` |
| 莫妮卡 | [下载 ZIP](制作/五人Codex安装包/friends-monica-mvp.zip) | `friends-monica-mvp` |
| 钱德勒 | [下载 ZIP](制作/五人Codex安装包/friends-chandler-mvp.zip) | `friends-chandler-mvp` |

每个 ZIP 都包含一个角色文件夹，内有 `pet.json` 与 `spritesheet.webp`。[五人独立图像与 GIF v3](制作/五人单动作预览/五人独立图像与GIF-v3.zip) 另供查看与制作使用。

### 安装任意角色

需要支持自定义宠物的 Codex 桌面客户端。将角色 ZIP 中的整个角色文件夹解压到 Codex 数据目录的 `pets/` 下，默认数据目录为 `~/.codex`；设置了 `CODEX_HOME` 时使用该目录。以罗斯为例：

```text
~/.codex/pets/friends-ross-mvp/
├── pet.json
└── spritesheet.webp
```

两个文件应直接放在角色目录中。然后在 Codex 宠物列表中选择对应中文名字，瑞秋的显示名为“瑞秋 MVP”。每个角色使用独立目录，可以同时安装六位角色。

### 克隆仓库后安装全部六人

在 macOS / Linux 终端运行：

```sh
git clone https://github.com/lishiyu996/friends-codex-pets.git
cd friends-codex-pets
pets_dir="${CODEX_HOME:-$HOME/.codex}/pets"
mkdir -p "$pets_dir/friends-rachel-mvp"
cp -n "制作/瑞秋/final/pet.json" "制作/瑞秋/final/spritesheet.webp" "$pets_dir/friends-rachel-mvp/"
for character in ross joey phoebe monica chandler; do
  pet_id="friends-$character-mvp"
  mkdir -p "$pets_dir/$pet_id"
  cp -n "制作/五人Codex安装包/$pet_id/pet.json" "制作/五人Codex安装包/$pet_id/spritesheet.webp" "$pets_dir/$pet_id/"
done
```

`cp -n` 不覆盖已有同名文件；升级前请先备份旧目录。

### 动作范围与验证

瑞秋仅有朝左待机眨眼，其他任务和交互状态统一使用待机帧。其余五人使用 v1 动画 WebP 图集，保留 v3 的逐帧停留和眨眼时序，各任务状态共用各自的一条动作循环。六人均不包含完整九动作或目光跟随，后续静态形象候选未替换安装包。

已核对文件结构、透明通道、1536×1872 图集尺寸、五人全部时间帧的 72 格一致性与时间线、ZIP 解压安装结构及安装副本哈希。此前已核对本机客户端加载格式与浏览器同类图集渲染，Codex 应用内选择与实际播放尚未完成实测。[打包检查](制作/五人Codex安装包/打包检查.json) · [安装检查](制作/五人Codex安装包/安装检查.json)。

从已有 GIF 重新打包五人可运行 `python3 制作/五人Codex安装包/打包.py`，依赖 Pillow 与 NumPy。该脚本只打包，不执行安装、不修改 GIF，也不重新生成角色形象。

## 人物与动作

| 人物 | 当前动作 | 独立形象 | 动画 |
| --- | --- | --- | --- |
| 瑞秋 | 朝左待机、眨眼 | [透明 PNG](制作/瑞秋/final/瑞秋-朝左透明基准.png) | [GIF](制作/瑞秋/qa/previews/瑞秋-朝左待机.gif) |
| 罗斯 | 抱恐龙书 ↔ 一手伸展，多个停留姿态眨眼 | [PNG](制作/五人单动作预览/罗斯/罗斯-单独形象.png) | [GIF v3](制作/五人单动作预览/罗斯/罗斯-动作预览-v3.gif) |
| 乔伊 | 持披萨 ↔ 咬一口、咀嚼，停留时眨眼 | [PNG](制作/五人单动作预览/乔伊/乔伊-单独形象.png) | [GIF v3](制作/五人单动作预览/乔伊/乔伊-动作预览-v3.gif) |
| 菲比 | 抱吉他，音符上升消失，独立眨眼 | [PNG](制作/五人单动作预览/菲比/菲比-单独形象.png) | [GIF v3](制作/五人单动作预览/菲比/菲比-动作预览-v3.gif) |
| 莫妮卡 | 叉腰持毛巾 ↔ 抱臂，多个停留姿态眨眼 | [PNG](制作/五人单动作预览/莫妮卡/莫妮卡-单独形象.png) | [GIF v3](制作/五人单动作预览/莫妮卡/莫妮卡-动作预览-v3.gif) |
| 钱德勒 | 西装版，仅眨眼 | [PNG](制作/五人单动作预览/钱德勒/钱德勒-单独形象.png) | [GIF v3](制作/五人单动作预览/钱德勒/钱德勒-动作预览-v3.gif) |

五人预览采用 384×416 画布，基础动作各六帧；v3 在不同停留姿态插入闭眼帧。动作 A→B 的过渡保持原速，通过延长姿态停留减少反复动作的频率。

| 人物 | GIF 循环时长 | 每轮眨眼次数 |
| --- | --- | --- |
| 罗斯 | 6.90 秒 | 3 |
| 乔伊 | 6.24 秒 | 2 |
| 菲比 | 4.56 秒 | 2，音符每 2.28 秒循环 |
| 莫妮卡 | 8.04 秒 | 3 |
| 钱德勒 | 2.56 秒 | 1 |

闭眼修订只作用于眼部区域，保留原姿态的身体、道具与透明轮廓。GIF 使用统一调色板、关闭颜色抖动，并处理透明边缘，减少轮廓闪点。[眨眼节奏检查](制作/五人单动作预览/眨眼节奏总检查-v3.json) · [多姿态眨眼对照](制作/五人单动作预览/多姿态眨眼检查-v3.png)。

## 文件结构

```text
friends-codex-pets/
├── README.md
├── LICENSE                      # 原创文字、配置与提示词的 MIT 许可
├── ASSET_NOTICE.md              # 角色与视觉素材说明
├── AGENTS.md                    # 项目规则唯一真源
├── CLAUDE.md -> AGENTS.md
├── GEMINI.md -> AGENTS.md
├── 设计/                        # 四份原始参考图、形象方案、历史提示词
├── 制作/
│   ├── 瑞秋/
│   │   ├── pet_request.json     # 图集规格与状态映射
│   │   ├── final/               # pet.json、图集、透明基准与安装 ZIP
│   │   └── qa/                  # GIF、透明边缘与结构检查
│   ├── 五人Codex安装包/         # 五个 pet.json、动画图集、ZIP、打包工具与检查
│   └── 五人单动作预览/
│       ├── 参考/                # 各人参考裁图与六帧布局
│       ├── 提示词/
│       ├── 罗斯/                # 其他四人同结构
│       │   ├── 分帧/            # 01.png 至 06.png
│       │   ├── 眨眼/            # 闭眼姿态、眼部掩膜与检查
│       │   ├── 罗斯-单独形象.png
│       │   ├── 罗斯-动作预览-v3.gif
│       │   └── 时间线-v3.json
│       ├── 乔伊/、菲比/、莫妮卡/、钱德勒/
│       ├── render-jobs.json
│       └── 五人独立图像与GIF-v3.zip
└── 调研/                        # 制作技能调研，带核验日期
```

## 制作记录与边界

- [形象设计方案](设计/老友记Codex桌宠-形象设计方案.md)记录角色确认范围。`三人形象修订02` 中仅莫妮卡被采用，图中的旧瑞秋、钱德勒不属于定稿。
- 四份原始参考图原样保留。角色动作使用参考图与内置图像生成服务制作，后续进行分帧、配准、透明边缘处理和 GIF 编码。
- 五人的提示词、原动作条、PNG、闭眼掩膜、时间线和检查记录均公开。早期临时处理脚本没有保留，当前仓库不提供完整的一键重建流水线。
- 六人均采用 1536×1872、8 列 9 行、单格 192×208 的 v1 图集。五人通过动画 WebP 保留自定义停留时长；同一时刻各格子显示相同姿态，客户端切换任务格子时不改变动作。
- 乔伊的披萨咬痕较弱，菲比的音符渐隐过渡较简单；PNG 与 GIF 的透明边缘显示也可能有差异。
- 公开历史从本次整理后的快照开始。检查文件中出现的 `be00d65` 是制作时的本地基线，不是公开仓库中的可用提交；本机缓存和临时文件路径已移除。
- 未采用的网页 Demo、SVG 与否决试稿已清理，不包含在此版本中。

## 许可与来源

本仓库原创文字、JSON 配置、时间线与提示词采用 [MIT License](LICENSE)。角色参考图、生成图像、PNG / GIF / WebP 和安装 ZIP 的范围说明见 [ASSET_NOTICE.md](ASSET_NOTICE.md)。

这是非官方同人项目，与《老友记》及 Codex / OpenAI 的权利人无隶属或认可关系。MIT 许可不授予第三方角色、商标或肖像权利。

制作流程参考 [OpenAI hatch-pet](https://github.com/openai/skills/tree/main/skills/.curated/hatch-pet)；历史技能比较见[调研记录](调研/Codex桌宠Skill筛选.md)。未将上游工具源码复制进本仓库。
