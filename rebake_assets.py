"""Re-process all thematic illustrations through rembg for clean transparent backgrounds.
This replaces mix-blend-mode: multiply workaround with proper transparency."""
from rembg import remove
from PIL import Image
import os

assets_dir = r"c:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\assets\an_naba"

# Assets that need clean transparent backgrounds
files_to_process = [
    "naba_mountains.png",
    "naba_night_day.png",
    "naba_rain_garden.png",
    "naba_paradise.png",
    "medallion_ayat.png",
    "divider_ornate.png",
    "corner_arabesque.png",
    "bismillah_ornament.png",
    # Scene backgrounds (used as page-scene-bg)
    "scene_sky.png",
    "scene_mountains.png",
    "scene_rain.png",
    "scene_garden.png",
    "scene_night.png",
]

for f in files_to_process:
    path = os.path.join(assets_dir, f)
    if not os.path.exists(path):
        print(f"  SKIP {f} (not found)")
        continue
    print(f"  Processing {f}...")
    img = Image.open(path)
    out = remove(img)
    out.save(path)
    print(f"  OK {f} done")

print("\nAll assets re-processed with clean transparency!")
