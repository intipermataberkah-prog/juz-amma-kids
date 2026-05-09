const fs = require('fs');
const path = require('path');

const API_KEY = '8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002';
const ASSETS_DIR = path.join(__dirname, 'assets');

const ASSETS_TO_GENERATE = [
    {
        name: 'page_border',
        prompt: 'A delicate watercolor floral border frame for a children\'s Islamic book page. Soft sage green vines, dusty rose flowers, small golden dots, and subtle Islamic geometric star patterns woven into the botanical design. The frame is rectangular with ornate corners. The center is completely empty and transparent. Painted in a soft, dreamy watercolor style on white background. High resolution, print quality.',
        size: { width: 1240, height: 1754 }
    },
    {
        name: 'header_ornament',
        prompt: 'A decorative horizontal header ornament for a children\'s Islamic book. Watercolor style with an elegant Islamic arch shape in the center, flanked by flowing floral vines and arabesque patterns. Colors: sage green, dusty rose, gold accents. Symmetrical design. White background. The center of the arch is empty for text placement. Wide horizontal format. Print quality.',
        size: { width: 1400, height: 500 }
    },
    {
        name: 'divider',
        prompt: 'A horizontal decorative divider ornament for a children\'s Islamic book. Watercolor style. A thin elegant line with a small Islamic star/flower motif in the center, with delicate vine flourishes extending to both sides. Colors: sage green and gold. Simple, refined, not too busy. White background. Wide format. Print quality.',
        size: { width: 1200, height: 200 }
    },
    {
        name: 'medallion',
        prompt: 'A single golden watercolor circular medallion ornament in Islamic style. Ornate border with tiny floral details. The center is empty and white for placing a number. Soft gold and warm brown tones. White background. Square format. Print quality, children\'s book illustration style.',
        size: { width: 400, height: 400 }
    },
    {
        name: 'corner_tl',
        prompt: 'A single watercolor corner ornament for top-left of a book page. Islamic arabesque pattern with flowing vines, small flowers, and golden dots. Sage green, dusty rose, gold. The design radiates from the corner outward. Rest of image is white/transparent. Square format. Print quality.',
        size: { width: 500, height: 500 }
    }
];

async function generateAsset(asset) {
    console.log(`\n🎨 Generating: ${asset.name}...`);
    
    try {
        // Submit to queue
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
            // Direct result (no queue)
            return await downloadImage(data.images[0].url, asset.name);
        }

        // Queue-based
        const statusUrl = data.status_url;
        const responseUrl = data.response_url;
        
        if (!statusUrl) {
            console.error(`  ❌ No status_url for ${asset.name}:`, data);
            return false;
        }

        console.log(`  ⏳ Queued, polling...`);
        
        let attempts = 0;
        while (attempts < 60) {
            await new Promise(r => setTimeout(r, 3000));
            attempts++;
            
            const statusRes = await fetch(statusUrl, {
                headers: { "Authorization": `Key ${API_KEY}` }
            });
            const statusData = await statusRes.json();
            
            if (statusData.status === 'COMPLETED') {
                // Fetch result
                const finalRes = await fetch(responseUrl, {
                    headers: { "Authorization": `Key ${API_KEY}` }
                });
                const finalData = await finalRes.json();
                
                if (finalData.images && finalData.images.length > 0) {
                    return await downloadImage(finalData.images[0].url, asset.name);
                }
                console.error(`  ❌ No images in response for ${asset.name}`);
                return false;
            } else if (statusData.status === 'FAILED') {
                console.error(`  ❌ Failed: ${asset.name}`, statusData);
                return false;
            }
            
            process.stdout.write('.');
        }
        
        console.error(`  ❌ Timeout for ${asset.name}`);
        return false;
        
    } catch (e) {
        console.error(`  ❌ Error generating ${asset.name}:`, e.message);
        return false;
    }
}

async function downloadImage(url, name) {
    try {
        const res = await fetch(url);
        const buffer = Buffer.from(await res.arrayBuffer());
        const filePath = path.join(ASSETS_DIR, `${name}.png`);
        fs.writeFileSync(filePath, buffer);
        console.log(`  ✅ Saved: ${filePath}`);
        return true;
    } catch (e) {
        console.error(`  ❌ Download failed for ${name}:`, e.message);
        return false;
    }
}

async function main() {
    console.log('🚀 Starting AI Asset Generation for Premium Book Design');
    console.log(`   Output: ${ASSETS_DIR}\n`);
    
    let success = 0;
    let failed = 0;
    
    for (const asset of ASSETS_TO_GENERATE) {
        const ok = await generateAsset(asset);
        if (ok) success++;
        else failed++;
    }
    
    console.log(`\n📊 Done! ${success} succeeded, ${failed} failed.`);
}

main();
