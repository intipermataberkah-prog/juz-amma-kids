# HANDOFF — Juz 'Amma Storybook Edition

> **Target**: Buku cerita anak premium A4, cetak offset Heidelberg SM 74  
> **Penerbit**: PT Inti Permata Berkah (Permata Kids)  
> **Status**: Surah An-Naba' (78) — **VERIFIED & WORKING (Bug pagination sudah diperbaiki)**  
> **Terakhir diperbarui**: 9 Mei 2026  

---

## 1. Ringkasan Proyek

Aplikasi web yang menghasilkan layout buku cerita anak **Juz 'Amma** (A4, 216×303mm dengan bleed) siap cetak offset. Setiap surah punya karakter maskot, ilustrasi tematik per kelompok ayat, kartu tafsir, asbabun nuzul, dan tajwid.

**Verified page output**: Cover → Hak Cipta → Kata Pengantar → Daftar Surah → Cara Baca → Surah Title → ~8 halaman konten (40 ayat + 3 info card) → padding ke kelipatan 16 = **16 halaman total**.

---

## 2. Quick Start

```bash
# 1. Jalankan HTTP server
cd c:\Users\Win11\.gemini\antigravity\scratch\juz-amma-kids
npx http-server -p 8888

# 2. Buka browser
http://localhost:8888

# 3. Klik "Muat Surah An-Naba'"
# 4. Klik "Cetak (A4)" untuk print/PDF
```

### Prerequisites
- **Node.js** ≥ 16 (untuk `npx http-server`)
- **Python 3.10+** + `rembg`, `Pillow`, `google-genai` (hanya untuk asset pipeline)
- **`.env`** berisi `GOOGLE_API_KEY=xxx` (hanya untuk generate aset baru)

---

## 3. Struktur File

```
juz-amma-kids/
│
├── index.html                        # Entry point (30 baris)
├── style.css                         # Seluruh styling (758 baris)
├── app.js                            # Rendering engine + pagination (674 baris)
├── .env                              # GOOGLE_API_KEY
│
├── data/
│   ├── juz_amma_content.js           # Database lokal: tafsir, asbabun, tajwid
│   └── juz_amma_content.json         # Sumber JSON mentah
│
├── assets/an_naba/                   # 30 aset PNG (Imagen 4 + rembg)
│   ├── character_naba.png            # Maskot karakter
│   ├── naba_mountains.png            # Ilustrasi tematik: gunung
│   ├── naba_night_day.png            # Ilustrasi tematik: malam/siang
│   ├── naba_rain_garden.png          # Ilustrasi tematik: hujan/kebun
│   ├── naba_paradise.png             # Ilustrasi tematik: surga
│   ├── scene_*.png                   # Background scene (5 file)
│   ├── cover_scene.png               # Sampul
│   ├── title_scene.png               # Judul surah
│   ├── medallion_ayat.png            # Nomor ayat
│   ├── divider_ornate.png            # Pemisah
│   └── ... (lihat daftar lengkap di bawah)
│
├── generate_and_process_assets.py    # Pipeline: Imagen 4 → rembg → PNG
├── rebake_assets.py                  # Re-proses transparansi via rembg
├── generate_content_json.py          # Generator database konten
└── HANDOFF.md                        # Dokumen ini
```

### File yang boleh dihapus (eksperimen)
```
al_ikhlas_test.css, al_ikhlas_test.html, 112_al_ikhlas_bg*.jpg,
test_fal.js, test_seedream*.js, test_seedream*.py, generate_test.js,
scratch_remove_bg.py, perfect_remove_bg.py, bg_default.png,
batch_rembg.py, DESIGN_CRITIQUE.md
```

---

## 4. Arsitektur

### Data Flow
```
equran.id/api/v2/surat/78 ──→ apiData (Arabic, Latin, Translation per ayat)
data/juz_amma_content.js  ──→ localData (Tafsir, Asbabun Nuzul, Tajwid)
                              ↓
                        app.js: loadJuzAmma()
                              ↓
    ┌──────────────────────────────────────┐
    │  1. buildCoverPage()                 │
    │  2. buildCopyrightPage()             │
    │  3. buildForewordPage()              │
    │  4. buildTableOfContentsPage()       │
    │  5. buildHowToUsePage()              │
    │  6. renderSurah()                    │
    │     ├─ buildSurahTitlePage()         │
    │     ├─ buildBismillah()              │
    │     ├─ [themes].forEach → groups     │
    │     │  ├─ story-illustration (float) │
    │     │  └─ buildAyatBlock() × N       │
    │     ├─ buildTafsirCard()             │
    │     ├─ buildAsbabunCard()            │
    │     └─ buildTajwidCard()             │
    │  7. padToMultipleOf16()              │
    └──────────────────────────────────────┘
```

### Pagination Engine (CRITICAL)
File: `app.js` line 363–431

Algoritma:
1. Semua konten dikumpulkan sebagai `items[]` (groups, separators, info cards)
2. Setiap item ditambahkan ke halaman, lalu di-cek `isOverflowing()`
3. Jika overflow → item dipindah ke halaman baru
4. **Jika item masih overflow di halaman baru** (terlalu besar) → **group dipecah** menjadi children individu dan di-paginate satu per satu
5. Buffer overflow: **8px** dari padding bawah

**Bug yang sudah diperbaiki**: Sebelumnya, group yang terlalu besar dibiarkan overflow di halaman baru tanpa penanganan, menyebabkan ayat 11–40 hilang.

### Thematic Story Groups
```javascript
const themes = [
    { start: 1,  end: 5,  image: null },                    // Berita Besar
    { start: 6,  end: 8,  image: 'naba_mountains.png' },    // Penciptaan Bumi
    { start: 9,  end: 11, image: 'naba_night_day.png' },    // Malam & Siang
    { start: 12, end: 16, image: 'naba_rain_garden.png' },  // Hujan & Tumbuhan
    { start: 17, end: 30, image: null },                     // Hari Kiamat
    { start: 31, end: 36, image: 'naba_paradise.png' },     // Surga
    { start: 37, end: 40, image: null },                     // Penutup
];
```
Ilustrasi ditampilkan dengan float zigzag (kiri-kanan bergantian), ayat wrap di sekelilingnya.

### Theme System (CSS Variables)
```css
--theme-deep       #1B2845   /* Navy gelap */
--theme-primary    #3A6BC5   /* Biru aksen */
--theme-accent     #FFD666   /* Emas */
--theme-green      #3DAA6D   /* Kartu tafsir */
--theme-purple     #7B68AE   /* Kartu tajwid */
--theme-rose       #E88BA5   /* Aksen */
--theme-orange     #F4A261   /* Aksen */
```
Alias `--naba-*` tersedia untuk backward compat. Untuk surah baru: override `--theme-*`.

---

## 5. Spesifikasi Cetak

| Parameter | Nilai |
|-----------|-------|
| Canvas | 216 × 303 mm (termasuk 3mm bleed) |
| Trim | 210 × 297 mm (A4) |
| Bleed | 3mm semua sisi |
| Padding konten | 10mm atas/bawah, 12mm kiri/kanan |
| Font minimum | 9pt body, 6pt floor |
| Color space | sRGB (perlu CMYK conversion untuk offset) |
| Imposition | Pad ke kelipatan 16 halaman |
| Mesin | Heidelberg SM 74 |

### Font
| Font | Kegunaan | Sumber |
|------|----------|--------|
| Amiri 400/700 | Teks Arab | Google Fonts CDN |
| Baloo 2 400–800 | Judul, label | Google Fonts CDN |
| Nunito 400–900 | Body text | Google Fonts CDN |

Fallback: `'Quicksand', 'Trebuchet MS', sans-serif`

---

## 6. Daftar Aset Lengkap

### Digunakan Aktif
| File | Tipe | Digunakan di |
|------|------|-------------|
| `cover_scene.png` | Full-bleed BG | Cover page |
| `title_scene.png` | Full-bleed BG | Surah title page |
| `character_naba.png` | Maskot | Cover + title float |
| `naba_mountains.png` | Ilustrasi tematik | Ayat 6–8 (float) |
| `naba_night_day.png` | Ilustrasi tematik | Ayat 9–11 (float) |
| `naba_rain_garden.png` | Ilustrasi tematik | Ayat 12–16 (float) |
| `naba_paradise.png` | Ilustrasi tematik | Ayat 31–36 (float) |
| `naba_sitting.png` | Space filler | Halaman terakhir konten |
| `medallion_ayat.png` | Dekoratif | Background nomor ayat |
| `divider_ornate.png` | Dekoratif | Separator antar grup |
| `scene_sky.png` | Scene BG | Ayat 1–5, 21–30 |
| `scene_mountains.png` | Scene BG | Ayat 6–11 |
| `scene_night.png` | Scene BG | Ayat 12–16, 37–40 |
| `scene_rain.png` | Scene BG | Ayat 17–20 |
| `scene_garden.png` | Scene BG | Ayat 31–36 |
| `closing_scene.png` | Scene BG | Closing scene |

### Ada Tapi Tidak Aktif di CSS/JS
`corner_arabesque.png`, `bismillah_ornament.png`, `border_frame.png`, `cloud.png`, `lantern.png`, `telescope.png`, `decor_vine_left.png`, `decor_vine_right.png`, `decor_quran_glow.png`, `decor_stars_cluster.png`, `naba_pointing.png`, `naba_praying.png`, `scene_cover.png`, `character_naba_original.png`

---

## 7. Keputusan Desain

| Keputusan | Alasan |
|-----------|--------|
| `mix-blend-mode: multiply` **DIHAPUS** | Tidak ter-render di print PDF. Aset di-rebake via rembg. |
| `backdrop-filter: blur()` **DIHAPUS** | Tidak ter-render di print. Diganti flat fill. |
| `mask-image: radial-gradient()` **DIHAPUS** | Rawan gagal/hitam pekat di mesin CtP/PDF export. |
| **Thematic Top Canvas** (Baru) | Gambar scene diletakkan di 35% area atas dengan opacity 60% dan di-*fade* menggunakan `linear-gradient` transparan ke warna kertas. Print-safe. |
| Kertas solid `#fcf9f2` (Baru) | Gradien pudar tiga warna dihilangkan. Menggunakan warna *parchment/cream* solid untuk teks agar kontras 100% dan tidak kotor saat dicetak offset. |
| Emoji **DIHAPUS** dari HTML | Rendering bervariasi antar OS, tidak konsisten di cetak offset. |
| `text-shadow` pada Arabic **DIHAPUS** | Tidak relevan untuk offset printing. |
| `popIn` animation **DIHAPUS** dari info-card | Media cetak, animasi tidak ada gunanya. |
| Page number pill background **DIHAPUS** | Terlalu berat visual. Angka plain saja. |
| Gold dust pattern (`page::before`) | **Tampil di web**, tersembunyi saat print (hemat tinta). |
| Overflow buffer **8px** (was 25px) | 25px terlalu banyak waste space per halaman. |

---

## 8. Asset Pipeline

### Generate Aset Baru
```bash
# 1. Edit prompt di generate_and_process_assets.py
# 2. Jalankan (butuh GOOGLE_API_KEY di .env)
python generate_and_process_assets.py

# Pipeline: Imagen 4 → rembg (u2net) → save PNG
```

### Re-bake Transparansi (Tanpa Generate Ulang)
```bash
python rebake_assets.py
# Proses 13 file yang sudah ada melalui rembg ulang
```

### API yang Digunakan
| API | Model | Kegunaan |
|-----|-------|----------|
| Google GenAI | `imagen-4.0-generate-001` | Generate ilustrasi |
| equran.id | REST v2 | Data ayat Arab/Latin/Terjemahan |

---

## 9. Pekerjaan Tersisa

### P0 — Harus Selesai Sebelum Cetak
- [ ] **Puppeteer PDF pipeline** — `printToPDF` dengan font embedding, 300 DPI
- [ ] **CMYK conversion** — Gold `#FFD666` → `C0 M14 Y65 K0` atau Pantone 7404 C
- [ ] **Crop marks** di PDF output
- [ ] **QA visual** pada setiap halaman dengan mata manusia

### P1 — Penting untuk Kualitas
- [ ] **Full-spread ilustrasi** untuk Judgment Day (ayat 17–30, saat ini text-only)
- [ ] **Activity pages** (mewarnai, dot-to-dot) untuk padding halaman kosong
- [ ] **SVG icon system** — ganti sisa emoji dengan custom SVG
- [ ] **Closing full-bleed page** — CSS sudah ada, belum dipakai di render

### P2 — Untuk Scaling ke 30+ Surah
- [ ] Parameterize asset paths: `assets/${surahSlug}/`
- [ ] Ekstrak `themes[]` dari hardcoded ke `data/themes.json`
- [ ] Generator maskot karakter per surah
- [ ] Generator scene background per surah
- [ ] Data tafsir/tajwid untuk surah 79–114

---

## 10. Known Issues (Sudah Diperbaiki)

| Bug | Root Cause | Fix |
|-----|-----------|-----|
| Ayat 11–40 hilang | Pagination engine tidak handle group overflow di halaman baru | Group-splitting algorithm (line 391–424) |
| White background pada ilustrasi | Sisa dari rembg background removal | Aset di-rebake; `mix-blend-mode` dihapus |
| Front matter tidak muncul | Browser cache JS lama | Cache buster `?v=20260509c` di `index.html` |
| Space kosong berlebih | Overflow buffer 25px + padding 12mm/14mm | Dikurangi ke 8px + 10mm/12mm |
| `.page-scene-bg` tersembunyi | Disabled karena white remnants | Re-enabled dengan vignette mask |
