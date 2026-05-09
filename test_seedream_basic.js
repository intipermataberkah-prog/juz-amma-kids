const apiKey = '8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002';
const url = "https://queue.fal.run/fal-ai/bytedance/seedream/v5/lite";

async function run() {
    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Authorization": `Key ${apiKey}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                prompt: "A beautiful space background, deep galaxy, stars. Empty poster background. NO TEXT.",
                image_size: "portrait_4_3"
            })
        });
        
        const data = await response.json();
        console.log("Submit:", data);
        
        let statusUrl = data.status_url;
        let responseUrl = data.response_url;

        if (statusUrl) {
            let status = 'IN_QUEUE';
            while (status === 'IN_QUEUE' || status === 'IN_PROGRESS') {
                await new Promise(r => setTimeout(r, 2000));
                const statusRes = await fetch(statusUrl, { headers: { "Authorization": `Key ${apiKey}` } });
                const statusData = await statusRes.json();
                status = statusData.status;
                if (status === 'FAILED') {
                    console.error("FAILED DATA:", statusData);
                }
            }

            if (status === 'COMPLETED') {
                const finalRes = await fetch(responseUrl, { headers: { "Authorization": `Key ${apiKey}` } });
                const finalData = await finalRes.json();
                console.log("FINAL:", finalData);
            }
        }
    } catch(e) { console.error(e); }
}

run();
