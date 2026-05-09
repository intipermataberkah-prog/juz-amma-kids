const fs = require('fs');

async function run() {
    const apiKey = '8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002';
    const filePath = 'C:/Users/Win11/Documents/Permata_KIds/JUZ AMMA/juzamma_v2_output/112_al_ikhlas_v2.png';
    
    // Read local image to base64
    const bitmap = fs.readFileSync(filePath);
    const base64Image = Buffer.from(bitmap).toString('base64');
    const dataUrl = `data:image/png;base64,${base64Image}`;

    const prompt = "A clean background matching this theme. Deep space, glowing galaxy, stars, golden lighting. Remove all text, words, and letters. Keep it as a beautiful, empty space background suitable for a children's poster. Vertical A4 ratio.";

    console.log("Sending request to FAL.AI...");
    
    try {
        const response = await fetch("https://queue.fal.run/fal-ai/flux/dev/image-to-image", {
            method: "POST",
            headers: {
                "Authorization": `Key ${apiKey}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                image_url: dataUrl,
                prompt: prompt,
                strength: 0.85, // Give it enough freedom to remove text but keep the theme
                image_size: { width: 1240, height: 1754 }, // A4 ratio
                num_inference_steps: 28
            })
        });
        
        const data = await response.json();
        console.log("Response:", data);
        
        // Polling the queue if necessary
        let statusUrl = data.status_url;
        if (statusUrl) {
            let status = 'IN_QUEUE';
            while (status === 'IN_QUEUE' || status === 'IN_PROGRESS') {
                console.log("Polling status...");
                await new Promise(r => setTimeout(r, 2000));
                const statusRes = await fetch(statusUrl, {
                    headers: { "Authorization": `Key ${apiKey}` }
                });
                const statusData = await statusRes.json();
                status = statusData.status;
                if (status === 'COMPLETED') {
                    console.log("Result:", JSON.stringify(statusData, null, 2));
                    break;
                } else if (status === 'FAILED') {
                    console.error("Failed:", statusData);
                    break;
                }
            }
        }
    } catch (e) {
        console.error("Error:", e);
    }
}

run();
