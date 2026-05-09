import requests, time, os, json
from pathlib import Path

FAL_API_KEY = "8e168200-34e5-4598-87ae-ccfb1deee44d:90ce61b3e7b5373d7f168ec74a5ae002"
OUTPUT_DIR  = r"C:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids\backgrounds"
HEADERS     = {"Authorization": "Key " + FAL_API_KEY, "Content-Type": "application/json"}

STYLE_BASE = """3D CGI animation render, Pixar studio quality, subsurface scattering, physically based rendering, volumetric lighting, ray tracing, cinematic depth of field. Children's Islamic storybook full-bleed illustration background. Rich saturated colors, dramatic cinematic lighting. Fully rendered 3D environment.
CRITICAL REQUIREMENT 1: ABSOLUTELY NO TEXT, NO WORDS, NO LETTERS, NO TYPOGRAPHY.
CRITICAL REQUIREMENT 2: ABSOLUTELY NO CHARACTERS, NO PEOPLE, NO CHILDREN, NO ANIMALS, NO ANGELS. PURE EMPTY SCENIC LANDSCAPE BACKGROUND ONLY. IGNORE ANY INSTRUCTIONS IN THE SCENE DESCRIPTION THAT MENTION LIVING BEINGS."""

# (num, key, name_latin, name_indo, line1, line2, pesan, scene)
SURAHS = [
(78, "an_naba", "An-Naba'", "Berita Besar",
"Suatu hari akan ada Hari Kiamat yang sangat besar!",
"Allah menyiapkan balasan sempurna untuk setiap amal kita.",
"Setiap kebaikan yang kamu lakukan, Allah catat!",
"Dramatic split sky at golden dusk. LEFT half: Lush paradise garden with sparkling golden rivers and glowing fruit trees. RIGHT half: Barren rocky grey land. CENTER SKY: Dramatic clouds parting revealing brilliant golden divine light from above. Rich jewel colors, dramatic sky."),

(79, "an_naziat", "An-Nazi'at", "Malaikat-malaikat",
"Ada malaikat-malaikat yang bertugas khusus dari Allah!",
"Mereka bekerja dengan sempurna, taat, tak pernah malas.",
"Malaikat Allah rajin bekerja, kita juga harus rajin!",
"Beautiful cosmic night sky full of stars and nebulas. Colorful galaxies, swirling purple and blue cosmic clouds, golden sparkles. Peaceful magical awe. Deep blue gold ethereal glow."),

(80, "abasa", "Abasa", "Bermuka Masam",
"Semua orang berhak mendapat perhatian yang sama!",
"Orang yang sungguh-sungguh ingin belajar, mulia di sisi Allah.",
"Jangan pernah meremehkan siapapun yang ingin belajar!",
"Warm cozy outdoor scene under a palm tree, golden afternoon light. Open glowing golden book resting on a stand. Warm amber tones, humble and warm atmosphere."),

(81, "at_takwir", "At-Takwir", "Menggulung",
"Bayangkan suatu hari matahari digulung seperti sebuah gulungan!",
"Dunia ini tidak abadi, hanya amal baik yang kita bawa.",
"Dunia ini sementara. Gunakan waktumu untuk kebaikan!",
"Magical cosmic scene. CENTER: Large beautiful sun slowly rolling up like a golden scroll. AROUND: Stars dancing softly, colorful swirling clouds. Magical wondrous fairy tale feel. Vivid purple orange sky dreamlike."),

(82, "al_infitar", "Al-Infitar", "Terbelah",
"Kamu punya dua malaikat penjaga yang selalu menemanimu!",
"Raqib mencatat kebaikan, Atid mencatat kesalahan kita.",
"Ingat! Ada malaikat yang mencatat. Perbanyak kebaikan!",
"Beautiful night sky opening like a curtain being pulled apart. CENTER SKY: Sky splitting gently revealing bright golden light. FOREGROUND: Silhouette of trees below. Deep blue purple sky with golden accents, magical and reassuring."),

(83, "al_mutaffifin", "Al-Mutaffifin", "Orang-orang Curang",
"Pedagang jujur dicintai Allah dan dipercaya semua orang!",
"Tapi pedagang curang akan mendapat balasan dari Allah.",
"Jujur itu kunci! Allah selalu melihat meski tidak ada yang tahu.",
"Colorful marketplace background. Beautiful perfectly balanced golden glowing scale on a table. BACKGROUND: Colorful market stalls, fruits. Disney 3D bright market colors, warm lighting."),

(84, "al_inshiqaq", "Al-Inshiqaq", "Terbelah",
"Suatu hari langit akan terbelah atas perintah Allah!",
"Setiap orang menerima buku catatan amalnya sendiri.",
"Ayo isi buku amal dengan kebaikan sebelum terlambat!",
"Dramatic beautiful twilight sky. CENTER: Large full moon, clouds parting around it. SKY: Cracking open gently like a book being opened with golden light streaming through. Disney 3D deep purple blue sky warm gold accents."),

(85, "al_buruj", "Al-Buruj", "Gugusan Bintang",
"Lihatlah langit malam dengan gugusan bintang yang indah!",
"Allah memuliakan orang yang tetap sabar dalam kebenaran.",
"Tetap kuat dalam kebenaran meski sulit. Allah bersama kita!",
"Magical night sky. Eight bright star clusters forming beautiful geometric constellation patterns, each glowing in different warm colors: gold, amber, rose, connected by soft light lines. Disney 3D deep navy sky glowing starlight, magical curious wonder."),

(86, "at_tariq", "At-Tariq", "Bintang Malam",
"Ada satu bintang yang sangat terang menembus gelapnya malam!",
"At-Tariq si pengetuk malam, simbol kebenaran yang selalu bersinar.",
"Kebenaran akan selalu bersinar seperti bintang di malam gelap.",
"Deep peaceful night. SKY: Very dark blue filled with many small stars. CENTER: ONE extra brilliant piercing star much larger than the rest, glowing intensely with dramatic rays of light shooting outward like a spotlight from heaven. Disney 3D very dark sky contrasting one brilliant light."),

(87, "al_ala", "Al-A'la", "Yang Maha Tinggi",
"Sucikanlah nama Allah Yang Maha Tinggi, pencipta segalanya!",
"Allah yang menumbuhkan tanaman dan mengajarkan ilmu kepada kita.",
"Selalu ingat dan syukuri semua yang Allah berikan!",
"Lush beautiful green meadow and farm. FOREGROUND: Rows of tall green crops growing abundantly from rich earth. SKY: Bright blue fluffy clouds, sun peeking through, rainbow on horizon. Rolling green hills, blooming flowers. Disney 3D vivid greens warm yellows."),

(88, "al_ghashiyah", "Al-Ghashiyah", "Hari Pembalasan",
"Ada dua golongan di Hari Pembalasan yang pasti datang!",
"Yang beramal baik bersinar bahagia, yang lalai akan menyesal.",
"Mulai sekarang isi hari dengan sholat, kebaikan, dan berbagi!",
"Split world illustration. LEFT HALF: Lush paradise garden, crystal clear river, colorful flowers, fruit trees, golden warm light, butterflies. RIGHT HALF: Dry barren rocky desert, cracked earth, grey light. CENTER: Glowing balanced scale dividing two worlds. Disney 3D vivid color contrast."),

(89, "al_fajr", "Al-Fajr", "Fajar",
"Fajar adalah waktu yang sangat istimewa bagi Allah!",
"Ujian datang bukan karena Allah benci, tapi karena Allah sayang.",
"Syukuri semua keadaan. Susah dan senang sama-sama dari Allah!",
"Breathtaking golden dawn. SKY: Deep purple night on left transitioning to brilliant orange pink gold on right, sun just peeking over horizon. BACKGROUND: Ancient stone landscape, palm trees, rolling hills. Disney 3D spectacular gradient sky colors, hopeful new beginning."),

(90, "al_balad", "Al-Balad", "Negeri",
"Allah bersumpah dengan kota Mekah yang sangat mulia!",
"Jalan kebaikan memang mendaki tapi hasilnya sangat mulia.",
"Pilih jalan kebaikan meski berat. Allah bersama orang baik!",
"Warm ancient city neighborhood. BACKGROUND: Colorful ancient Arabian buildings, archways, empty market streets. FOREGROUND: Cobblestone street, potted plants, warm lanterns glowing. Disney 3D warm amber terracotta palette."),

(91, "ash_shams", "Ash-Shams", "Matahari",
"Allah bersumpah dengan matahari, bulan, langit, dan bumi!",
"Beruntunglah orang yang memilih untuk menyucikan jiwanya.",
"Kamu punya pilihan jadi baik atau buruk. Pilihlah kebaikan!",
"Beautiful cosmic scene. CENTER: Large beautiful bright SUN, warm golden rays spreading outward. AROUND: Moon, small twinkling stars. BELOW: Daytime landscape with trees, hills. Gradient sky deep blue to warm orange. Disney 3D very warm golden palette."),

(92, "al_lail", "Al-Lail", "Malam",
"Orang yang rajin memberi dan bertakwa, Allah mudahkan jalannya!",
"Harta paling berharga adalah harta yang kita bagi dengan ikhlas.",
"Jangan pelit! Semakin banyak berbagi, Allah mudahkan hidupmu.",
"Magical nighttime scene. A beautiful glowing donation box resting on a pedestal, radiating golden light. BACKGROUND: Dark blue night sky, soft glowing stars, peaceful neighborhood. Warm lamplight illuminating scene. Disney 3D dark blue contrasted with warm golden glow."),

(93, "ad_duha", "Ad-Duha", "Waktu Duha",
"Allah menurunkan surah ini untuk menghibur Nabi SAW yang sedih!",
"Allah berkata: Kami tidak meninggalkanmu. Allah selalu ada!",
"Saat merasa sedih atau sendiri, Allah tidak pernah meninggalkanmu!",
"Beautiful golden morning. Open window, brilliant morning sun streaming in, curtains billowing. Warm cozy room, plants, soft shadows, a beautiful prayer mat on the floor surrounded by soft golden morning light. Disney 3D warm golden morning light, peace and gratitude."),

(94, "ash_sharh", "Ash-Sharh", "Melapangkan",
"Allah melapangkan dada Nabi dari beban yang berat!",
"Bersama setiap kesulitan pasti ada kemudahan. Allah berjanji!",
"Jangan menyerah! Bersama setiap kesulitan ada DUA kemudahan.",
"Uplifting symbolic scene. BACKGROUND: Heavy grey clouds on left transforming into brilliant sunshine clear blue sky on right. FOREGROUND: Beautiful glowing flowers blooming on the sunny side. Disney 3D dramatic light to dark contrast, relief after hardship, hope."),

(95, "at_tin", "At-Tin", "Buah Tin",
"Manusia diciptakan Allah dengan sebaik-baiknya bentuk!",
"Fisik sempurna, akal berpikir, hati merasakan — semua dari Allah.",
"Kamu diciptakan sempurna oleh Allah. Jaga dengan iman!",
"Lush beautiful garden. LEFT: Large fig tree with big green leaves, plump purple figs hanging abundantly. RIGHT: Ancient olive tree with silver-green leaves, golden olives. CENTER PATH: Empty path winding between trees. Rolling green hills, golden afternoon light. Disney 3D rich lush greens, abundance."),

(96, "al_alaq", "Al-'Alaq", "Segumpal Darah",
"IQRA! Bacalah! Itulah wahyu pertama untuk Nabi Muhammad SAW!",
"Dengan ilmu, manusia bisa menjadi mulia di sisi Allah.",
"Rajin belajar dan membaca adalah perintah Allah langsung!",
"Warm cozy magical learning scene. Beautiful wooden desk with a glowing open book radiating soft light. AROUND: Floating open books, soft glowing golden sparkles drifting upward like magic. Warm study room, bookshelves, soft lamp light. Disney 3D warm amber lighting, joy of learning."),

(97, "al_qadr", "Al-Qadr", "Kemuliaan",
"Malam Lailatul Qadr lebih baik dari seribu bulan!",
"Para malaikat dan Jibril turun ke bumi atas izin Allah.",
"Cari Lailatul Qadr di 10 malam terakhir Ramadan. Jangan lewat!",
"Magical sacred night. SKY: Deep velvety blue, extremely bright full moon, thousands of golden sparkles descending from sky. CENTER: Beautiful white mosque with minarets, windows glowing warm light. Disney 3D deep blue and gold ethereal glow."),

(98, "al_bayyinah", "Al-Bayyinah", "Bukti Nyata",
"Allah mengutus Nabi SAW membawa Al-Quran yang suci!",
"Orang beriman yang beramal sholeh adalah sebaik-baiknya makhluk.",
"Jaga sholat, berbuat baik, bantu sesama. Itulah orang terbaik!",
"Warm learning scene. CENTER: Beautiful glowing scroll on golden pedestal radiating clear bright white light upward. Soft warm light, simple mosque-style arches, greenery. Disney 3D warm golden light."),

(99, "az_zalzalah", "Az-Zalzalah", "Kegoncangan",
"Saat bumi digoncangkan — itulah Hari Kiamat yang pasti datang!",
"Sekecil apapun kebaikanmu, walau seberat atom, Allah catat!",
"Jangan remehkan kebaikan kecil! Senyum dan membantu pun bernilai.",
"Symbolic beautiful earth scene. CENTER: Beautiful Earth globe shaking slightly with tiny golden books and scrolls floating out from ground upward. ABOVE: Large golden scale of justice floating in sky, perfectly balanced and glowing. Blue sky, fluffy clouds, sunlight, peaceful landscape. Disney 3D bright blues and golds."),

(100, "al_adiyat", "Al-'Adiyat", "Kuda-kuda Perang",
"Allah bersumpah dengan kuda-kuda yang berlari sangat kencang!",
"Kuda setia kepada tuannya, kita harus lebih setia kepada Allah.",
"Setia kepada Allah, selalu ingat dan syukuri setiap nikmat-Nya!",
"Majestic desert at golden hour. BACKGROUND: Dramatic orange sunset sky, distant rocky mountains, golden sand dunes. Golden sparkling dust clouds kicking up. Disney 3D warm golden tones, energetic joyful landscape."),

(101, "al_qariah", "Al-Qari'ah", "Hari Kiamat",
"Al-Qari'ah adalah Hari Kiamat yang pasti akan tiba!",
"Semua amal ditimbang. Yang berat kebaikannya akan sangat bahagia.",
"Setiap hari isi timbangan kebaikanmu dengan sholat dan sedekah!",
"Symbolic magical sky scene. CENTER: Giant scale of justice floating in sky, left side heavy and glowing with pile of golden good deeds, right side empty floating up. BACKGROUND: Dramatic colorful sky, pink purple clouds, golden rays. Disney 3D magical floating elements."),

(102, "at_takathur", "At-Takathur", "Bermegah-megahan",
"Manusia sering terlena berlomba-lomba mengumpulkan harta!",
"Semua kemewahan tidak dibawa mati. Hanya amal yang dibawa.",
"Boleh punya banyak, tapi jangan lupa kepada Allah dan sesama!",
"Clear contrast scene. LEFT: Enormous pile of gold, jewels, and luxury items looking heavy and dark. RIGHT: A beautiful glowing simple flower blooming brightly. CENTER: Heart symbol glowing warmly. Disney 3D bright cheerful colors, clear lesson about contentment."),

(103, "al_asr", "Al-'Asr", "Masa",
"Demi masa! Sungguh manusia benar-benar dalam kerugian kecuali...",
"...orang yang beriman, beramal sholeh, dan saling menasihati.",
"Jangan buang waktu! Gunakan setiap menit untuk hal bermanfaat.",
"Beautiful golden afternoon Asr time. BACKGROUND: Golden afternoon sun low in sky, casting long warm shadows over a beautiful peaceful garden. CENTER: Clock showing afternoon time with golden glow. Disney 3D warm golden hour lighting."),

(104, "al_humazah", "Al-Humazah", "Pengumpat",
"Allah tidak menyukai orang yang suka mengejek dan mencela!",
"Yang menghina orang lain akan mendapat balasan dari Allah.",
"Jangan ejek atau hina teman! Bantu, jangan ejek kekurangannya.",
"Beautiful playground scene. LEFT: Dark small storm cloud raining over a patch of withered flowers. RIGHT: Transformed scene, beautiful blooming flowers, bright sunshine above. Disney 3D clear before-after contrast, bright colors."),

(105, "al_fil", "Al-Fil", "Gajah",
"Raja Abrahah membawa pasukan gajah untuk hancurkan Ka'bah!",
"Allah mengirim ribuan burung Ababil yang mengalahkan mereka.",
"Tidak ada kekuatan yang bisa mengalahkan perlindungan Allah!",
"Wide golden desert at colorful pink orange sunset. FAR LEFT: Holy Kaaba, wide black cube with horizontal gold band, white marble base, soft white divine glow. SKY: Hundreds of tiny glowing pebbles falling like rain. Painterly sunset, pink purple orange clouds, golden warm glow."),

(106, "quraish", "Quraish", "Suku Quraisy",
"Suku Quraisy adalah penjaga Ka'bah yang diberi keistimewaan Allah!",
"Mereka berdagang ke Yaman & Syam, selalu aman karena perlindungan Allah.",
"Syukuri setiap nikmat Allah, sekecil apapun!",
"Beautiful trade route at golden hour. BACKGROUND split: LEFT snowy mountain winter landscape, RIGHT lush green summer landscape. CENTER BACKGROUND: ancient city with glowing golden Kaaba visible. Warm divine golden light. Disney Pixar 3D rich warm market colors."),

(107, "al_maun", "Al-Ma'un", "Barang-barang Berguna",
"Sholat yang benar menggerakkan hati untuk peduli sesama!",
"Membantu sesama adalah bagian penting dari ibadah kita.",
"Mulai dari hal kecil: berbagi bekal, meminjamkan pensil!",
"Warm community scene. BACKGROUND: Warm neighborhood street, flowers, golden afternoon light. FOREGROUND: Small everyday items resting on a table glowing with warm light: a cup, a plate, a bowl of soup. Disney 3D warm cozy neighborhood."),

(108, "al_kawthar", "Al-Kautsar", "Nikmat yang Banyak",
"Allah memberi Nabi SAW Al-Kautsar, nikmat yang sangat banyak!",
"Al-Kautsar adalah telaga surga, airnya lebih putih dari susu.",
"Sholat adalah cara kita berterima kasih kepada Allah!",
"Breathtaking paradise river scene. CENTER: Magnificent glowing river of crystal clear water, sparkling golden and silver light, flowing gently across lush green landscape. BANKS: Colorful exotic flowers, fruit trees, butterflies. SKY: Perfect blue, fluffy white clouds, soft golden light everywhere. Disney 3D lush vivid greens, sparkling water effects, paradise."),

(109, "al_kafirun", "Al-Kafirun", "Orang-orang Kafir",
"Katakanlah: Untukmu agamamu, dan untukku agamaku!",
"Seorang Muslim harus teguh dalam iman, namun tetap bersikap damai.",
"Teguh dengan keyakinanmu, tapi tetap bersikap baik dan damai!",
"Peaceful harmonious neighborhood scene. BACKGROUND: Peaceful neighborhood, different colorful buildings side by side, a beautiful glowing mosque on one side, flowers between them, clear blue sky. Disney 3D warm harmonious colors, peace and respect."),

(110, "an_nasr", "An-Nasr", "Pertolongan",
"Pertolongan Allah datang dan kemenangan tiba dengan damai!",
"Nabi SAW menaklukkan Mekah tanpa pertumpahan darah.",
"Saat berhasil, jangan sombong! Semua karena bantuan Allah.",
"Joyful celebration scene. SKY: Hundreds of beautiful glowing flower petals swirling in a spectacular pattern above. CENTER: Golden divine light radiating from above onto a peaceful beautiful city. Disney 3D vibrant celebratory colors, victory through divine help."),

(111, "al_masad", "Al-Masad", "Sabut",
"Harta dan kekuasaan tidak bisa menyelamatkan dari balasan Allah!",
"Gunakanlah semua yang kita punya untuk kebaikan, bukan kejahatan.",
"Yang paling berharga adalah iman dan akhlak yang baik!",
"Two garden paths showing clear consequences. CENTER LEFT: A bright clean beautiful path with flowers blooming, colorful butterflies, warm sunshine above. CENTER RIGHT: Thorny dark neglected path with storm clouds. FOREGROUND: Clear fork in road with two signposts. Disney 3D clear visual contrast."),

(112, "al_ikhlas", "Al-Ikhlas", "Ikhlas",
"Allah itu Satu! Tidak ada yang setara dengan Dia!",
"Surah Al-Ikhlas setara dengan sepertiga Al-Quran seluruhnya!",
"Hafalkan Al-Ikhlas! Kamu sudah memahami inti ajaran Islam.",
"Majestic cosmic symbolic scene. CENTER: Giant glowing golden light radiating in space representing the oneness of Allah. AROUND: Universe expanding, galaxies, stars, planets, nebulas all swirling around the central light in perfect harmony. Deep beautiful space, warm gold and blue tones. Disney 3D cosmic scale, magnificent oneness."),

(113, "al_falaq", "Al-Falaq", "Waktu Subuh",
"Berlindunglah kepada Allah dari kejahatan malam yang gelap!",
"Dari kejahatan sihir dan dari kejahatan orang yang dengki.",
"Baca Al-Falaq setiap pagi dan malam sebagai perisai pelindungmu!",
"Magical dawn protection scene. LEFT HALF: Dark mysterious night with shadowy shapes. RIGHT HALF: Brilliant golden dawn breaking, light rays splitting through darkness, chasing shadows completely away. Background: Deep purple transforming to brilliant orange gold dawn. Disney 3D dramatic light versus dark."),

(114, "an_nas", "An-Nas", "Manusia",
"Berlindunglah kepada Allah dari bisikan jahat setan!",
"Setan selalu berusaha membisikkan pikiran buruk ke dalam dada kita.",
"Baca An-Nas setiap pagi dan malam. Allah pasti melindungimu!",
"Warm divine protection scene. CENTER: Beautiful transparent golden protective bubble like a gentle force field of light resting on a peaceful meadow. OUTSIDE BUBBLE: Tiny dark shadows bouncing off harmlessly. ABOVE: Rays of golden divine light from sky reinforcing the bubble. Disney 3D warm protective golden glow."),
]

def build_prompt(scene):
    return f"{STYLE_BASE}\n\nSCENE: {scene}"

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
        try:
            r = requests.get(job["status_url"], headers=HEADERS, timeout=15)
            if r.status_code != 200: continue
            d = r.json()
            status = d.get("status", "?")
            print(f"      [{elapsed}s] {status}")
            if status == "COMPLETED":
                rr = requests.get(job["response_url"], headers=HEADERS, timeout=30)
                rr.raise_for_status()
                images = rr.json().get("images", [])
                if images: return images[0]["url"]
                raise Exception("No images in response")
            elif status in ("FAILED", "failed", "error"):
                raise Exception(f"Job failed: {d}")
        except requests.exceptions.ReadTimeout:
            pass
        if elapsed > timeout:
            raise Exception(f"Timeout after {timeout}s")

def download(url, path):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    with open(path, "wb") as f:
        f.write(r.content)

def main():
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    total = len(SURAHS)

    print("=" * 60)
    print("  JUZ AMMA V2 BATCH - CLEAN BACKGROUNDS (NO TEXT, NO CHARACTERS)")
    print(f"  Model: Seedream v4.5")
    print(f"  Output: {OUTPUT_DIR}")
    print("=" * 60)

    for idx, (num, key, name_latin, name_indo, line1, line2, pesan, scene) in enumerate(SURAHS):
        label = f"[{idx+1:02d}/{total}] Surah {num} {name_latin}"
        img_path = os.path.join(OUTPUT_DIR, f"{num:03d}_{key}_bg.png")

        if os.path.exists(img_path):
            print(f"  OK {label} - skip")
            continue

        print(f"\n  GENERATING: {label}")
        try:
            prompt = build_prompt(scene)
            job = submit_image(prompt)
            print(f"      Polling...")
            img_url = poll_image(job)
            download(img_url, img_path)
            print(f"      Saved -> {img_path}")
            time.sleep(2)
        except Exception as e:
            print(f"      ERROR: {e}")
            time.sleep(3)

    print("\n" + "=" * 60)
    print("  FINISHED!")
    print("=" * 60)

if __name__ == "__main__":
    main()
