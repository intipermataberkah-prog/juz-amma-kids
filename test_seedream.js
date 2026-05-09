const fs = require('fs');

async function run() {
    const apiKey = '8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002';
    const filePath = 'C:/Users/Win11/Documents/Permata_KIds/JUZ AMMA/juzamma_v2_output/112_al_ikhlas_v2.png';
    const outputPath = 'C:/Users/Win11/.gemini/antigravity/scratch/juz-amma-kids/112_al_ikhlas_bg_seedream.jpg';
    
    const bitmap = fs.readFileSync(filePath);
    const base64Image = Buffer.from(bitmap).toString('base64');
    const dataUrl = `data:image/png;base64,${base64Image}`;

    const prompt = "A clean background matching the original theme exactly. Deep space, glowing galaxy, stars, magical golden lighting. Empty background for a poster. Absolutely NO TEXT, NO LETTERS, NO WORDS, NO NUMBERS. Pure scenic background.";

    console.log("Sending request to FAL.AI Seedream...");
    
    // We will try the known or guessed seedream endpoints
    const endpoints = [
        "https://queue.fal.run/fal-ai/bytedance/seedream/v5/lite/image-to-image",
        "https://queue.fal.run/fal-ai/bytedance/seedream/v5/lite",
        "https://queue.fal.run/fal-ai/seedream",
        "https://queue.fal.run/fal-ai/seedream/image-to-image"
    ];

    for (let url of endpoints) {
        console.log("Trying", url);
        try {
            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Authorization": `Key ${apiKey}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    image_url: dataUrl,
                    prompt: prompt,
                    strength: 0.95,
                    image_size: "portrait_4_3" // common for A4-ish
                })
            });
            
            if (!response.ok) {
                console.log("Failed:", response.status, await response.text());
                continue;
            }
            
            const data = await response.json();
            console.log("Success with", url, data);
            
            let statusUrl = data.status_url;
            let responseUrl = data.response_url;

            if (statusUrl) {
                let status = 'IN_QUEUE';
                while (status === 'IN_QUEUE' || status === 'IN_PROGRESS') {
                    await new Promise(r => setTimeout(r, 2000));
                    const statusRes = await fetch(statusUrl, { headers: { "Authorization": `Key ${apiKey}` } });
                    const statusData = await statusRes.json();
                    status = statusData.status;
                }

                if (status === 'COMPLETED') {
                    const finalRes = await fetch(responseUrl, { headers: { "Authorization": `Key ${apiKey}` } });
                    const finalData = await finalRes.json();
                    
                    if (finalData.images && finalData.images.length > 0) {
                        const imgUrl = finalData.images[0].url;
                        console.log("Downloaded Image URL:", imgUrl);
                        
                        const imgBuffer = Buffer.from(await (await fetch(imgUrl)).arrayBuffer());
                        fs.writeFileSync(outputPath, imgBuffer);
                        console.log("Saved to:", outputPath);
                        return;
                    }
                }
            }
        } catch (e) {
            console.error("Error with", url, e);
        }
    }
}

run();
