---
name: hyperrealistic-image
description: Generate hyperrealistic, everyday-looking photos. Core principle: writing "realistic" or "photo" just triggers an AI style. You need specific devices, shooting logic, imperfections, and the "Golden Three-Part Prompt Structure" to make images that look like they were actually taken by a real person. Triggered by keywords like "real photo", "looks like a snapshot", "film feel", "candid", "old photo", "street photography", "imperfect".
category: ["Image & Design"]
---

# Hyperrealistic Image Generator

## Attribution & Inspiration

The core creative approach was inspired by this Bilibili video:
[Doubao can generate hyperrealistic images too!](https://www.bilibili.com/video/BV1ku7R6iE54)

After 6 scenes and 40+ rounds of testing and iteration, the "Golden Three-Part Prompt Structure" and era grading system were developed into the complete methodology in this Skill.

> **Note:** This skill was extensively tested and optimized on Doubao (豆包). Results may be better on Doubao than other models. The methodology itself is model-agnostic and works with Midjourney, DALL-E, Stable Diffusion, Flux, and others, but some parameters may need fine-tuning for best results.

## Core Principle

Writing "realistic", "photoreal", or "photo-level" just triggers an AI style. To generate true photorealism, you need **specific, perceivable imperfections** to guide the model into thinking you're describing a real photo that actually exists.

> **Realism = Specific Device + Shooting Logic + Quality Flaws + Imperfect Details + Ordinary People + Anti-AI Negation**

**⚠️ The most important rule: Device names are NOT decorative words!**

Writing "Sony Cyber-shot" doesn't equal realism — the AI will treat it as a prop and continue using overhead angles, perfect composition, and refined lighting. **Device names must be paired with the actual shooting logic of that era/device:**

| Device | Real Shooting Logic | AI Default Mistakes |
|--------|-------------------|---------------------|
| 2000s knockoff phone | One-handed, tilted frame, extremely low res | Overhead angle, centered subject, sharp image |
| 2000s point-and-shoot | Eye-level quick snap, tilted, no waiting | Overhead angle, centered, perfect moment |
| 1970s photo studio | Studio-posed, frontal flash, cloth backdrop | Artistic gradient background, soft light, natural expression |
| Old phone candid | One-handed, tilted, foreground intrusion | Professional composition, clean frame, precise focus |
| Film camera | Heavy grain, color shift, misfocus | High-res sharp, accurate color, perfect depth of field |

**So the first part must include BOTH: what device + how a person using that device would shoot.** Writing only the device name without shooting logic is useless.

**Key Findings:**
- Saying "blurry" tends to produce pixel art → Use "low resolution", "soft details", "focus isn't quite right"
- Saying "grain" can look like oil painting → Use "noise", "film grain", "scan quality"
- People must be described as "everyone looks different" → Otherwise AI uses template faces
- The older the era, the more yellowing, fading, and blur increase progressively
- Walls and buildings must be described as "mottled, irregular, weathered" → Otherwise AI produces 3D-render look
- Multi-person scenes must emphasize "everyone faces the same direction" → Otherwise AI scrambles body orientations
- **Writing device name without shooting logic → AI ignores era constraints and uses default perfect composition** → Must explicitly write "held up the camera and pressed the shutter", "terrible composition", "studio-posed" etc.
- **Saying "low saturation" gets discount-applied by the model** → Use extreme repetition: "extremely extremely low saturation", "drab and yellowish", "not a single color is vivid", "every color is covered in gray and yellow". Be dramatic. Saying it once isn't enough — repeat and intensify.

## Golden Three-Part Prompt Structure

A highly effective structure verified through 6 scenes and 40+ rounds of testing:

### Part 1 (Top, highest weight): Era + Device + Shooting Logic + Color + Quality
Use **specific era** + **specific device name** + **how a person using that device would shoot** + **specific color/quality description** to lock in the overall style. This part determines 80% of the final result.

**⚠️ Shooting logic is mandatory!** Writing only the device name without "how a person would shoot with it" means the AI will ignore era constraints and use default perfect composition.

✅ Good openings (all include shooting logic):
- "1970s old photo, shot with a Seagull 120 TLR camera in a photo studio, the photographer told everyone to stand still, frontal flash fired, stiff and unnatural expressions, severely faded and yellowed, extremely low saturation, poor quality, low resolution, lots of noise"
- "1990s color photo, shot with Kodak Gold film on a point-and-shoot, held up and pressed the shutter without caring about composition, frame is slightly tilted, severely faded, overall yellowish and dark, hazy like covered in fog"
- "2000s Sony Cyber-shot point-and-shoot, casually held up and pressed, terrible composition, frame slightly tilted, average quality, low resolution, lots of noise, dull grayish colors, color shift toward yellow and green"
- "Taken with a phone, casually, didn't focus before pressing, frame slightly tilted, random composition, average quality, not high-res, slight digital noise, white balance off, dull colors with low saturation"

❌ Bad openings:
- "A realistic photo" (too vague, triggers AI style)
- "Hyperrealistic portrait" (still AI vocabulary)
- "A very blurry photo" (tends to produce pixel art)
- "2000s Sony Cyber-shot, average quality" (❌ Only device name, no shooting logic — AI will ignore era and use perfect composition)

### Part 2 (Middle): Subject Content + Imperfect Details
Describe the subject, but emphasize **ordinary, imperfect, uniquely featured**, to avoid AI template-ification.

- **People**: Ordinary looking, not influencer faces, everyone looks different with their own features. Average-sized eyes. Natural, slightly stiff expressions. Skin has pores, blemishes. Clothes are slightly old with wrinkles.
- **Buildings/Environment**: Mottled walls, peeling paint, water stains, dirty and old. Old signs with peeling paint, no vivid colors.
- **Composition**: Slightly tilted, off-center, slightly cropped, casually shot.
- **Objects**: Slightly old, scratched, not brand new and perfect.
- **Multi-person scenes**: Everyone faces the same direction, absolutely no one facing the camera, only backs of heads visible.

### Part 3 (Ending, for sealing): Negation Descriptions
Use "not XX" sentence patterns to suppress AI feel.

Must-add phrases (pick 2-3):
- Not a retouched photo
- Not AI-generated
- Not professional photography
- Not a high-res image
- Just a casual photo taken by an ordinary person
- Just a very ordinary photo

## Era Grading System (Verified)

Old photos from different eras have completely different qualities — you can't use the same parameters.

| Era | Yellowing | Fading | Quality | Saturation | Typical Devices |
|-----|-----------|--------|---------|------------|-----------------|
| 1970s | Severe | Severe, near B&W with faint color | Poor, blurry, unclear detail | Very low | Film cameras, Seagull, Shanghai brand |
| 1990s | Moderate | Noticeable, muted colors | Average, heavy grain | Low | Kodak Gold, Fuji film, point-and-shoot |
| 2000s | Yellowish-gray | Noticeable, dull and muted | Average, digital feel, low-res | Low | Knockoff phones, early digicams, camera phones, point-and-shoot |
| 2010s | Minimal | Almost none | Good, clear but not modern | Medium | Smartphones, digital cameras |

**1970s keywords**: severe yellowing, severe fading, extremely low saturation, drab, poor quality, blurry, film grain, mottled walls, plain clothes, no vivid colors, wooden signs, slogans

**1990s keywords**: yellowing, fading, low contrast, hazy, heavy grain, Kodak Gold film, old furniture, vintage clothing, studio backdrops

**2000s keywords**: yellowish-gray, dull muted colors, noticeable fading, low saturation, digital noise, low resolution, soft details, knockoff phones, old phones, point-and-shoot, period-appropriate clothing

## 5 Realism Style Presets

| Style | Core Device/Medium | Opening Template Example | Use Cases |
|-------|-------------------|-------------------------|-----------|
| 📱 Phone Snapshot | Smartphone / Old phone | "Taken with a phone, casually, one-handed, frame slightly tilted, random composition, average quality, not high-res, slight digital noise, white balance off, dull colors with low saturation" | Daily life, vlog, selfies, campus life |
| 🎞️ Film Feel | Kodak Gold / Fuji C200 | "Shot on Kodak Gold film, heavy grain, warm yellowish tones, low contrast, slightly faded feel, slight vignette" | Artistic, vintage, mood, portraits |
| 📷 Documentary Street | Leica / Ricoh GR / Point-and-shoot | "Documentary street photo, held up and pressed the shutter, tilted composition, authentic messy feel, high contrast, hard light, film grain, slight motion blur" | Street, human interest, storytelling |
| 🏠 Life Record | Phone indoor | "Shot indoors with a phone, warm yellow lighting, yellowish white balance, average quality with noise, white balance off, stuff on the table, casual home snapshot feel" | Home, daily life, cozy, food |
| 📼 Vintage Photo | Film + scan | "1990s old photo, shot on film, severely faded and yellowish-dark, low contrast hazy, average quality heavy grain, dust and scratches, scanned from old album" | Nostalgia, 70s/90s/00s, family portraits, old photos |

## Usage

### Basic
```
Hyperrealistic generate: [your description]
```

### Specify style
```
Film feel generate: a person on a rainy street
```

### Maximize realism
```
Max realism: a girl reading in a cafe
```

### Specify era
```
1990s family portrait
```
```
2008 street scene
```
```
1970s city street
```

## Anti-AI Keyword Library

These phrases are combat-tested to effectively suppress AI feel. Add selectively based on image content:

### People (must-add when people are present)
- Ordinary looking, not an influencer face, not a celebrity face
- Everyone looks different, each with their own features
- Plain features, so average you wouldn't find them in a crowd
- Average-sized eyes, not big eyes, not cartoon eyes
- Skin has pores, blemishes, freckles, skin texture, not smooth
- Face has minor flaws, not flawless
- Imperfect expressions, slightly stiff, slightly unnatural, slightly dull
- Hair slightly greasy and messy, with stray strands
- Clothes slightly old, with wrinkles
- Not posing, not modeling, very casual and unpolished
- Not looking at the camera, natural state

### Quality
- Average quality, not high resolution
- Details aren't sharp, soft
- Has noise, digital noise
- Focus isn't quite right, slightly soft
- Not a high-res image
- Colors aren't vivid, low saturation
- Low contrast, hazy

### Buildings/Environment
- Mottled walls, peeling paint, water stains (only where appropriate — old streets, old neighborhoods)
- Dirty and old (only where appropriate)
- Not a neat brick wall
- Old signs, peeling paint
- Signs of age
- ⚠️ **Normal places (cafes, malls, offices) don't need to be described as run-down** — just "ordinary, slightly tacky, unpolished, not fancy" is realistic enough
- ⚠️ **Imperfect ≠ dilapidated** — a mid-range cafe that's clean but tacky is actually the most realistic

### Composition
- Composition slightly tilted
- Subject not centered
- Top/side slightly cropped
- Casual shot, no attention to composition
- Slight foreground obstruction

### Negation (must add 2-3 at the end)
- Not a retouched photo
- Not AI-generated
- Not professional photography
- Not a high-res image
- Not a posed shot
- Not a painting
- Not pixel art
- Just a casual photo by an ordinary person
- Just a very ordinary photo

### Multi-person Scenes (must-add when 2+ people)
- Everyone faces the same direction
- Every person's face is turned away from the camera, only backs of heads visible
- Absolutely no one facing the camera
- No front-facing faces
- Everyone's orientation is unified, no one turned their head
- All figures face the same way

## Verified Examples

### Example 1: 1990s Family Portrait (Verified ✅)
```
1990s color old photo, shot on Kodak Gold film at a photo studio, the photographer told everyone to stand still and look at the camera, frontal flash went off, expressions are stiff and wooden, standing straight. Faded badly over twenty-plus years, colors overall yellowish and dark, very low contrast, hazy like covered in fog, whites turned cream-yellow, blacks are grayish not truly black, colors aren't bright at all, muted. Quality is a bit blurry, heavy grain, photo has dust and tiny scratches. Scanned from an old album, just a very ordinary family portrait, no white border, no frame, just the photo itself. A family, everyone looks different, each with their own features, all ordinary-looking people, not celebrity faces, not template influencer faces, skin has texture and pores, wearing old-fashioned clothes. Background is the studio's blue cloth backdrop, backdrop has wrinkles and stains, fake flowers and rocks nearby. Not a retouched photo, not AI-generated, just a very old ordinary family photo.
```

### Example 2: 2008 Street Candid (Verified ✅)
```
2008, shot with an old phone, one-handed, pressed the shutter, composition is tilted, subject off-center, top cropped a bit, casually shot with no attention to composition, a passerby's arm intrudes into the foreground. Quality is very poor, very blurry, lots of noise, heavy grain, colors are dull and not vivid, slightly color-shifted toward yellow, very low resolution, just the level of an ordinary phone from that year, not high-res. Frame is very simple, just a girl standing by the street, background is an ordinary street and wall, nothing too cluttered. Girl looks very ordinary, not an influencer face, average skin with blemishes, messy hair, wearing an old gray jacket and jeans, no makeup or very light makeup. She's looking down at her phone, holding an old slider phone, screen facing herself, phone is old with scratches. She has no idea someone is taking her photo, very natural and relaxed state. No white border, no frame, just a very average photo. Not a retouched photo, not AI-generated, not professional photography, just casually shot by an ordinary person.
```

### Example 3: 1970s Street Scene (Verified ✅)
```
1970s old photo, shot with an old film camera, over forty years old. Colors severely faded, overall yellowish-gray, extremely low saturation, almost no vivid colors, every color covered in yellow and gray, drab and yellowish. Poor quality, low resolution, details hard to make out, a bit blurry but not pixel art. Has film grain, has noise. Photo is old, has dust, has fine scratches, all random. The scene is a 1970s city street. Bicycles on the road, a few scattered people, all wearing gray, blue, black, army green old clothes, very plain styles, all Mao suits, military-style jackets, straight-leg pants. People are small, ordinary postures, faces can't be seen clearly. Roadside has short old brick buildings, mottled walls, a bit dirty and old, not neat brick walls. White-text red slogans on walls, text is a bit blurry. Shops have wooden signs, characters painted in oil, paint mostly peeled off, old-looking. No neon lights, no LED, nothing modern. Photo is slightly tilted, just casually shot by an ordinary person. Not a retouched photo, not AI-generated, not high-res, not painted. Just a very old, oxidized, yellowed, faded ordinary photo.
```

### Example 4: Classroom Nap Snapshot (Verified ✅)
```
Taken casually with a phone, quality is just an ordinary smartphone in daytime indoor, not high-res but not blurry, very slight digital noise, colors natural not vivid, auto white balance slightly warm, not that sharp DSLR quality. Lunchtime, napping at desk in classroom, lights off, curtains drawn, soft diffused light coming in, overall dim but everything is visible. Normal seated position looking slightly down, frame slightly tilted, not perfectly level, composition not deliberate, just held up and shot, bottom-left corner shows a tiny bit of own finger edge. All classmates ahead are facing away, napping face-down on desks, only backs of heads and backs visible, all facing the blackboard, absolutely no one facing the camera, no front faces, no one turned around. Everyone's orientation is consistent. Desks have books, pens, water bottles, things scattered around. Not professional photography, not deliberate composition, just a student's casual daily snapshot, not a retouched photo, not AI-generated.
```

### Example 5: 2000s Chinese Cafe Snapshot (Verified ✅)
```
2000s, in a Chinese cafe, shot casually with an old point-and-shoot digital camera from that era. Quality is very poor, very blurry, very low resolution, details can't be seen at all, soft and mushy, tons of noise, heavy grain, colors severely faded, overall yellowish-gray, extremely extremely low saturation, drab and yellowish, like covered in a dirty yellow fog, whites have yellowed, not a single color is vivid, white balance way off, very low contrast, just the garbage quality of the cheapest digital camera from that era, not high-res. Composition slightly tilted, subject left of center not centered, top cropped a bit, slight foreground obstruction, casually shot with zero attention to composition. Scene is a small cafe in a 2000s Chinese city, sign in Chinese, ordinary printed sign, paint partially peeled. Interior is simple, wooden tables and chairs looking old, walls a bit dirty with water stains and mottling, warm yellow lighting uneven, some areas dark some bright. Table has a coffee cup, cup is old with water stains, also a newspaper or magazine. One person sitting at the table, very ordinary looking, typical Chinese young person, not an influencer face, not a celebrity, average-sized eyes, skin has pores and texture, hair a bit messy with stray strands, wearing 2000s-era clothes, loose sweater or jacket, dull old-looking colors. Expression very natural, not looking at camera, head down stirring coffee. Background has a couple people, also ordinary Chinese, each doing their own thing. Whole frame is dirty and old-looking, very era-appropriate. Not a retouched photo, not AI-generated, not professional photography, not high-res, not posed, just a casual snapshot by an ordinary person, a very ordinary old photo.
```

## Tuning Guide

When results aren't right, adjust in this order:

1. **Composition too perfect / angle wrong** → Most common! Add shooting logic: "held up the camera and pressed the shutter", "terrible composition", "studio-posed", "passerby intruded into foreground". Device name alone isn't enough — must describe how a person using that device would shoot
2. **Colors wrong** → Strengthen opening color description (yellowish/grayish/bluish/faded), deeper for older eras
3. **People too AI** → Add "everyone looks different", "not an influencer face", "average-sized eyes"
4. **Quality too good** → Add "low resolution", "soft details", "has noise"
5. **Buildings too fake** → Add "mottled walls", "not a neat brick wall", "old-looking"
6. **Looks like a painting** → Remove "grain", use "noise", "scan quality", add "not a painting"
7. **Looks like pixel art** → Don't say "blurry", use "low resolution", "soft details", add "not pixel art"
8. **Still fake overall** → Add more negation phrases at the end (not retouched, not AI-generated, not professional)
9. **People facing wrong directions (multi-person)** → Add "everyone faces the same direction", "absolutely no one facing the camera", "only backs of heads visible" — the more you emphasize, the better
10. **Lighting wrong** → Clearly describe light source (curtain diffuse/lamp/natural), brightness (dim/soft/bright), color temperature (warm yellow/cool white)
11. **Too sharp for a phone** → Add "slight digital noise", "white balance off", "low saturation" — don't say "blurry", say "average quality"
12. **First-person view feels fake** → Add "can see a bit of own hand/phone edge", "slightly looking-down angle", "eye-level height"
13. **Family portrait doesn't look right** → Studio scenes must include: solid blue cloth backdrop (not gradient), frontal flash (not soft light), studio-posed (not natural expressions), stiff positioning (not warm interaction)
14. **Street photo doesn't look right** → Must include: quick shutter press (not waiting for perfect moment), tilted composition (not centered/symmetric), foreground intrusion (not clean frame)

## Common Pitfalls

### Pitfall 1: "Blurry" ≠ Realism
Saying "blurry" or "very blurry" tends to produce pixel art or over-blurred images. Correct phrasing: "average quality", "low resolution", "soft details", "focus isn't quite right". Real phone photos are clear but not sharp — they have noise but aren't blurry.

### Pitfall 2: Multi-person Orientation Chaos
With 2+ people, the AI will almost certainly mess up someone's facing direction. Must actively, repeatedly, forcefully emphasize orientation consistency: "everyone faces away from camera", "absolutely no one facing the camera", "only backs of heads and backs visible". The more emphasis, the better the result.

### Pitfall 3: Lighting is Hard to Calibrate
Saying "very dark" produces all-black frames, "very bright" looks like studio lighting. Correct approach — describe light source and brightness relationship:
- Curtained classroom: "curtains drawn, soft diffused light coming in, overall dim but everything visible"
- Overcast outdoor: "overcast natural light, soft not harsh, overall cool tone"
- Night indoor: "warm yellow lamp, only one light, surroundings quite dark, obvious light-shadow contrast"

### Pitfall 4: First-person View Breaks Immersion
If the first-person view is too "straight" or "clean", it doesn't feel like a real person shot it. Add these details:
- Frame edge shows a bit of own hand/finger/phone bezel
- Angle slightly low or high, not perfectly eye-level
- Slight foreground obstruction (own arm, desk edge)
- Frame has slight tilt

### Pitfall 5: Only Change One Parameter at a Time
Don't change multiple variables simultaneously during iteration — you won't know which adjustment worked. Fix one issue at a time (colors first, then lighting, then composition), find a satisfactory baseline, then fine-tune the next dimension.

### Pitfall 6: Device Name Without Shooting Logic (Most Critical!)
The most crucial issue discovered in v6. Writing "2000s Sony Cyber-shot" ≠ realism — AI treats the camera model as decoration and continues using overhead angles, perfect composition, refined lighting. **Must simultaneously write "how a person using this device would shoot"**:
- Point-and-shoot street → "held up the camera and pressed the shutter, terrible composition, frame slightly tilted, passerby intruded into foreground"
- Studio family portrait → "photographer told everyone to stand still, frontal flash went off, stiff and unnatural expressions"
- Old phone casual → "held up one-handed, didn't focus properly, frame a bit tilted"

**Test**: If your first part only has era + device + quality description, but nothing about "how it was shot" (posture, composition habits, shooting method), you're falling into this pitfall.

### Pitfall 7: "Low Saturation" Gets Discounted
Models naturally discount degree words like "low" and "average". Writing "low saturation" might still produce fairly vivid images, "faded" might only slightly shift color. Must use extreme repetition: "extremely extremely low saturation", "drab and yellowish", "not a single color is vivid". Once isn't enough — repeat, and use negation: "absolutely not vivid" for double-sealing.

### Pitfall 8: Imperfect ≠ Dilapidated
When writing "dirty and old", "mottled", "water stains", the AI turns normal places into condemned buildings. Cafes become demolition sites, malls become abandoned ruins. **Distinguish by scene**:
- Genuinely old places (old streets, old neighborhoods, 1970s buildings) → Can use "mottled, peeling, dirty, old"
- Normal places (cafes, malls, offices) → Use "ordinary, slightly tacky, unpolished, not fancy" — never "run-down" or "dirty"
- **Mid-range cafe style**: Clean but unpolished, slightly tacky decor — this is the most authentic 2000s Chinese cafe look

## License

MIT
