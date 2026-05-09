import os
import requests
import json
import base64

API_KEY = "AIzaSyCbFyyoSXJYVtynvFMD8rfYTEfk_f9q38c"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-4.0-generate-001:predict?key={API_KEY}"

def generate_image(prompt, filename):
    print(f"Generating {filename}...")
    headers = {"Content-Type": "application/json"}
    data = {
        "instances": [{"prompt": prompt}],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "3:4",
            "personGeneration": "DONT_ALLOW"
        }
    }
    
    response = requests.post(URL, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()
        if "predictions" in result and len(result["predictions"]) > 0:
            b64_img = result["predictions"][0]["bytesBase64Encoded"]
            with open(filename, "wb") as f:
                f.write(base64.b64decode(b64_img))
            print(f"Saved {filename}")
        else:
            print("No prediction found:", result)
    else:
        print(f"Error {response.status_code}: {response.text}")

prompts = {
    "assets/an_naba/bg_nature.png": "A beautiful soft pastel watercolor painting of a grassy field. The bottom edge features rolling green hills, small blooming flowers, and leafy branches. The top corners have subtle hanging vines. The vast center area is a very light, smooth, completely blank pastel green gradient with zero details. Flat 2D texture. Dreamy, magical, clean, minimalist, no text, no words, no characters."
}

for filename, prompt in prompts.items():
    generate_image(prompt, filename)
