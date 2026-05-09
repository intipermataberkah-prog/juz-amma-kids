from rembg import remove
from PIL import Image

input_path = r"c:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\assets\an_naba\character_naba_original.png"
output_path = r"c:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\assets\an_naba\character_naba.png"

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
print("Background removed perfectly using rembg!")
