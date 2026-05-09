import os
from google import genai
from google.genai import types
from rembg import remove
from PIL import Image
from io import BytesIO

# Read API Key from .env
api_key = None
with open(".env", "r") as f:
    for line in f:
        if line.startswith("GOOGLE_API_KEY="):
            api_key = line.strip().split("=")[1]

if not api_key:
    print("Error: GOOGLE_API_KEY not found in .env")
    exit(1)

client = genai.Client(api_key=api_key)

out_dir = r"c:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\assets\an_naba"
os.makedirs(out_dir, exist_ok=True)

# Premium Islamic decorative elements
assets = {
    "frame_ornate.png": "An extremely ornate golden Islamic arabesque rectangular border frame, intricate geometric patterns with floral motifs, no text, isolated on pure white background, luxury gold foil style, high detail, 8k quality",
    "corner_arabesque.png": "A single ornate golden Islamic arabesque corner ornament with intricate geometric and floral patterns, luxury gold foil embossing style, isolated on pure white background, high detail",
    "divider_ornate.png": "A wide horizontal ornate golden Islamic arabesque divider separator, intricate geometric pattern with a central medallion, luxury gold foil style, isolated on pure white background, high detail",
    "bismillah_ornament.png": "An ornate golden Islamic calligraphy frame border surrounding empty space, with intricate arabesque floral vines and geometric patterns, luxury gold foil embossing style, isolated on pure white background, high detail",
    "medallion_ayat.png": "A small ornate golden Islamic octagonal medallion with intricate geometric pattern inside, luxury gold foil style, isolated on pure white background, high detail"
}

print("Starting asset generation and background removal...")

for filename, prompt in assets.items():
    print(f"\n--- Generating {filename} ---")
    try:
        response = client.models.generate_images(
            model='imagen-4.0-generate-001',
            prompt=prompt,
            config=types.GenerateImagesConfig(
                number_of_images=1,
                aspect_ratio="1:1",
                output_mime_type="image/jpeg"
            )
        )
        
        if response.generated_images:
            img_bytes = response.generated_images[0].image.image_bytes
            
            # Load into PIL
            input_img = Image.open(BytesIO(img_bytes))
            
            # 2. Remove Background
            print("Removing background...")
            output_img = remove(input_img)
            
            # 3. Save
            out_path = os.path.join(out_dir, filename)
            output_img.save(out_path, "PNG")
            print(f"Saved {filename}")
        else:
            print("Error: No predictions found in response")
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")

print("\nDone!")
