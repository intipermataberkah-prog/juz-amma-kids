const fs = require('fs');
const path = require('path');

const API_KEY = '8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002';
const ASSETS_DIR = path.join(__dirname, 'assets', 'an_naba');

// Surah An-Naba = "The Great News"
// Themes: Wonders of creation, mountains, night/day, rain, gardens, Day of Judgment
// Character: A curious Muslim boy named "Naba" with a telescope, exploring nature
// Palette: Deep cosmic blue (#1B2845), golden dawn (#F4C95D), emerald green (#2D8B56), warm sand (#E8D5B5)

const ASSETS = [
    {
        name: 'character_naba',
        prompt: 'A cute cartoon Muslim boy character, age 7, wearing a white thobe and small white kufi cap, holding a golden telescope, looking up at the sky with wonder and amazement. Big expressive sparkly eyes, warm brown skin, friendly smile. He is standing on a grassy hill. Children\'s book illustration style, Pixar-like 3D rendering quality, vibrant colors, soft lighting. Full body shot, white background for easy compositing. High quality digital art.',
        size: { width: 800, height: 1100 }
    },
    {
        name: 'scene_cover',
        prompt: 'A breathtaking children\'s book illustration of a magical night sky scene. A vast cosmic sky filled with swirling galaxies, shooting stars, and a crescent moon, transitioning to dawn at the horizon. Below are majestic purple mountains with snow-capped peaks, a lush green valley with flowers, and gentle rain falling on one side creating a rainbow. The scene represents Allah\'s creation wonders. Style: modern children\'s book illustration, Pixar quality, vibrant blues, purples, golds, and greens. Dreamy, magical atmosphere. No text, no characters.',
        size: { width: 1240, height: 1754 }
    },
    {
        name: 'scene_mountains',
        prompt: 'Children\'s book illustration of magnificent colorful mountains at sunrise. The mountains are stylized and friendly-looking with soft rounded peaks in purple, blue, and teal. Golden sunlight breaks through clouds at the top. Green valleys below with tiny flowers. A gentle waterfall flows down one mountain. Warm, inviting, magical atmosphere. Modern children\'s book digital art style, vibrant colors. No text, no characters.',
        size: { width: 1240, height: 600 }
    },
    {
        name: 'scene_garden',
        prompt: 'Children\'s book illustration of a magical paradise garden. Lush tropical plants, colorful flowers blooming everywhere, fruit trees with golden fruits, a crystal clear stream, butterflies and birds. Warm golden sunlight filtering through the canopy. Everything is vibrant, lush, and inviting. Style: modern Pixar-quality children\'s book illustration. Rich greens, warm golds, pinks, and purples. No text, no characters.',
        size: { width: 1240, height: 600 }
    },
    {
        name: 'scene_night',
        prompt: 'Children\'s book illustration of a peaceful magical night sky. Deep cosmic blue and purple sky filled with twinkling stars, a glowing crescent moon surrounded by soft light, wispy clouds. Below is a silhouette of a gentle town with mosque minarets. Fireflies glow softly. Dreamy, calming, beautiful. Modern children\'s book digital art, Pixar quality. No text.',
        size: { width: 1240, height: 600 }
    },
    {
        name: 'border_frame',
        prompt: 'An ornate decorative border frame for a children\'s book page. The border features intertwined vines, stars, crescent moons, and small flowers in deep blue, gold, and green. The center is completely empty and white. The style is elegant but child-friendly, like a luxury children\'s Quran. The border has a slight watercolor texture. No text.',
        size: { width: 1240, height: 1754 }
    }
];

async function generateAsset(asset) {
    console.log(`\n🎨 Generating: ${asset.name}...`);
    try {
        const response = await fetch("https://queue.fal.run/fal-ai/flux/dev", {
            method: "POST",
            headers: {
                "Authorization": `Key ${API_KEY}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                prompt: asset.prompt,
                image_size: asset.size,
                num_inference_steps: 28,
                guidance_scale: 7.5,
                num_images: 1
            })
        });

        const data = await response.json();
        
        if (data.images && data.images.length > 0) {
            return await downloadImage(data.images[0].url, asset.name);
        }

        const statusUrl = data.status_url;
        const responseUrl = data.response_url;
        if (!statusUrl) { console.error(`  ❌ No queue:`, data); return false; }

        console.log(`  ⏳ Queued...`);
        let attempts = 0;
        while (attempts < 90) {
            await new Promise(r => setTimeout(r, 3000));
            attempts++;
            const statusRes = await fetch(statusUrl, { headers: { "Authorization": `Key ${API_KEY}` } });
            const statusData = await statusRes.json();
            
            if (statusData.status === 'COMPLETED') {
                const finalRes = await fetch(responseUrl, { headers: { "Authorization": `Key ${API_KEY}` } });
                const finalData = await finalRes.json();
                if (finalData.images && finalData.images.length > 0) {
                    return await downloadImage(finalData.images[0].url, asset.name);
                }
                return false;
            } else if (statusData.status === 'FAILED') {
                console.error(`  ❌ Failed:`, statusData); return false;
            }
            process.stdout.write('.');
        }
        return false;
    } catch (e) {
        console.error(`  ❌ Error:`, e.message);
        return false;
    }
}

async function downloadImage(url, name) {
    const res = await fetch(url);
    const buffer = Buffer.from(await res.arrayBuffer());
    const filePath = path.join(ASSETS_DIR, `${name}.png`);
    fs.writeFileSync(filePath, buffer);
    console.log(`  ✅ Saved: ${filePath}`);
    return true;
}

async function main() {
    if (!fs.existsSync(ASSETS_DIR)) fs.mkdirSync(ASSETS_DIR, { recursive: true });
    console.log('🚀 Generating An-Naba character & scene assets...\n');
    
    let ok = 0, fail = 0;
    for (const asset of ASSETS) {
        (await generateAsset(asset)) ? ok++ : fail++;
    }
    console.log(`\n📊 Done! ${ok} succeeded, ${fail} failed.`);
}

main();
