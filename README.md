# 超真实生图 / Hyperrealistic Image

> 生成超真实、有生活感的图片。不是"看起来真实"，而是"就是一张普通照片"。
>
> Generate hyperrealistic, everyday-looking photos. Not "looks realistic" — but "is just an ordinary photo."

**适用于任何AI图片生成模型**：豆包、Midjourney、DALL-E、Stable Diffusion、Flux、文心一格等。
**Works with any AI image generation model**: Doubao, Midjourney, DALL-E, Stable Diffusion, Flux, etc.

> ⚠️ **提示 / Note**: 本技能的提示词在豆包上进行了大量实测优化，在豆包上的出图效果可能会更优秀。其他模型同样适用，但可能需要微调部分参数以达到最佳效果。
>
> This skill was extensively tested and optimized on Doubao. Results may be better on Doubao than other models. The methodology is model-agnostic, but some parameters may need fine-tuning for best results on other models.

---

## 核心原理 / Core Principle

**中文**：直接写"真实"、"写实"、"照片级"只会触发一种AI风格。要生成真正有真实感的图片，需要用**具体的、可感知的不完美特征**来引导模型。真实感 = 具体设备 + 拍摄逻辑 + 画质缺陷 + 不完美细节 + 普通人物 + 反AI否定。

**English**: Writing "realistic" or "photo" just triggers an AI style. To generate true photorealism, you need **specific, perceivable imperfections** to guide the model. Realism = Specific Device + Shooting Logic + Quality Flaws + Imperfect Details + Ordinary People + Anti-AI Negation.

**黄金三段式 / Golden Three-Part Structure**:
1. **第一段 / Part 1**（置顶，权重最高）：年代 + 设备 + 拍摄逻辑 + 色彩 + 画质 / Era + Device + Shooting Logic + Color + Quality
2. **第二段 / Part 2**（中间）：主体内容 + 不完美细节 / Subject Content + Imperfect Details
3. **第三段 / Part 3**（结尾）：否定式描述（封印AI感）/ Negation Descriptions (seal the AI feel)

## 支持的风格 / Supported Styles

| 风格 / Style | 核心设备 / Device | 适用场景 / Use Cases |
|------|------|------|
| 📱 手机随手拍 / Phone Snapshot | 智能手机 / Smartphone | 日常记录、生活vlog、校园生活 / Daily life, vlog, campus |
| 🎞️ 胶片感 / Film Feel | 柯达金胶卷 / Kodak Gold | 文艺、复古、氛围感 / Artistic, vintage, mood |
| 📷 纪实街拍 / Documentary Street | 徕卡、理光GR / Leica, Ricoh GR | 街头、人文、故事感 / Street, human interest |
| 🏠 生活记录 / Life Record | 手机室内 / Phone indoor | 居家、日常、温馨感 / Home, daily, cozy |
| 📼 年代旧照片 / Vintage Photo | 胶卷+扫描 / Film + scan | 怀旧、70/90/00年代 / Nostalgia, retro eras |

## 支持的年代分级 / Era Grading

| 年代 / Era | 泛黄 / Yellowing | 褪色 / Fading | 画质 / Quality | 典型设备 / Devices |
|------|------|------|------|------|
| 70年代 / 1970s | 严重 / Severe | 严重 / Severe | 差 / Poor | 海鸥、上海牌 / Seagull, Shanghai |
| 90年代 / 1990s | 中度 / Moderate | 明显 / Noticeable | 一般 / Average | 柯达金、富士 / Kodak Gold, Fuji |
| 00年代 / 2000s | 偏黄灰 / Yellowish-gray | 明显 / Noticeable | 一般 / Average | 山寨手机、卡片机 / Knockoff phones, digicams |
| 10年代 / 2010s | 不黄 / Minimal | 几乎无 / Almost none | 较好 / Good | 早期智能手机 / Early smartphones |

## 文件 / Files

| 文件 / File | 语言 / Language | 说明 / Description |
|------|------|------|
| `SKILL.md` | 中文（默认）/ Chinese (default) | 完整方法论 + 9个实战验证示例。Coze/中文Agent直接加载此文件 / Full methodology + 9 verified examples. Loaded by Coze/Chinese agents |
| `SKILL_EN.md` | English | Full methodology + 5 verified examples. For international agents |
| `main.py` | Python | 提示词优化器 / Prompt optimizer, auto-detects style/era/realism level |

## 使用方式 / Usage

### 方式一：作为 Agent Skill 使用 / As an Agent Skill
中文Agent / Chinese agents: 将 `SKILL.md` 放入技能目录 / Place `SKILL.md` in your skill directory
International agents: Place `SKILL_EN.md` in your skill directory (rename to `SKILL.md`)

### 方式二：直接使用 Python 脚本 / Use Python Script
```bash
python main.py
```
修改 `main.py` 底部的 `test_inputs` 列表即可生成不同场景的提示词。
Modify `test_inputs` at the bottom of `main.py` to generate prompts for different scenes.

### 方式三：直接参考方法论写提示词 / Reference the Methodology
阅读 `SKILL.md`（中文）或 `SKILL_EN.md`（英文）中的方法论和示例，手动构建提示词，粘贴到任何AI图片生成工具中使用。
Read the methodology and examples in `SKILL.md` (Chinese) or `SKILL_EN.md` (English), manually construct prompts, and paste into any AI image generation tool.

## 灵感来源 / Inspiration

本 Skill 的核心创作思路灵感来源于 B 站视频：[豆包也能生成超真实图片！](https://www.bilibili.com/video/BV1ku7R6iE54)

在此基础上，经过 6 个场景、40+ 轮实测迭代，总结出"黄金三段式"提示词结构与年代分级系统。方法论本身是模型无关的，适用于所有AI图片生成工具。

The core creative approach was inspired by this Bilibili video: [Doubao can generate hyperrealistic images too!](https://www.bilibili.com/video/BV1ku7R6iE54)

After 6 scenes and 40+ rounds of testing, the "Golden Three-Part Prompt Structure" and era grading system were developed. The methodology is model-agnostic and works with all AI image generation tools.

## License

MIT
