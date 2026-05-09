# Design Critique: Juz Amma — Storybook Edition

**Reviewer:** Design Critique (Cowork)
**Date:** 2026-05-09
**Files reviewed:** `index.html`, `style.css`, `app.js`
**Project context:** Children's book (Permata Kids brand) — A4 portrait, offset Heidelberg SM 74, Stahl folder, 16-page imposition, 300 DPI vector-first assets.
**Stage:** Refinement (working prototype, pre-press).
**Author:** Lazuardi Fikhirudin Leonard — PT Inti Permata Berkah.

---

## Overall Impression

Konsep storybook-nya kuat — tematisasi per-surah ("Cosmic Wonder" untuk An-Naba), float wrap-around layout, medallion verse numbers, dan separasi tafsir/asbabun/tajwid via colored side-stripes adalah sistem yang matang. **Tapi**: artwork ini di-design seperti web app, bukan press-ready file. Banyak efek yang bagus di Chrome (mix-blend-mode, backdrop-filter, drop-shadow, browser print) akan rusak total begitu masuk ke CtP plate. Beberapa ukuran teks juga akan jadi ilegible setelah dicetak.

Biggest opportunity: **decouple "screen prototype" dari "press-ready output"**. HTML/CSS jadi layout iteration tool; final file lewat Puppeteer/InDesign pipeline dengan PDF/X-1a output.

---

## 1. Print Production Readiness (CRITICAL)

| Finding | Severity | Recommendation |
|---|---|---|
| **No bleed**: `.page` di 210×297mm tanpa 3mm bleed | Critical | Ubah canvas ke 216×303mm dengan content area 210×297mm + 3mm bleed semua sisi. Semua full-bleed background harus extend ke 216×303mm. |
| **`mix-blend-mode: multiply`** di `.page-scene-bg` dan `.story-illustration img` | Critical | Browser PDF (`window.print()`) tidak handle blend mode konsisten. Pre-bake efek ke PNG dengan transparent background, hapus property dari CSS. |
| **`backdrop-filter: blur()`** di chips dan cover overlay | Critical | Tidak ter-render di print. Replace dengan flat semi-transparent fill (`rgba(255,255,255,0.85)`). |
| **Browser `window.print()` workflow** | Critical | Tidak embed font, color profile sRGB, raster effects ~96 DPI. Migrate ke Puppeteer/Playwright headless dengan `printToPDF` + font embedding, atau export ke InDesign IDML untuk final compositing. |
| **All-sRGB color** — gold `#FFD666` belum di-test CMYK | Moderate | Akan jadi muddy di CMYK 4-color. Untuk premium feel, pertimbangkan **Pantone 7404 C** sebagai spot color (5th color), atau lock CMYK build di sekitar `C0 M14 Y65 K0` dan proof first. |
| **Drop-shadow filters & inset shadows** | Moderate | Akan ter-raster di low DPI saat browser print. Pre-bake shadow ke asset, atau pastikan rendering pipeline 300 DPI. |
| **No 16-page imposition awareness** | Moderate | Dynamic pagination tidak peduli kelipatan 16. Tambahkan logic "pad to multiple of 16" — diisi full-bleed thematic illustrations atau halaman aktivitas. |
| **`image-rendering` print rules** | Minor | `image-rendering: -webkit-optimize-contrast` adalah hack; tidak ada efek di Firefox/Edge. Pastikan asset memang sudah 300 DPI nominal. |

---

## 2. Typography & Readability (untuk Anak)

| Element | Current | Issue | Recommendation |
|---|---|---|---|
| `.ayat-latin` | 0.7rem (~8.4pt) | Borderline kecil untuk anak 6–10 thn | Naikkan ke **0.85rem** minimum |
| `.tajwid-desc` | 0.56rem (~6.7pt) | **Tidak terbaca** setelah cetak — gum/spread bisa bikin huruf nempel | Naikkan ke **0.7rem** + line-height 1.5 |
| `.tajwid-example-latin` | 0.48rem (~5.8pt) | Di bawah threshold offset minimum | Naikkan ke **0.65rem** atau hilangkan kalau redundant |
| `.cover-footer` | 0.8rem | OK | — |
| `.ayat-arabic` Amiri | 1.8rem, line-height 2.2 | OK, bisa lebih besar | Pertimbangkan **2.1rem** untuk anak. Amiri sudah right choice. |
| `.bismillah-arabic` | 2rem | Terlalu kecil untuk page opening | Naikkan ke **2.4rem** |
| `.surah-title-arabic` | 5.5rem | OK display size | — |
| `.info-card-title` | 0.88rem | Terlihat seperti caption padahal konten penting | Naikkan ke **1.05rem font-weight 800** |

**Pesan utama**: anak-anak target audience butuh minimum **9pt** untuk reading body, dan **6pt** adalah hard floor untuk caption. Saat ini ada beberapa text di bawah floor itu.

---

## 3. Visual Hierarchy

**What draws the eye first** (urutan ideal vs aktual):

- **Cover page** — Title "Juz Amma" gold + glow → benar, hierarchy tercapai.
- **Surah title page** — Arabic name → Latin name (gold) → meaning → meta chips. Logis.
- **Content page** — Konflik di sini. `verse-num` medallion bersaing dengan `story-illustration` dan `page-scene-bg`. Saat scene-bg multiply hidup di belakang, mata bingung mau ke ayat dulu atau gambar dulu. Cropping vignette mask di scene-bg (`mask-image: radial-gradient`) bagus untuk fokus tengah, tapi kadang malah bikin Arabic text "tenggelam".

**Reading flow An-Naba**: Bismillah → ayat 1–5 (no image) → ayat 6–8 (mountains, kiri) → ayat 9–11 (night/day, kanan) → zigzag continues. Naratif ini penting dan jagain. Cuma satu concern: `align-left/align-right` toggle terlalu mekanis. Beberapa tema seharusnya dapat ilustrasi full-width — terutama Judgment Day 17–30 yang sekarang text-only kehilangan gravitas visual.

**Emphasis problems**:

- `.info-card-title` cuma 0.88rem — info card adalah konten penting (pelajaran tafsir), tapi title-nya terlihat seperti caption.
- Page number 0.6rem dengan pill background `rgba(255,249,240,0.85)` — pill feels heavy untuk angka kecil. Cukup angka tanpa pill, atau pakai ornament style sesuai theme.

---

## 4. Consistency

| Element | Issue | Recommendation |
|---|---|---|
| **Icon system** | Mixed: emoji (🌟🖨️🌿📜🔊) + custom medallion + sparkle stars + stars `✦` | Commit ke **satu sistem**. Untuk premium kids book offset, replace semua emoji dengan custom SVG icons match dengan illustrated style. Emoji rendering bervariasi antar OS dan tidak printable konsisten. |
| **Border-radius scale** | 8px (ayat-block), 14px (closing-scene), 16px (info-card), 50px (chips/btn/page-num) | Buat scale: `--r-sm: 8px`, `--r-md: 14px`, `--r-lg: 24px`, `--r-pill: 50px`. |
| **Theming system** | Semua var prefix `--naba-*` — tidak scalable ke surah lain | Refactor ke `--theme-primary`, `--theme-secondary`, `--theme-accent`, `--theme-deep`, `--theme-cream`. Apply via `body[data-surah="78"] { ... }` atau class. Lihat `THEME_REFACTOR_PLAN.md`. |
| **Asset path hardcoded** | `assets/an_naba/...` di app.js | Parameterize: `assets/${surahSlug}/...`. Critical untuk roadmap 30-surah. |
| **Theme array hard-coded di renderSurah** | `themes` array specific An-Naba | Pindah ke data layer (`juzAmmaData[78].themes`). Setiap surah punya thematic groupings di JSON-nya. |
| **Font fallback** | `'Baloo 2', cursive` — bisa render Comic Sans di system tanpa Baloo | Tambahkan fallback yang lebih dekat: `'Baloo 2', 'Quicksand', 'Trebuchet MS', sans-serif`. |

---

## 5. Layout

**Float wrap-around (`align-left`/`align-right`)**: Konsep zigzag bagus untuk visual rhythm, tapi 42% width image dengan `max-height: 220px` di A4 (297mm tinggi) terlihat cramped. Anak-anak respond lebih baik ke **ilustrasi yang dominan** (60–80% width, atau full-bleed spreads). Pertimbangkan dua treatment:

1. **"Story spread"** — full-page illustration kiri, full-page text kanan untuk thematic moments penting (Judgment Day, Paradise).
2. **"Inline marginalia"** — image kecil di outer margin sebagai hint, bukan float wrap. Lebih clean dan mudah di-paginate.

**Closing scene di last page**: `.closing-scene` dengan height 80px min terlalu kecil. Either commit jadi full-bleed `.closing-fullbleed` page (yang sudah dibuat tapi belum dipakai di `renderSurah`!), atau hilangkan saja.

**Front matter missing**: Untuk publikasi resmi via PT Inti Permata Berkah dengan ISBN, butuh:

- Halaman hak cipta + KDT (Katalog Dalam Terbitan)
- Kata Pengantar oleh Lazuardi Fikhirudin Leonard
- Daftar isi (Daftar Surah)
- Cara penggunaan buku (untuk ortu/pendamping)

Saat ini struktur: cover → title surah → content. Belum production-grade untuk distribusi retail.

---

## What Works Well

- **Thematic story groups** sebagai mental model — naratif lebih dari sekuensial — adalah pendekatan yang tepat untuk Permata Kids' positioning.
- **Medallion verse numbers** dengan custom asset jauh lebih premium dari plain numbered circles.
- **Color palette An-Naba** (deep navy + gold + soft cream) feels appropriate dan tidak childish-cliché.
- **Pagination overflow detection** yang dinamis (`isOverflowing`) — solusi engineering elegan untuk content panjangnya bervariasi per surah.
- **Continuation header** ("Lanjutan Surah ...") — touch professional untuk multi-page surahs.
- **Print CSS killing animations dan flattening shadows** — sudah aware soal print constraints, tinggal eskalasi ke level offset.

---

## Priority Recommendations

1. **Migrate dari browser print ke Puppeteer pipeline** — Embed fonts, control color, get real 300 DPI output. Tanpa ini, semua effort visual akan rusak di press. Lihat `PRINT_PRODUCTION_CHECKLIST.md`.
2. **Add 3mm bleed + crop mark generation** — Non-negotiable untuk SM 74 dengan trimming. Saat ini file akan trim ke white edges.
3. **Pre-bake `mix-blend-mode` dan `backdrop-filter` ke PNG assets** — Hapus property dari CSS, ganti dengan static composited PNG dengan transparent BG.
4. **Bump minimum font size ke 9pt body / 6pt absolute floor** — Tajwid descriptions saat ini illegible setelah print.
5. **Refactor theme variables ke `--theme-*` generic + per-surah override** — Required architectural change untuk scale ke 30+ surah tanpa fork CSS. Lihat `THEME_REFACTOR_PLAN.md`.
6. **Add front matter pages** (hak cipta, kata pengantar, daftar isi, cara baca) — Untuk legitimitas publikasi resmi PT IPB.
7. **Plan halaman padding ke kelipatan 16** — Untuk imposition di Stahl folder. Bisa diisi activity pages atau full-bleed surah-end illustrations.

---

## Companion Documents

- `PRINT_PRODUCTION_CHECKLIST.md` — Press-ready checklist untuk Heidelberg SM 74 / Stahl folder.
- `THEME_REFACTOR_PLAN.md` — Architecture plan untuk scale theming ke 30+ surah.
