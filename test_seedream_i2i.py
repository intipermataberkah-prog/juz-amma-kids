import requests, time, os, base64

FAL_API_KEY = "8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002"
OUTPUT_DIR  = r"C:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\backgrounds"
HEADERS     = {"Authorization": "Key " + FAL_API_KEY, "Content-Type": "application/json"}

# Read Al-Ikhlas image
img_path = r"C:\Users\Win11\Documents\Permata_KIds\JUZ AMMA\juzamma_v2_output\112_al_ikhlas_v2.png"
with open(img_path, "rb") as f:
    b64 = base64.b64encode(f.read()).decode("utf-8")
data_url = f"data:image/png;base64,{b64}"

def test_endpoint(url):
    print(f"Testing {url} ...")
    r = requests.post(
        url,
        headers=HEADERS,
        json={
            "image_url": data_url,
            "prompt": "A clean background matching the original theme exactly. Remove all text, letters, and words. Pure scenic background.",
            "strength": 0.95,
            "image_size": {"width": 1240, "height": 1754},
        },
        timeout=30
    )
    if r.status_code not in (200, 201):
        print(f"Submit failed {r.status_code}: {r.text[:200]}")
        return False
    data = r.json()
    job = {"request_id": data["request_id"], "status_url": data["status_url"], "response_url": data["response_url"]}
    
    start = time.time()
    while True:
        time.sleep(3)
        elapsed = int(time.time() - start)
        sr = requests.get(job["status_url"], headers=HEADERS, timeout=15)
        if sr.status_code != 200: continue
        d = sr.json()
        status = d.get("status", "?")
        print(f"[{elapsed}s] {status}")
        if status == "COMPLETED":
            rr = requests.get(job["response_url"], headers=HEADERS, timeout=30)
            print("SUCCESS!", rr.json())
            return True
        elif status in ("FAILED", "failed", "error"):
            print("Job failed:", d)
            return False

def main():
    endpoints = [
        "https://queue.fal.run/fal-ai/bytedance/seedream/v4.5/image-to-image",
        "https://queue.fal.run/fal-ai/bytedance/seedream/image-to-image",
        "https://queue.fal.run/fal-ai/seedream/v4.5/image-to-image"
    ]
    for ep in endpoints:
        if test_endpoint(ep):
            break

if __name__ == "__main__":
    main()
