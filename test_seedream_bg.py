import requests, time, os

FAL_API_KEY = "8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002"
OUTPUT_DIR  = r"C:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\backgrounds"
HEADERS     = {"Authorization": "Key " + FAL_API_KEY, "Content-Type": "application/json"}

# Base style for background ONLY
STYLE_BASE = """3D CGI animation render, Pixar studio quality, subsurface scattering, physically based rendering, volumetric lighting, ray tracing, cinematic depth of field. Children's Islamic storybook full-bleed illustration background. Rich saturated colors, dramatic cinematic lighting. Fully rendered 3D environment.
CRITICAL REQUIREMENT: ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO TYPOGRAPHY.
CRITICAL REQUIREMENT 2: ABSOLUTELY NO CHARACTERS, NO PEOPLE, NO CHILDREN, NO ANIMALS. PURE EMPTY SCENIC LANDSCAPE BACKGROUND ONLY."""

# Scene for An-Naba
scene = "Dramatic split sky at golden dusk. LEFT half: Lush paradise garden with sparkling golden rivers and glowing fruit trees. RIGHT half: Barren rocky grey land. CENTER SKY: Dramatic clouds parting revealing brilliant golden divine light from above. Rich jewel colors, dramatic sky."

def submit_image(prompt):
    r = requests.post(
        "https://queue.fal.run/fal-ai/bytedance/seedream/v4.5/text-to-image",
        headers=HEADERS,
        json={
            "prompt": prompt,
            "image_size": {"width": 1240, "height": 1754},
            "num_inference_steps": 35,
            "num_images": 1,
        },
        timeout=30
    )
    if r.status_code not in (200, 201):
        raise Exception(f"Submit failed {r.status_code}: {r.text[:200]}")
    data = r.json()
    return {"request_id": data["request_id"], "status_url": data["status_url"], "response_url": data["response_url"]}

def poll_image(job, timeout=300):
    start = time.time()
    while True:
        time.sleep(4)
        elapsed = int(time.time() - start)
        r = requests.get(job["status_url"], headers=HEADERS, timeout=15)
        if r.status_code != 200:
            continue
        d = r.json()
        status = d.get("status", "?")
        if status == "COMPLETED":
            rr = requests.get(job["response_url"], headers=HEADERS, timeout=30)
            rr.raise_for_status()
            images = rr.json().get("images", [])
            if images:
                return images[0]["url"]
            raise Exception("No images in response")
        elif status in ("FAILED", "failed", "error"):
            raise Exception(f"Job failed: {d}")
        if elapsed > timeout:
            raise Exception(f"Timeout after {timeout}s")

def download(url, path):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Testing Seedream v4.5 NO TEXT, NO CHARACTERS...")
    prompt = f"{STYLE_BASE}\n\nSCENE: {scene}"
    try:
        job = submit_image(prompt)
        print(f"Polling job {job['request_id']}...")
        url = poll_image(job)
        out_path = os.path.join(OUTPUT_DIR, "078_an_naba_bg_test_nochar.png")
        download(url, out_path)
        print(f"Saved test image to {out_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
