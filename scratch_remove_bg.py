from PIL import Image

def remove_white_bg(input_path, output_path, tolerance=15):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    new_data = []
    
    # 255 - tolerance
    threshold = 255 - tolerance
    
    for item in data:
        # Check if the pixel is close to white
        if item[0] > threshold and item[1] > threshold and item[2] > threshold:
            new_data.append((255, 255, 255, 0)) # Transparent
        else:
            new_data.append(item)
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

if __name__ == "__main__":
    remove_white_bg(
        r"c:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\assets\an_naba\character_naba.png",
        r"c:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\assets\an_naba\character_naba.png"
    )
    print("Background removed via PIL.")
