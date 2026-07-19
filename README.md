# Hyperrealistic Image

[English](#english) | [中文](#中文)

---

## English

> Generate hyperrealistic, everyday-looking photos. Not "looks realistic" — but "is just an ordinary photo."

Works with any AI image generation model: Doubao, Midjourney, DALL-E, Stable Diffusion, Flux, etc.

> ⚠️ This skill was extensively tested and optimized on Doubao. Results may be better on Doubao than other models. The methodology is model-agnostic, but some parameters may need fine-tuning.

### Core Principle

Writing "realistic" or "photo" just triggers an AI style. To generate true photorealism, you need **specific, perceivable imperfections** to guide the model.

**Realism = Specific Device + Shooting Logic + Quality Flaws + Imperfect Details + Ordinary People + Anti-AI Negation**

**Golden Three-Part Structure**:
1. **Part 1** (top, highest weight): Era + Device + Shooting Logic + Color + Quality
2. **Part 2** (middle): Subject Content + Imperfect Details
3. **Part 3** (ending): Negation Descriptions (seal the AI feel)

### Supported Styles

| Style | Core Device | Use Cases |
|-------|------------|-----------|
| 📱 Phone Snapshot | Smartphone | Daily life, vlog, campus |
| 🎞️ Film Feel | Kodak Gold film | Artistic, vintage, mood |
| 📷 Documentary Street | Leica, Ricoh GR | Street, human interest |
| 🏠 Life Record | Phone indoor | Home, daily, cozy |
| 📼 Vintage Photo | Film + scan | Nostalgia, retro eras |

### Era Grading

| Era | Yellowing | Fading | Quality | Typical Devices |
|-----|-----------|--------|---------|-----------------|
| 1970s | Severe | Severe | Poor | Seagull, Shanghai brand |
| 1990s | Moderate | Noticeable | Average | Kodak Gold, Fuji film |
| 2000s | Yellowish-gray | Noticeable | Average | Knockoff phones, digicams |
| 2010s | Minimal | Almost none | Good | Early smartphones |

### Files

| File | Language | Description |
|------|----------|-------------|
| `SKILL.md` | Chinese (default) | Full methodology + 9 verified examples |
| `SKILL_EN.md` | English | Full methodology + 5 verified examples |
| `main.py` | Python | Prompt optimizer |

### Usage

**As an Agent Skill**: Place `SKILL_EN.md` in your skill directory (rename to `SKILL.md`)

**Use Python Script**: `python main.py` — modify `test_inputs` at the bottom.

**Reference the Methodology**: Read `SKILL_EN.md`, manually construct prompts.

### Inspiration

Inspired by [this Bilibili video](https://www.bilibili.com/video/BV1ku7R6iE54). 6 scenes, 40+ rounds of testing.

### License

MIT

---

## 中文

> 生成超真实、有生活感的图片。不是"看起来真实"，而是"就是一张普通照片"。

适用于任何AI图片生成模型：豆包、Midjourney、DALL-E、Stable Diffusion、Flux、文心一等。

> ⚠️ 本技能的提示词在豆包上进行了大量实测优化，在豆包上的出图效果可能会更优秀。其他模型同样适用，但可能需要微调部分参数。

### 核心原理

直接写"真实"、"写实"、"照片级"只会触发一种AI风格。要生成真正有真实感的图片，需要用**具体的、可感知的不完美特征**来引导模型。

**真实感 = 具体设备 + 拍摄逻辑 + 画质缺陷 + 不完美细节 + 普通人物 + 反AI否定**

**黄金三段式**：
1. **第一段**（置顶，权重最高）：年代 + 设备 + 拍摄逻辑 + 色彩 + 画质
2. **第二段**（中间）：主体内容 + 不完美细节
3. **第三段**（结尾）：否定式描述（封印AI感）

### 支持的风格

| 风格 | 核心设备 | 适用场景 |
|------|---------|---------|
| 📱 手机随手拍 | 智能手机 | 日常记录、生活vlog、校园生活 |
| 🎞️ 胶片感 | 柯达金胶卷 | 文艺、复古、氛围感 |
| 📷 纪实街拍 | 徕卡、理光GR | 街头、人文、故事感 |
| 🏠 生活记录 | 手机室内 | 居家、日常、温馨感 |
| 📼 年代旧照片 | 胶卷+扫描 | 怀旧、70/90/00年代 |

### 年代分级

| 年代 | 泛黄 | 褪色 | 画质 | 典型设备 |
|------|------|------|------|---------|
| 70年代 | 严重 | 严重 | 差 | 海鸥、上海牌 |
| 90年代 | 中度 | 明显 | 一般 | 柯达金、富士 |
| 00年代 | 偏黄灰 | 明显 | 一般 | 山寨手机、卡片机 |
| 10年代 | 不黄 | 几乎无 | 较好 | 早期智能手机 |

### 文件

| 文件 | 语言 | 说明 |
|------|------|------|
| `SKILL.md` | 中文（默认） | 完整方法论 + 9个实战验证示例 |
| `SKILL_EN.md` | English | Full methodology + 5 verified examples |
| `main.py` | Python | 提示词优化器 |

### 使用方式

**作为 Agent Skill**：将 `SKILL.md` 放入技能目录即可

**使用 Python 脚本**：`python main.py`，修改底部 `test_inputs` 列表。

**直接参考方法论**：阅读 `SKILL.md`，手动构建提示词。

### 灵感来源

灵感来源于 B 站视频：[豆包也能生成超真实图片！](https://www.bilibili.com/video/BV1ku7R6iE54)。6个场景、40+轮实测迭代。

### License

MIT
