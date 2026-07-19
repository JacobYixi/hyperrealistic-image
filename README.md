# Hyperrealistic Image

**English** | [中文](README_ZH.md)

> Generate hyperrealistic, everyday-looking photos. Not "looks realistic" — but "is just an ordinary photo."

Works with any AI image generation model: Doubao, Midjourney, DALL-E, Stable Diffusion, Flux, etc.

> ⚠️ This skill was extensively tested and optimized on Doubao. Results may be better on Doubao than other models. The methodology is model-agnostic, but some parameters may need fine-tuning for best results.

## Core Principle

Writing "realistic" or "photo" just triggers an AI style. To generate true photorealism, you need **specific, perceivable imperfections** to guide the model.

**Realism = Specific Device + Shooting Logic + Quality Flaws + Imperfect Details + Ordinary People + Anti-AI Negation**

**Golden Three-Part Structure**:
1. **Part 1** (top, highest weight): Era + Device + Shooting Logic + Color + Quality
2. **Part 2** (middle): Subject Content + Imperfect Details
3. **Part 3** (ending): Negation Descriptions (seal the AI feel)

## Supported Styles

| Style | Core Device | Use Cases |
|-------|------------|-----------|
| 📱 Phone Snapshot | Smartphone | Daily life, vlog, campus |
| 🎞️ Film Feel | Kodak Gold film | Artistic, vintage, mood |
| 📷 Documentary Street | Leica, Ricoh GR | Street, human interest |
| 🏠 Life Record | Phone indoor | Home, daily, cozy |
| 📼 Vintage Photo | Film + scan | Nostalgia, retro eras |

## Era Grading

| Era | Yellowing | Fading | Quality | Typical Devices |
|-----|-----------|--------|---------|-----------------|
| 1970s | Severe | Severe | Poor | Seagull, Shanghai brand |
| 1990s | Moderate | Noticeable | Average | Kodak Gold, Fuji film |
| 2000s | Yellowish-gray | Noticeable | Average | Knockoff phones, digicams |
| 2010s | Minimal | Almost none | Good | Early smartphones |

## Files

| File | Language | Description |
|------|----------|-------------|
| `SKILL.md` | Chinese (default) | Full methodology + 9 verified examples. Loaded by Coze/Chinese agents |
| `SKILL_EN.md` | English | Full methodology + 5 verified examples. For international agents |
| `main.py` | Python | Prompt optimizer, auto-detects style/era/realism level |

## Usage

**As an Agent Skill**: Place `SKILL_EN.md` in your skill directory (rename to `SKILL.md`)

**Use Python Script**:
```bash
python main.py
```
Modify `test_inputs` at the bottom to generate prompts for different scenes.

**Reference the Methodology**: Read `SKILL_EN.md`, manually construct prompts, and paste into any AI image generation tool.

## Inspiration

Inspired by [this Bilibili video](https://www.bilibili.com/video/BV1ku7R6iE54). After 6 scenes and 40+ rounds of testing, the "Golden Three-Part Prompt Structure" and era grading system were developed. The methodology is model-agnostic.

## License

MIT
