import requests, time, os, base64

FAL_API_KEY = "8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002"
OUTPUT_DIR  = r"C:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\backgrounds"
HEADERS     = {"Authorization": "Key " + FAL_API_KEY, "Content-Type": "application/json"}

img_path = r"C:\Users\Win11\Documents\Permata_KIds\JUZ AMMA\juzamma_v2_output\112_al_ikhlas_v2.png"
with open(img_path, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")
data_url = f"data:image/png;base64,{b64}"

def test_edit():
    url = "https://queue.fal.run/fal-ai/bytedance/seedream/v4.5/edit"
    print(f"Testing {url} ...")
    r = requests.post(
        url,
        headers=HEADERS,
        json={
            "image_urls": [data_url],
            "prompt": "Remove all children, humans, characters, people, text, letters, and numbers. Leave ONLY the pure empty cosmic space background.",
        },
        timeout=60
    )
    if r.status_code not in (200, 201):
        print(f"Submit failed {r.status_code}: {r.text[:200]}")
        return
    data = r.json()
    job = {"request_id": data["request_id"], "status_url": data["status_url"], "response_url": data["response_url"]}
    
    start = time.time()
    while True:
        time.sleep(4)
        elapsed = int(time.time() - start)
        sr = requests.get(job["status_url"], headers=HEADERS, timeout=15)
        if sr.status_code != 200: continue
        d = sr.json()
        status = d.get("status", "?")
        print(f"[{elapsed}s] {status}")
        if status == "COMPLETED":
            rr = requests.get(job["response_url"], headers=HEADERS, timeout=30)
            images = rr.json().get("images", [])
            if images:
                img_url = images[0]["url"]
                print("Downloaded Image URL:", img_url)
                # Download and save
                out_path = os.path.join(OUTPUT_DIR, "112_al_ikhlas_bg_edit_test.png")
                r_img = requests.get(img_url)
                with open(out_path, "wb") as f_img:
                    f_img.write(r_img.content)
                print("Saved to:", out_path)
            return
        elif status in ("FAILED", "failed", "error"):
            print("Job failed:", d)
            return
        if elapsed > 300:
            print("Timeout!")
            return

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    test_edit()

if __name__ == "__main__":
    main()
