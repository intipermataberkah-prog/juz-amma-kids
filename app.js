const btnLoadData = document.getElementById('btnLoadData');
const btnPrint = document.getElementById('btnPrint');
const loadingStatus = document.getElementById('loadingStatus');
const container = document.getElementById('juzAmmaContainer');

let localContentData = null;

async function fetchWithRetry(url, retries = 3) {
    for (let i = 0; i < retries; i++) {
        try {
            const res = await fetch(url);
            if (!res.ok) throw new Error(`HTTP ${res.status}`);
            return await res.json();
        } catch (err) {
            if (i === retries - 1) throw err;
            await new Promise(r => setTimeout(r, 1000 * (i + 1)));
        }
    }
}

// ===== SCENE MAP: ayat → background scene =====
const SCENE_MAP = {
    78: [
        { from: 1,  to: 5,  scene: 'bg_sky.png' },
        { from: 6,  to: 16, scene: 'bg_nature.png' },
        { from: 17, to: 20, scene: 'bg_night.png' },
        { from: 21, to: 30, scene: 'bg_sky.png' },
        { from: 31, to: 36, scene: 'bg_nature.png' },
        { from: 37, to: 40, scene: 'bg_night.png' },
    ]
};

function getSceneForAyat(surahNum, ayatNum) {
    const map = SCENE_MAP[surahNum];
    if (!map) return 'bg_sky.png';
    for (const g of map) {
        if (ayatNum >= g.from && ayatNum <= g.to) return g.scene;
    }
    return 'bg_sky.png';
}

// ===== OVERFLOW =====
function isOverflowing(contentDiv) {
    const last = contentDiv.lastElementChild;
    if (!last) return false;
    
    // Instead of checking contentDiv (which might stretch due to flexbox),
    // we check the parent .page which has a strict fixed height of 303mm.
    const page = contentDiv.closest('.page');
    if (!page) return false;

    const pageRect = page.getBoundingClientRect();
    
    // page has padding: 3mm (bleed). contentDiv has padding-bottom: 10mm.
    // The total safe bottom boundary is inside these paddings.
    // Let's just use the absolute page bottom minus bleed minus bottom padding minus an 8px buffer.
    // bleed (3mm) ~ 11.3px, padBot (10mm) ~ 37.8px. Total ~ 49px + 8px buffer = 57px from the very bottom.
    const maxBot = pageRect.bottom - 57;
    
    return last.getBoundingClientRect().bottom > maxBot;
}

// ===== HELPERS =====
function el(tag, className) {
    const e = document.createElement(tag);
    e.className = className;
    return e;
}

let pageNum = 1;
let currentAyatNum = 1;

let decorIndex = 0;
const decors = [
    { src: 'decor_vine_left.png', class: 'decor-vine-left' },
    { src: 'decor_vine_right.png', class: 'decor-vine-right' },
    { src: 'decor_quran_glow.png', class: 'decor-quran-glow' },
    { src: 'decor_stars_cluster.png', class: 'decor-stars-cluster' },
    { src: 'naba_pointing.png', class: 'naba-pointing' },
    { src: 'character_naba.png', class: 'ayat-decor decor-item-character_naba' },
    { src: 'lantern.png', class: 'ayat-decor decor-item-lantern' },
    { src: 'telescope.png', class: 'ayat-decor decor-item-telescope' }
];

// ===== PAGE FACTORY (efficient: decorations embedded in page) =====
function createContentPage(surahNum) {
    const page = document.createElement('div');
    page.className = 'page';

    // 1. Layer 1: Thematic Full-Bleed Watercolor Background
    const sceneSrc = getSceneForAyat(surahNum || 78, currentAyatNum);
    const bg = document.createElement('div');
    bg.className = 'page-layer-watercolor';
    bg.innerHTML = `<img src="assets/an_naba/${sceneSrc}" alt="">`;
    page.appendChild(bg);

    // 2. Layer 4: Mascot Peek-a-boo (Randomly on some pages)
    if (pageNum % 3 === 0) {
        const mascot = document.createElement('img');
        mascot.className = 'mascot-peek mascot-peek-bottom-left';
        mascot.src = 'assets/an_naba/naba_pointing.png';
        page.appendChild(mascot);
    } else if (pageNum % 5 === 0) {
        const mascot = document.createElement('img');
        mascot.className = 'mascot-peek mascot-peek-top-right';
        mascot.src = 'assets/an_naba/character_naba.png';
        page.appendChild(mascot);
    } else if (pageNum > 2 && pageNum % 2 !== 0 && Math.random() > 0.5) {
        const mascot = document.createElement('img');
        mascot.className = 'mascot-peek mascot-peek-bottom-right';
        mascot.src = 'assets/an_naba/naba_sitting.png';
        page.appendChild(mascot);
    }

    // 3. Content area (full page minus padding)
    const content = document.createElement('div');
    content.className = 'page-content';
    page.appendChild(content);

    container.appendChild(page);
    pageNum++;
    return { page, content };
}

function addPageNum(page) {
    const pn = document.createElement('div');
    pn.className = 'page-number';
    pn.textContent = pageNum - 1;
    page.appendChild(pn);
}

// ===== FULL-BLEED PAGE =====
function buildFullbleedPage(imgSrc, overlayClass, contentHTML) {
    const page = document.createElement('div');
    page.className = 'page fullbleed-page';

    const bg = document.createElement('div');
    bg.className = 'fullbleed-bg';
    bg.innerHTML = `<img src="${imgSrc}" alt="">`;
    page.appendChild(bg);

    const overlay = document.createElement('div');
    overlay.className = 'fullbleed-overlay';
    page.appendChild(overlay);

    const content = document.createElement('div');
    content.className = 'fullbleed-content';
    content.innerHTML = contentHTML;
    page.appendChild(content);

    return page;
}

// ===== COVER =====
function buildCoverPage() {
    const page = buildFullbleedPage(
        'assets/an_naba/cover_scene.png',
        'cover-overlay',
        `<h1 class="cover-title">Juz 'Amma</h1>
         <h2 class="cover-subtitle">Kumpulan Surat Pendek untuk Anak Muslim</h2>
         <p class="cover-footer">Storybook Edition · Lengkap dengan Terjemahan, Tafsir & Tajwid</p>`
    );
    page.classList.add('cover-page');

    const ch = document.createElement('img');
    ch.className = 'character-float';
    ch.src = 'assets/an_naba/character_naba.png';
    ch.alt = 'Naba';
    page.appendChild(ch);

    return page;
}

// ===== SURAH TITLE =====
function buildSurahTitlePage(apiData, surahNum) {
    const page = buildFullbleedPage(
        'assets/an_naba/title_scene.png',
        'surah-overlay',
        `<div class="surah-title-badge">Surah ke-${surahNum} · Juz 30</div>
         <div class="surah-title-arabic">${apiData.nama}</div>
         <div class="surah-title-latin">Surah ${apiData.namaLatin}</div>
         <div class="surah-title-meaning">"${apiData.arti}"</div>
         <div class="surah-meta-row">
             <span class="surah-meta-chip">📍 ${apiData.tempatTurun}</span>
             <span class="surah-meta-chip">📖 ${apiData.jumlahAyat} Ayat</span>
         </div>`
    );
    page.classList.add('surah-title-page');

    const ch = document.createElement('img');
    ch.className = 'character-float';
    ch.src = 'assets/an_naba/character_naba.png';
    ch.alt = 'Naba';
    page.appendChild(ch);

    return page;
}

// ===== CONTENT BUILDERS =====
function buildBismillah() {
    const div = document.createElement('div');
    div.className = 'bismillah-section';
    div.innerHTML = `
        <div class="bismillah-line">
            <span class="bismillah-star">✦</span>
            <span class="bismillah-arabic">بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ</span>
            <span class="bismillah-star">✦</span>
        </div>
        <span class="bismillah-latin">Bismillāhir-raḥmānir-raḥīm</span>
    `;
    return div;
}

function buildAyatBlock(ayat) {
    const div = document.createElement('div');
    div.className = 'ayat-block';
    div.innerHTML = `
        <div class="verse-num">${ayat.nomorAyat}</div>
        <div class="ayat-arabic">${ayat.teksArab}</div>
        <div class="ayat-latin">${ayat.teksLatin}</div>
        <div class="ayat-translation">${ayat.teksIndonesia}</div>
    `;
    return div;
}

  // ===== DECORATIVE SEPARATOR =====
function buildAyatSeparator() {
    const div = document.createElement('div');
    div.className = 'ayat-separator';
    div.innerHTML = `<img src="assets/an_naba/divider_ornate.png" alt="">`;
    return div;
}

function buildContinuation(namaLatin) {
    const div = document.createElement('div');
    div.className = 'continuation-header';
    div.textContent = `Lanjutan Surah ${namaLatin}`;
    return div;
}

function buildTafsirCard(apiData, localData) {
    const div = document.createElement('div');
    div.className = 'info-card tafsir';
    div.innerHTML = `
        <span class="info-card-icon">🌿</span>
        <div class="info-card-title">Tafsir for Kids</div>
        <div class="tafsir-grid">
            <div class="tafsir-col">
                <h4>Tentang Surah ${apiData.namaLatin}</h4>
                <p>${localData.tafsir_qna}</p>
            </div>
            <div class="tafsir-col">
                <h4>Pesan Penting</h4>
                <p>${localData.pesan_penting}</p>
            </div>
        </div>
    `;
    return div;
}

function buildAsbabunCard(localData) {
    const div = document.createElement('div');
    div.className = 'info-card asbabun';
    div.innerHTML = `
        <span class="info-card-icon">📜</span>
        <div class="info-card-title">Asbabun Nuzul</div>
        <div class="info-card-body">${localData.asbabun_nuzul}</div>
    `;
    return div;
}

function buildTajwidCard(localData) {
    let html = '';
    if (localData.tajwid && localData.tajwid.length > 0) {
        localData.tajwid.forEach(t => {
            const parts = t.contoh.split(/\s*\(|\)\s*/);
            html += `
                <div class="tajwid-item">
                    <div class="tajwid-left">
                        <span class="tajwid-name">${t.hukum}</span>
                        <span class="tajwid-desc">${t.penjelasan}</span>
                    </div>
                    <div class="tajwid-right">
                        <span class="tajwid-example">${parts[0] || ''}</span>
                        <span class="tajwid-example-latin">${parts[1] || ''}</span>
                    </div>
                </div>`;
        });
    }
    const div = document.createElement('div');
    div.className = 'info-card tajwid-card';
    div.innerHTML = `
        <span class="info-card-icon">🔊</span>
        <div class="info-card-title">Hukum Bacaan Tajwid</div>
        <div class="tajwid-list">${html}</div>
    `;
    return div;
}


// ===== RENDER =====
function renderSurah(apiData, localData, surahNum) {
    if (!apiData || !localData) return;

    // 1. Surah title (full-bleed)
    const titlePage = buildSurahTitlePage(apiData, surahNum);
    addPageNum(titlePage);
    pageNum++;
    container.appendChild(titlePage);

    // 2. Content items
    const items = [];
    items.push({ el: buildBismillah(), type: 'bismillah', ayatNum: 0 });

    // Thematic Story Groups for An-Naba
    const themes = [
        { start: 1, end: 5, image: null }, // The Great News
        { start: 6, end: 8, image: 'naba_mountains.png', caption: 'Gunung diciptakan sebagai pasak bumi.' }, 
        { start: 9, end: 11, image: 'naba_night_day.png', caption: 'Malam untuk istirahat, siang untuk mencari rezeki.' }, 
        { start: 12, end: 16, image: 'naba_rain_garden.png', caption: 'Air hujan menumbuhkan kebun-kebun yang lebat.' }, 
        { start: 17, end: 30, image: null }, // Judgment Day (Serious, no decor)
        { start: 31, end: 36, image: 'naba_paradise.png', caption: 'Kemenangan dan kebun-kebun surga bagi yang bertakwa.' }, 
        { start: 37, end: 40, image: null } // Conclusion
    ];

    let alignLeft = true;

    themes.forEach(theme => {
        const groupEl = document.createElement('div');
        let groupClasses = ['story-group'];
        
        if (theme.image) {
            groupClasses.push(alignLeft ? 'align-left' : 'align-right');
            alignLeft = !alignLeft; // Toggle for zig-zag
        }
        groupEl.className = groupClasses.join(' ');

        // Add Illustration FIRST (must come before verses for float wrapping)
        if (theme.image) {
            const illEl = document.createElement('div');
            illEl.className = 'story-illustration';
            let illHtml = `<img src="assets/an_naba/${theme.image}" alt="">`;
            if (theme.caption) {
                illHtml += `<div class="story-caption">${theme.caption}</div>`;
            }
            illEl.innerHTML = illHtml;
            groupEl.appendChild(illEl);
        }

        // Add verses directly to the group (no wrapper) so they wrap around the float
        for (let i = theme.start; i <= theme.end; i++) {
            const ayat = apiData.ayat.find(a => a.nomorAyat === i);
            if (ayat) groupEl.appendChild(buildAyatBlock(ayat));
        }

        items.push({ el: groupEl, type: 'group', ayatNum: theme.end });
        
        // Add a separator after large text-only groups if needed, but zig-zag is usually enough
        if (!theme.image && theme.end !== 40) {
            items.push({ el: buildAyatSeparator(), type: 'sep', ayatNum: theme.end });
        }
    });

    items.push({ el: buildTafsirCard(apiData, localData), type: 'info', ayatNum: 40 });
    items.push({ el: buildAsbabunCard(localData), type: 'info', ayatNum: 40 });
    items.push({ el: buildTajwidCard(localData), type: 'info', ayatNum: 40 });

    // 3. Paginate — with group-splitting for oversized groups
    currentAyatNum = 1;
    let { page, content } = createContentPage(surahNum);

    for (let i = 0; i < items.length; i++) {
        const item = items[i];
        if (item.ayatNum > 0) currentAyatNum = item.ayatNum;

        content.appendChild(item.el);

        if (!isOverflowing(content)) continue;

        // Overflows current page
        content.removeChild(item.el);

        if (item.type === 'group') {
            // Try to chunk it on the CURRENT page to fill empty space
            const originalChildren = Array.from(item.el.children);
            let activeGroup = document.createElement('div');
            activeGroup.className = item.el.className;
            content.appendChild(activeGroup);

            let deferredChildren = [];

            for (let c = 0; c < originalChildren.length; c++) {
                const child = originalChildren[c];
                activeGroup.appendChild(child);

                if (!isOverflowing(content)) {
                    continue;
                }

                // Overflow happened with this child!
                activeGroup.removeChild(child);

                const isPageEmpty = (content.children.length === 0) || 
                                    (content.children.length === 1 && content.children[0] === activeGroup && activeGroup.children.length === 0) ||
                                    (content.children.length === 2 && content.children[0].classList.contains('continuation-header') && content.children[1] === activeGroup && activeGroup.children.length === 0);

                if (isPageEmpty && deferredChildren.length === 0) {
                    activeGroup.appendChild(child);
                    continue;
                }

                if (child.classList.contains('story-illustration')) {
                    deferredChildren.push(child);
                    continue;
                }

                // Break page
                if (content.children.length === 0 || 
                   (content.children.length === 1 && content.children[0].children.length === 0) ||
                   (content.children.length === 2 && content.children[0].classList.contains('continuation-header') && content.children[1].children.length === 0)) {
                    container.removeChild(page);
                } else {
                    addPageNum(page);
                }

                ({ page, content } = createContentPage(surahNum));
                content.appendChild(buildContinuation(apiData.namaLatin));

                activeGroup = document.createElement('div');
                activeGroup.className = item.el.className;
                content.appendChild(activeGroup);

                deferredChildren.forEach(defChild => {
                    activeGroup.appendChild(defChild);
                });
                deferredChildren = [];

                activeGroup.appendChild(child);
            }

            if (deferredChildren.length > 0) {
                if (content.children.length === 0 || 
                   (content.children.length === 1 && content.children[0].children.length === 0) ||
                   (content.children.length === 2 && content.children[0].classList.contains('continuation-header') && content.children[1].children.length === 0)) {
                    container.removeChild(page);
                } else {
                    addPageNum(page);
                }

                ({ page, content } = createContentPage(surahNum));
                content.appendChild(buildContinuation(apiData.namaLatin));

                activeGroup = document.createElement('div');
                activeGroup.className = item.el.className;
                content.appendChild(activeGroup);

                deferredChildren.forEach(defChild => {
                    activeGroup.appendChild(defChild);
                });
            }
            
            // Clean up empty activeGroups
            if (activeGroup.children.length === 0) {
                content.removeChild(activeGroup);
                const headers = content.querySelectorAll('.continuation-header');
                if (headers.length > 0 && content.children.length === headers.length) {
                    headers.forEach(h => content.removeChild(h));
                }
            }
        } else {
            // Not a group. Move to next page.
            if (content.children.length === 0 || (content.children.length === 1 && content.children[0].children.length === 0)) {
                container.removeChild(page);
            } else {
                addPageNum(page);
            }

            ({ page, content } = createContentPage(surahNum));
            
            if (item.type === 'info') {
                content.appendChild(buildContinuation(apiData.namaLatin));
            }

            content.appendChild(item.el);

            // If it STILL overflows even on a fresh page
            if (isOverflowing(content)) {
                content.removeChild(item.el);

                const contHeader = content.querySelector('.continuation-header');
                if (contHeader) content.removeChild(contHeader);

                const originalChildren = Array.from(item.el.children);
                let activeGroup = document.createElement('div');
                activeGroup.className = item.el.className;
                content.appendChild(activeGroup);

                for (let c = 0; c < originalChildren.length; c++) {
                    const child = originalChildren[c];
                    activeGroup.appendChild(child);

                    if (!isOverflowing(content)) {
                        continue;
                    }

                    activeGroup.removeChild(child);

                    if (activeGroup.children.length === 0) {
                        activeGroup.appendChild(child);
                    }

                    if (content.children.length === 0 || (content.children.length === 1 && content.children[0].children.length === 0)) {
                        container.removeChild(page);
                    } else {
                        addPageNum(page);
                    }

                    ({ page, content } = createContentPage(surahNum));
                    content.appendChild(buildContinuation(apiData.namaLatin));

                    activeGroup = document.createElement('div');
                    activeGroup.className = item.el.className;
                    content.appendChild(activeGroup);

                    if (!child.parentNode) {
                        activeGroup.appendChild(child);
                    }
                }
            }
        }
    }

    // Add space filler if there is room on the last page
    const spaceFiller = document.createElement('div');
    spaceFiller.className = 'space-filler';
    spaceFiller.innerHTML = `<img src="assets/an_naba/naba_sitting.png" alt="Naba sitting">`;
    content.appendChild(spaceFiller);

    // Add page number to the last content page
    addPageNum(page);
}

// ===== FRONT MATTER PAGES =====
function buildCopyrightPage() {
    const page = document.createElement('div');
    page.className = 'page front-matter-page';
    page.innerHTML = `
        <div class="page-content" style="justify-content: center; padding: 20mm 18mm;">
            <div style="text-align: center; margin-bottom: 24px;">
                <div style="font-family: 'Baloo 2', sans-serif; font-size: 1.6rem; font-weight: 800; color: var(--naba-deep);">
                    Juz 'Amma &mdash; Storybook Edition
                </div>
                <div style="font-size: 0.85rem; color: var(--naba-text-light); margin-top: 4px;">
                    Kumpulan Surat Pendek untuk Anak Muslim
                </div>
            </div>
            <div style="text-align: center; font-size: 0.75rem; color: var(--naba-text); line-height: 2.0;">
                <strong>Penerbit:</strong> PT Inti Permata Berkah<br>
                <strong>Penulis & Desainer:</strong> Tim Kreatif Permata Kids<br>
                <strong>Ilustrasi:</strong> AI-Generated (Imagen 4)<br>
                <strong>Editor:</strong> Lazuardi Fikhirudin Leonard<br><br>
                <strong>Cetakan Pertama:</strong> 2026<br>
                <strong>ISBN:</strong> 978-xxx-xxxx-xx-x<br><br>
                Hak cipta dilindungi undang-undang.<br>
                Dilarang memperbanyak sebagian atau seluruh isi buku<br>
                tanpa izin tertulis dari penerbit.<br><br>
                <em>Dicetak oleh: Heidelberg SM 74</em><br>
                <em>Ukuran: 21 x 29,7 cm (A4)</em>
            </div>
        </div>`;
    pageNum++;
    return page;
}

function buildForewordPage() {
    const page = document.createElement('div');
    page.className = 'page front-matter-page';
    page.innerHTML = `
        <div class="page-content" style="padding: 18mm 18mm;">
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="font-family: 'Baloo 2', sans-serif; font-size: 1.4rem; font-weight: 800; color: var(--naba-deep);">
                    Kata Pengantar
                </div>
                <div style="width: 60px; height: 3px; background: var(--naba-gold); margin: 8px auto;"></div>
            </div>
            <div style="font-size: 0.85rem; color: var(--naba-text); line-height: 1.8; text-align: justify;">
                <p style="margin-bottom: 12px;">
                    <em>Assalamu'alaikum Warahmatullahi Wabarakatuh,</em>
                </p>
                <p style="margin-bottom: 12px;">
                    Alhamdulillah, segala puji bagi Allah SWT yang telah memberikan kita nikmat iman dan kesempatan
                    untuk mendekatkan anak-anak kita pada Al-Qur'an. Buku <strong>"Juz 'Amma &mdash; Storybook Edition"</strong>
                    ini hadir sebagai media pembelajaran yang menggabungkan keindahan visual dengan konten Islami yang mendalam.
                </p>
                <p style="margin-bottom: 12px;">
                    Setiap surah dalam Juz 'Amma disajikan dengan ilustrasi tematik yang menghidupkan makna ayat-ayatnya,
                    dilengkapi dengan terjemahan, tafsir ringkas, dan panduan tajwid dasar. Kami berharap buku ini
                    tidak hanya menjadi bahan bacaan, tetapi juga menjadi jendela bagi anak-anak untuk memahami
                    kebesaran Allah melalui ciptaan-Nya.
                </p>
                <p style="margin-bottom: 12px;">
                    Semoga buku ini menjadi amal jariyah bagi semua pihak yang terlibat dalam pembuatannya,
                    dan menjadi cahaya bagi generasi penerus umat Islam.
                </p>
                <p style="margin-bottom: 12px;">
                    <em>Wassalamu'alaikum Warahmatullahi Wabarakatuh,</em>
                </p>
                <p style="text-align: right; margin-top: 20px;">
                    <strong>Tim Permata Kids</strong><br>
                    <em>Jakarta, 2026</em>
                </p>
            </div>
        </div>`;
    pageNum++;
    return page;
}

function buildTableOfContentsPage() {
    const page = document.createElement('div');
    page.className = 'page front-matter-page';

    const surahs = [
        { num: 78, name: "An-Naba'", arabic: "النبأ", meaning: "Berita Besar" },
        { num: 79, name: "An-Nazi'at", arabic: "النازعات", meaning: "Malaikat Pencabut" },
        { num: 80, name: "'Abasa", arabic: "عبس", meaning: "Bermuka Masam" },
        { num: 81, name: "At-Takwir", arabic: "التكوير", meaning: "Menggulung" },
        { num: 82, name: "Al-Infitar", arabic: "الانفطار", meaning: "Terbelah" },
        { num: 83, name: "Al-Mutaffifin", arabic: "المطففين", meaning: "Orang Curang" },
        { num: 84, name: "Al-Insyiqaq", arabic: "الانشقاق", meaning: "Terbelah" },
        { num: 85, name: "Al-Buruj", arabic: "البروج", meaning: "Gugusan Bintang" },
        { num: 86, name: "At-Tariq", arabic: "الطارق", meaning: "Yang Datang di Malam Hari" },
        { num: 87, name: "Al-A'la", arabic: "الأعلى", meaning: "Yang Paling Tinggi" },
        { num: 88, name: "Al-Gasyiyah", arabic: "الغاشية", meaning: "Hari Pembalasan" },
        { num: 89, name: "Al-Fajr", arabic: "الفجر", meaning: "Fajar" },
        { num: 90, name: "Al-Balad", arabic: "البلد", meaning: "Negeri" },
        { num: 91, name: "Asy-Syams", arabic: "الشمس", meaning: "Matahari" },
        { num: 92, name: "Al-Lail", arabic: "الليل", meaning: "Malam" },
        { num: 93, name: "Ad-Duha", arabic: "الضحى", meaning: "Waktu Duha" },
        { num: 94, name: "Asy-Syarh", arabic: "الشرح", meaning: "Lapang" },
        { num: 95, name: "At-Tin", arabic: "التين", meaning: "Buah Tin" },
        { num: 96, name: "Al-'Alaq", arabic: "العلق", meaning: "Segumpal Darah" },
        { num: 97, name: "Al-Qadr", arabic: "القدر", meaning: "Kemuliaan" },
        { num: 98, name: "Al-Bayyinah", arabic: "البينة", meaning: "Bukti Nyata" },
        { num: 99, name: "Az-Zalzalah", arabic: "الزلزلة", meaning: "Guncangan" },
        { num: 100, name: "Al-'Adiyat", arabic: "العاديات", meaning: "Kuda Berlari" },
        { num: 101, name: "Al-Qari'ah", arabic: "القارعة", meaning: "Hari Kiamat" },
        { num: 102, name: "At-Takasur", arabic: "التكاثر", meaning: "Bermegah-megahan" },
        { num: 103, name: "Al-'Asr", arabic: "العصر", meaning: "Masa" },
        { num: 104, name: "Al-Humazah", arabic: "الهمزة", meaning: "Pengumpat" },
        { num: 105, name: "Al-Fil", arabic: "الفيل", meaning: "Gajah" },
        { num: 106, name: "Quraisy", arabic: "قريش", meaning: "Suku Quraisy" },
        { num: 107, name: "Al-Ma'un", arabic: "الماعون", meaning: "Barang Berguna" },
        { num: 108, name: "Al-Kausar", arabic: "الكوثر", meaning: "Nikmat Berlimpah" },
        { num: 109, name: "Al-Kafirun", arabic: "الكافرون", meaning: "Orang Kafir" },
        { num: 110, name: "An-Nasr", arabic: "النصر", meaning: "Pertolongan" },
        { num: 111, name: "Al-Lahab", arabic: "المسد", meaning: "Gejolak Api" },
        { num: 112, name: "Al-Ikhlas", arabic: "الإخلاص", meaning: "Ikhlas" },
        { num: 113, name: "Al-Falaq", arabic: "الفلق", meaning: "Waktu Subuh" },
        { num: 114, name: "An-Nas", arabic: "الناس", meaning: "Manusia" },
    ];

    let rows = surahs.map(s =>
        `<tr>
            <td style="width: 30px; font-weight: 800; color: var(--naba-gold-dark);">${s.num}</td>
            <td style="font-weight: 700;">${s.name}</td>
            <td style="font-family: 'Amiri', serif; font-size: 1.1rem; text-align: right; direction: rtl;">${s.arabic}</td>
            <td style="color: var(--naba-text-light); font-style: italic;">${s.meaning}</td>
        </tr>`
    ).join('');

    page.innerHTML = `
        <div class="page-content" style="padding: 15mm 14mm;">
            <div style="text-align: center; margin-bottom: 14px;">
                <div style="font-family: 'Baloo 2', sans-serif; font-size: 1.4rem; font-weight: 800; color: var(--naba-deep);">
                    Daftar Surah
                </div>
                <div style="width: 60px; height: 3px; background: var(--naba-gold); margin: 8px auto;"></div>
            </div>
            <table style="width: 100%; border-collapse: collapse; font-size: 0.7rem; line-height: 1.9;">
                ${rows}
            </table>
        </div>`;
    pageNum++;
    return page;
}

function buildHowToUsePage() {
    const page = document.createElement('div');
    page.className = 'page front-matter-page';
    page.innerHTML = `
        <div class="page-content" style="padding: 18mm 18mm;">
            <div style="text-align: center; margin-bottom: 20px;">
                <div style="font-family: 'Baloo 2', sans-serif; font-size: 1.4rem; font-weight: 800; color: var(--naba-deep);">
                    Cara Menggunakan Buku Ini
                </div>
                <div style="width: 60px; height: 3px; background: var(--naba-gold); margin: 8px auto;"></div>
            </div>
            <div style="font-size: 0.85rem; color: var(--naba-text); line-height: 1.8;">
                <div style="margin-bottom: 16px; padding: 12px 16px; background: rgba(61,170,109,0.08); border-radius: 12px; border-left: 4px solid var(--naba-green);">
                    <strong style="color: var(--naba-green); font-size: 0.9rem;">1. Baca Bersama</strong><br>
                    Bacakan ayat Arab beserta terjemahannya bersama anak. Gunakan ilustrasi tematik untuk menjelaskan makna ayat secara visual.
                </div>
                <div style="margin-bottom: 16px; padding: 12px 16px; background: rgba(58,107,197,0.08); border-radius: 12px; border-left: 4px solid var(--naba-sky);">
                    <strong style="color: var(--naba-sky); font-size: 0.9rem;">2. Pahami Tafsir</strong><br>
                    Setiap surah dilengkapi kartu tafsir yang menjelaskan konteks dan hikmah. Ajak anak berdiskusi tentang pelajaran yang bisa diambil.
                </div>
                <div style="margin-bottom: 16px; padding: 12px 16px; background: rgba(123,104,174,0.08); border-radius: 12px; border-left: 4px solid var(--naba-purple);">
                    <strong style="color: var(--naba-purple); font-size: 0.9rem;">3. Belajar Tajwid</strong><br>
                    Kartu tajwid menunjukkan contoh hukum bacaan pada ayat-ayat tertentu. Latih anak membaca dengan benar melalui contoh yang diberikan.
                </div>
                <div style="margin-bottom: 16px; padding: 12px 16px; background: rgba(232,139,165,0.08); border-radius: 12px; border-left: 4px solid var(--naba-rose);">
                    <strong style="color: var(--naba-rose); font-size: 0.9rem;">4. Amati Ilustrasi</strong><br>
                    Setiap kelompok ayat memiliki ilustrasi tematik. Ajak anak mengamati dan menghubungkan gambar dengan makna ayat. Ini membantu daya ingat!
                </div>
                <div style="padding: 12px 16px; background: rgba(244,162,97,0.08); border-radius: 12px; border-left: 4px solid var(--naba-orange);">
                    <strong style="color: var(--naba-orange); font-size: 0.9rem;">5. Hafalan Bertahap</strong><br>
                    Mulai dari surah-surah pendek di akhir Juz 'Amma, lalu maju ke surah yang lebih panjang. Konsistensi lebih penting dari kecepatan!
                </div>
            </div>
        </div>`;
    pageNum++;
    return page;
}

// ===== PAD TO 16-PAGE MULTIPLE (for offset imposition) =====
function padToMultipleOf16() {
    const allPages = container.querySelectorAll('.page');
    const totalPages = allPages.length;
    const remainder = totalPages % 16;
    if (remainder === 0) return;
    const padCount = 16 - remainder;
    for (let i = 0; i < padCount; i++) {
        const blank = document.createElement('div');
        blank.className = 'page front-matter-page';
        blank.innerHTML = `<div class="page-content" style="justify-content: center; align-items: center; opacity: 0.15;">
            <div style="text-align: center;">
                <div style="font-family: 'Amiri', serif; font-size: 3rem; color: var(--naba-deep);">&#65010;</div>
            </div>
        </div>`;
        container.appendChild(blank);
    }
}

// ===== LOAD =====
async function loadJuzAmma() {
    try {
        btnLoadData.disabled = true;
        loadingStatus.textContent = "Memuat database lokal...";
        if (typeof juzAmmaData === 'undefined') throw new Error("Database lokal tidak ditemukan.");
        localContentData = juzAmmaData;

        loadingStatus.textContent = "Menunggu font dimuat...";
        await document.fonts.ready;

        // Cover
        container.appendChild(buildCoverPage());

        // Front Matter
        container.appendChild(buildCopyrightPage());
        container.appendChild(buildForewordPage());
        container.appendChild(buildTableOfContentsPage());
        container.appendChild(buildHowToUsePage());

        loadingStatus.textContent = "Menunggu gambar dimuat...";
        const imagesToLoad = [
            'assets/an_naba/naba_mountains.png',
            'assets/an_naba/naba_night_day.png',
            'assets/an_naba/naba_rain_garden.png',
            'assets/an_naba/naba_paradise.png',
            'assets/an_naba/bg_sky.png',
            'assets/an_naba/bg_nature.png',
            'assets/an_naba/bg_night.png',
            'assets/an_naba/character_naba.png',
            'assets/an_naba/naba_pointing.png',
            'assets/an_naba/naba_sitting.png'
        ];
        await Promise.all(imagesToLoad.map(src => {
            return new Promise(resolve => {
                const img = new Image();
                img.onload = resolve;
                img.onerror = resolve;
                img.src = src;
            });
        }));

        loadingStatus.textContent = `Memuat Surah An-Naba'...`;
        const json = await fetchWithRetry(`https://equran.id/api/v2/surat/78`);
        
        // Minor delay to ensure browser layout engine settles cached images
        await new Promise(r => setTimeout(r, 100));

        renderSurah(json.data, localContentData[78], 78);

        // Pad to 16-page multiple for offset imposition
        padToMultipleOf16();

        loadingStatus.textContent = "Surah An-Naba' berhasil dimuat!";
        btnPrint.disabled = false;
    } catch (err) {
        console.error(err);
        loadingStatus.textContent = "Error: " + err.message;
        btnLoadData.disabled = false;
    }
}

// ===== EVENTS =====
btnLoadData.addEventListener('click', loadJuzAmma);
btnPrint.addEventListener('click', () => window.print());
