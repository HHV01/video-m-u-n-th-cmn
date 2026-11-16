# PHẦN 2. PROMPT NHÂN VẬT

**Midjourney:** giữ nguyên + tham số cuối. **DALL·E 3:** bỏ `--...`, thêm "Generate this as a clean black and white vector illustration." **Stable Diffusion:** dán phần Negative vào ô Negative, Seed 88888, CFG 7–9, Steps 30–40.

**Thứ tự làm:** A của cả 7 người → kiểm tra tỉ lệ đầu/thân đồng đều → dùng ảnh đã chọn làm reference cho B, C. Nếu AI làm mất phụ kiện, thêm `ALWAYS WEARING`.



## C1 · MINH – Senior Backend Developer
**Phụ kiện bất biến:** Kính vuông (luôn đeo)

### A – Character Sheet (full body)
```text
minimalist stick figure character, simple black line art on pure white background, thick uniform 4px stroke weight, round head, dot eyes, simple curved mouth, no shading, no color, no gradient, flat 2D vector style, full body standing pose, centered composition, generous white space, consistent character design, clean vector illustration, stick figure wearing a hoodie with the hood down, ALWAYS wearing square glasses (two small squares connected by a bridge line), holding a coffee mug in one hand (small cylinder with handle), slightly slouched posture, tired but calm, short hair as 3-4 small vertical lines on top of head, small stubble beard as a few dots on chin, simple pants (two straight lines), simple shoes (two small ovals), neutral face with dot eyes and slight curved mouth
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 1:1 --style raw --v 6
```

### B – Expression Sheet (6 biểu cảm)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, character expression sheet, 6 headshots in a 2x3 grid layout, same character, consistent head size across all 6 panels, clean white space between panels, no labels, no text, no body below shoulders, same character: square glasses ALWAYS ON, short hair (3-4 small lines), stubble dots on chin, hoodie collar visible at neck, Panel 1 (top-left): neutral tired expression, flat slight smile, Panel 2 (top-right): small subtle smile, eyes slightly curved, Panel 3 (middle-left): confused, furrowed brow behind glasses, one eye smaller, Panel 4 (middle-right): frustrated, flat mouth, 2 sweat drops near head, Panel 5 (bottom-left): thinking, one hand on chin, eyes looking up, Panel 6 (bottom-right): surprised, eyes wide behind glasses, small open mouth
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 3:2 --style raw --v 6
```

### C – Scene Prompt (ghép bối cảnh)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, stick figure with square glasses, hoodie, holding coffee mug, [EXPRESSION: neutral / confused / frustrated / thinking / surprised / happy], standing in [BACKGROUND: open workspace / meeting room / pantry / war room], full body visible, facing [left / right / forward], [ACTION: speaking / listening / working on laptop]
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 16:9 --style raw --v 6
```

---

## C2 · LINH – Junior Frontend Developer
**Phụ kiện bất biến:** Tóc đuôi ngựa cao, mắt to hơn 20%

### A – Character Sheet (full body)
```text
minimalist stick figure character, simple black line art on pure white background, thick uniform 4px stroke weight, round head, dot eyes, simple curved mouth, no shading, no color, no gradient, flat 2D vector style, full body standing pose, centered composition, generous white space, consistent character design, clean vector illustration, stick figure with a high ponytail (single curved line extending from back of head), holding an open laptop under one arm (rectangle with keyboard lines), holding a small square sticky note in the other hand, upright eager posture, big round eyes (slightly larger dots than usual), wide enthusiastic smile, simple t-shirt, small earring dot on one ear, simple pants and shoes, body leaning slightly forward with energy
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 1:1 --style raw --v 6
```

### B – Expression Sheet (6 biểu cảm)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, character expression sheet, 6 headshots in a 2x3 grid layout, same character, consistent head size across all 6 panels, clean white space between panels, no labels, no text, no body below shoulders, same character: high ponytail (curved line at back of head), small earring dot, t-shirt collar visible, big round eyes larger than standard, Panel 1 (top-left): neutral curious, slight head tilt, Panel 2 (top-right): big bright smile, eyes as curved arcs (^ ^), Panel 3 (middle-left): confused, one eyebrow up, small '?' above head, Panel 4 (middle-right): frustrated, puffed cheeks, Panel 5 (bottom-left): thinking, eyes looking up, hand on chin, Panel 6 (bottom-right): surprised, wide round eyes, small round 'o' mouth
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 3:2 --style raw --v 6
```

### C – Scene Prompt (ghép bối cảnh)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, stick figure with high ponytail and big round eyes, holding laptop, [EXPRESSION: neutral / confused / frustrated / thinking / surprised / happy], standing in [BACKGROUND: open workspace / meeting room / pantry / war room], full body visible, facing [left / right / forward], [ACTION: speaking / listening / working on laptop]
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 16:9 --style raw --v 6
```

---

## C3 · TRANG – QC / Tester
**Phụ kiện bất biến:** Kính lúp

### A – Character Sheet (full body)
```text
minimalist stick figure character, simple black line art on pure white background, thick uniform 4px stroke weight, round head, dot eyes, simple curved mouth, no shading, no color, no gradient, flat 2D vector style, full body standing pose, centered composition, generous white space, consistent character design, clean vector illustration, stick figure holding a magnifying glass in one hand (circle with handle line, raised near face level), holding a clipboard with a checklist in the other hand (rectangle with 3 small squares and checkmarks), hair in a low bun (small circle at back of head), focused expression with slightly squinted eyes (short horizontal lines), small neutral closed-mouth smile, collared shirt, tiny stud earring dots, upright but leaning slightly forward (observing), simple pants and shoes
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 1:1 --style raw --v 6
```

### B – Expression Sheet (6 biểu cảm)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, character expression sheet, 6 headshots in a 2x3 grid layout, same character, consistent head size across all 6 panels, clean white space between panels, no labels, no text, no body below shoulders, same character: low bun (small circle at back of head), stud earrings, collared shirt neckline, slightly squinted eyes, Panel 1 (top-left): neutral focused, eyes as short horizontal lines, Panel 2 (top-right): gentle closed-mouth smile, eyes softened, Panel 3 (middle-left): confused, tilted head, one eye squinted more, Panel 4 (middle-right): frustrated, flat mouth, small magnifying glass held near face, Panel 5 (bottom-left): thinking, both hands on chin, eyes to the side, Panel 6 (bottom-right): surprised, eyes wide, one hand raised near mouth
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 3:2 --style raw --v 6
```

### C – Scene Prompt (ghép bối cảnh)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, stick figure with low bun, holding magnifying glass and clipboard, [EXPRESSION: neutral / confused / frustrated / thinking / surprised / happy], standing in [BACKGROUND: open workspace / meeting room / pantry / war room], full body visible, facing [left / right / forward], [ACTION: speaking / listening / working on laptop]
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 16:9 --style raw --v 6
```

---

## C4 · ĐỨC – Business Analyst
**Phụ kiện bất biến:** Kính tròn

### A – Character Sheet (full body)
```text
minimalist stick figure character, simple black line art on pure white background, thick uniform 4px stroke weight, round head, dot eyes, simple curved mouth, no shading, no color, no gradient, flat 2D vector style, full body standing pose, centered composition, generous white space, consistent character design, clean vector illustration, stick figure wearing round glasses (two small circles connected by bridge), loose necktie (slightly tilted), holding an open notebook in one hand and a pen in the other, calm attentive posture, head slightly tilted to one side (listening), short neat hair (smooth curved line on top), gentle friendly smile, button-up shirt with small button dots, simple pants and shoes, one hand slightly raised as if explaining
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 1:1 --style raw --v 6
```

### B – Expression Sheet (6 biểu cảm)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, character expression sheet, 6 headshots in a 2x3 grid layout, same character, consistent head size across all 6 panels, clean white space between panels, no labels, no text, no body below shoulders, same character: round glasses, loose necktie visible at collar, short neat hair, Panel 1 (top-left): neutral attentive, head slightly tilted, Panel 2 (top-right): warm friendly smile, eyes gently curved, Panel 3 (middle-left): confused, one eyebrow raised, head tilt, Panel 4 (middle-right): frustrated but composed, flat mouth, one hand raised palm-out (stop gesture), Panel 5 (bottom-left): thinking, hand on chin, eyes looking up, Panel 6 (bottom-right): surprised, raised eyebrows above glasses, small 'oh' mouth
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 3:2 --style raw --v 6
```

### C – Scene Prompt (ghép bối cảnh)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, stick figure with round glasses and loose necktie, holding notebook and pen, [EXPRESSION: neutral / confused / frustrated / thinking / surprised / happy], standing in [BACKGROUND: open workspace / meeting room / pantry / war room], full body visible, facing [left / right / forward], [ACTION: speaking / listening / working on laptop]
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 16:9 --style raw --v 6
```

---

## C5 · SARAH – Product Owner
**Phụ kiện bất biến:** Tóc bob ngang vai

### A – Character Sheet (full body)
```text
minimalist stick figure character, simple black line art on pure white background, thick uniform 4px stroke weight, round head, dot eyes, simple curved mouth, no shading, no color, no gradient, flat 2D vector style, full body standing pose, centered composition, generous white space, consistent character design, clean vector illustration, stick figure with shoulder-length bob hair (curved lines on both sides of head ending at jaw level), simple blazer (two straight lines forming open lapels on torso), holding a takeaway coffee cup in one hand (tall cylinder with lid line), wristwatch on the other arm (small circle on wrist), confident upright posture, one hand on hip, chin slightly raised, bright confident smile with dot eyes, simple pants and professional shoes
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 1:1 --style raw --v 6
```

### B – Expression Sheet (6 biểu cảm)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, character expression sheet, 6 headshots in a 2x3 grid layout, same character, consistent head size across all 6 panels, clean white space between panels, no labels, no text, no body below shoulders, same character: shoulder-length bob hair, blazer lapels visible at shoulders, small wristwatch on one wrist, Panel 1 (top-left): neutral confident, chin slightly up, Panel 2 (top-right): bright assertive smile, eyes curved confidently, Panel 3 (middle-left): confused, one eyebrow sharply raised, head tilt, Panel 4 (middle-right): frustrated, flat mouth, crossed arms, small clock icon nearby, Panel 5 (bottom-left): thinking, finger tapping chin, eyes narrowed, Panel 6 (bottom-right): surprised, eyebrows high, small 'o' mouth
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 3:2 --style raw --v 6
```

### C – Scene Prompt (ghép bối cảnh)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, stick figure with shoulder-length bob hair, blazer, holding coffee cup, [EXPRESSION: neutral / confused / frustrated / thinking / surprised / happy], standing in [BACKGROUND: open workspace / meeting room / pantry / war room], full body visible, facing [left / right / forward], [ACTION: speaking / listening / working on laptop]
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 16:9 --style raw --v 6
```

---

## C6 · HẢI – DevOps Engineer
**Phụ kiện bất biến:** Mũ beanie, luôn cười nửa miệng

### A – Character Sheet (full body)
```text
minimalist stick figure character, simple black line art on pure white background, thick uniform 4px stroke weight, round head, dot eyes, simple curved mouth, no shading, no color, no gradient, flat 2D vector style, full body standing pose, centered composition, generous white space, consistent character design, clean vector illustration, stick figure wearing a beanie hat (small rounded cap with folded brim line), over-ear headphones around the neck, holding a small terminal screen in one hand (rectangle with '>_' prompt), relaxed slouching posture, slight smirk (asymmetric smile, one side higher), one eyebrow slightly raised (one eye slightly higher than the other), simple hoodie, simple pants and sneakers
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 1:1 --style raw --v 6
```

### B – Expression Sheet (6 biểu cảm)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, character expression sheet, 6 headshots in a 2x3 grid layout, same character, consistent head size across all 6 panels, clean white space between panels, no labels, no text, no body below shoulders, same character: beanie hat, over-ear headphones around neck, small terminal icon near one shoulder, always a slight smirk, Panel 1 (top-left): neutral relaxed with slight smirk, Panel 2 (top-right): half-smile, one side up more, Panel 3 (middle-left): confused, one eyebrow up, '?' above head, Panel 4 (middle-right): frustrated, flat mouth, one eye twitching (small zigzag near eye), Panel 5 (bottom-left): thinking, eyes sideways, smirk fading, Panel 6 (bottom-right): surprised, wide eyes, beanie slightly tilted
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 3:2 --style raw --v 6
```

### C – Scene Prompt (ghép bối cảnh)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, stick figure wearing beanie and headphones around neck, holding terminal, [EXPRESSION: neutral / confused / frustrated / thinking / surprised / happy], standing in [BACKGROUND: open workspace / meeting room / pantry / war room], full body visible, facing [left / right / forward], [ACTION: speaking / listening / working on laptop]
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 16:9 --style raw --v 6
```

---

## C7 · MAI – Scrum Master / PM
**Phụ kiện bất biến:** Headset có micro

### A – Character Sheet (full body)
```text
minimalist stick figure character, simple black line art on pure white background, thick uniform 4px stroke weight, round head, dot eyes, simple curved mouth, no shading, no color, no gradient, flat 2D vector style, full body standing pose, centered composition, generous white space, consistent character design, clean vector illustration, stick figure wearing a headset with microphone (band over head, small curved line from ear to mouth), holding a clipboard with sticky notes (rectangle with 3 small squares), hair in a low ponytail (single line at back of head), organized upright posture, warm encouraging smile, one hand gesturing open with palm up (facilitating), simple blouse with small collar, simple pants and professional shoes
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 1:1 --style raw --v 6
```

### B – Expression Sheet (6 biểu cảm)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, character expression sheet, 6 headshots in a 2x3 grid layout, same character, consistent head size across all 6 panels, clean white space between panels, no labels, no text, no body below shoulders, same character: headset with microphone, low ponytail, clipboard visible at shoulder level, Panel 1 (top-left): neutral warm, slight smile, Panel 2 (top-right): encouraging smile, one hand raised in open gesture, Panel 3 (middle-left): confused, head tilt, hand near ear, Panel 4 (middle-right): frustrated but controlled, flat mouth, hand on forehead, Panel 5 (bottom-left): thinking, hand on chin, eyes on clipboard, Panel 6 (bottom-right): surprised, raised eyebrows, hand near headset
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 3:2 --style raw --v 6
```

### C – Scene Prompt (ghép bối cảnh)
```text
minimalist stick figure, simple black line art on pure white background, thick uniform 4px stroke weight, dot eyes, simple curved mouth, no shading, no color, flat 2D vector style, stick figure with headset and low ponytail, holding clipboard with sticky notes, [EXPRESSION: neutral / confused / frustrated / thinking / surprised / happy], standing in [BACKGROUND: open workspace / meeting room / pantry / war room], full body visible, facing [left / right / forward], [ACTION: speaking / listening / working on laptop]
Negative: realistic, photo, 3D render, color, gradient, shading, detailed face, anime, manga, complex background, text, watermark, multiple characters, extra limbs, deformed, blurry, sketchy lines, inconsistent stroke
--seed 88888 --ar 16:9 --style raw --v 6
```

---



---

