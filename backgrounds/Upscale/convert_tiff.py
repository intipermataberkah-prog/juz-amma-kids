import os
import glob
from PIL import Image

def convert_tiff_to_jpg():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tiff_files = glob.glob(os.path.join(script_dir, "*.tiff"))
    
    print(f"Found {len(tiff_files)} TIFF files to convert...")
    
    for tiff_file in tiff_files:
        try:
            filename = os.path.basename(tiff_file)
            jpg_filename = filename.replace(".tiff", ".jpg")
            jpg_path = os.path.join(script_dir, jpg_filename)
            
            # Skip if already exists
            if os.path.exists(jpg_path):
                print(f"Skipping {jpg_filename}, already exists.")
                continue
                
            print(f"Converting {filename} -> {jpg_filename}...")
            
            # Open image, convert to RGB (since it might be CMYK), and save as JPG
            with Image.open(tiff_file) as img:
                rgb_img = img.convert('RGB')
                rgb_img.save(jpg_path, 'JPEG', quality=100)
                
            print(f"Successfully converted {filename}")
        except Exception as e:
            print(f"Error converting {filename}: {e}")

if __name__ == "__main__":
    convert_tiff_to_jpg()
    print("All conversions completed.")
