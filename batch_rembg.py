import os
from rembg import remove
from PIL import Image

images = {
    "naba_praying.png": r"C:\Users\Win11\.gemini\antigravity\brain\ea426a93-a5d8-47c8-8974-0a3a8f6c234b\naba_praying_1778245381947.png",
    "naba_sitting.png": r"C:\Users\Win11\.gemini\antigravity\brain\ea426a93-a5d8-47c8-8974-0a3a8f6c234b\naba_sitting_quran_1778245396150.png",
    "lantern.png": r"C:\Users\Win11\.gemini\antigravity\brain\ea426a93-a5d8-47c8-8974-0a3a8f6c234b\element_lantern_1778245414023.png",
    "telescope.png": r"C:\Users\Win11\.gemini\antigravity\brain\ea426a93-a5d8-47c8-8974-0a3a8f6c234b\element_telescope_1778245446840.png",
    "cloud.png": r"C:\Users\Win11\.gemini\antigravity\brain\ea426a93-a5d8-47c8-8974-0a3a8f6c234b\element_cloud_stars_1778245465084.png"
}

out_dir = r"c:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\assets\an_naba"

for out_name, in_path in images.items():
    print(f"Processing {out_name}...")
    try:
        input_img = Image.open(in_path)
        output_img = remove(input_img)
        out_path = os.path.join(out_dir, out_name)
        output_img.save(out_path)
        print(f"Saved to {out_path}")
    except Exception as e:
        print(f"Error on {out_name}: {e}")

print("Batch background removal complete.")
