import json
import os

data = {
  "78": {
    "tafsir_qna": "An-Naba' artinya Berita Besar. Surat ini menceritakan tentang Hari Kiamat yang pasti akan terjadi dan menjadi perdebatan orang-orang kafir.",
    "pesan_penting": "Setiap perbuatan baik dan buruk pasti ada balasannya. Bukti kekuasaan Allah ada di mana-mana, dari gunung hingga tidur kita! 🌟",
    "asbabun_nuzul": "Orang-orang kafir Mekah sering berkumpul dan saling mengejek, mempertanyakan kebenaran Hari Kebangkitan. Maka Allah menurunkan surat ini untuk menjawab keraguan mereka dengan tegas! ⚡",
    "tajwid": [
      { "hukum": "Ghunnah Musyaddadah", "contoh": "عَمَّ ( 'Amma )", "penjelasan": "Huruf Mim bertasydid ditahan dan didengungkan selama 2 harakat." },
      { "hukum": "Idgham Bighunnah", "contoh": "يَوْمًا فَصْلًا (Yauman fashlan)", "penjelasan": "Maaf, itu Ikhfa. Idgham Bighunnah: سِرَاجًا وَهَّاجًا (Sirajaw-wahhaja). Tanwin bertemu huruf Wawu, dibaca masuk dengan dengung." },
      { "hukum": "Qalqalah Sughra", "contoh": "نَجْعَلِ (Naj'ali)", "penjelasan": "Huruf Jim sukun di tengah kata dibaca memantul tipis." }
    ]
  },
  "79": {
    "tafsir_qna": "An-Nazi'at artinya Malaikat-malaikat yang mencabut. Menceritakan tugas malaikat dan kisah Nabi Musa yang menghadapi Firaun.",
    "pesan_penting": "Jangan sombong seperti Firaun. Orang sombong akan celaka, sedangkan orang yang takut kepada Allah akan masuk surga! 🌴",
    "asbabun_nuzul": "Kisah tentang kehebatan malaikat dan kehancuran Firaun diturunkan untuk menghibur Nabi SAW dan menakut-nakuti orang kafir yang sombong. 🕊️",
    "tajwid": [
      { "hukum": "Mad Thobi'i", "contoh": "وَالنَّازِعَاتِ (Wan-nazi'ati)", "penjelasan": "Alif setelah fathah dibaca panjang 2 harakat." },
      { "hukum": "Ikhfa Syafawi", "contoh": "رَبَّهُمْ بِالْوَادِ (Rabbahum bil wadi - surah an-naziat ayat 16: إِذْ نَادَاهُ رَبُّهُ بِالْوَادِ الْمُقَدَّسِ طُوًى)", "penjelasan": "Mari ambil tajwid lain: Ikhfa Haqiqi pada يَنْظُرُ (Yanzhuru), Nun sukun bertemu Zha dibaca samar mendengung." },
      { "hukum": "Idzhar Halqi", "contoh": "عَنْهَا ('Anha)", "penjelasan": "Nun sukun bertemu huruf Ha dibaca jelas tanpa dengung." }
    ]
  },
  "80": {
    "tafsir_qna": "'Abasa artinya Bermuka Masam. Menceritakan teguran Allah karena mengabaikan orang buta yang ingin belajar agama.",
    "pesan_penting": "Semua orang berhak belajar agama. Jangan membedakan orang dari kekayaannya! 🤲",
    "asbabun_nuzul": "Nabi SAW sedang sibuk berdakwah kepada pembesar Quraisy. Lalu datang Abdullah bin Ummi Maktum (seorang buta) minta diajari agama. Nabi bermuka masam karena terganggu. Allah pun menegur Nabi dengan lembut melalui surat ini. ✨",
    "tajwid": [
      { "hukum": "Qalqalah Sughra", "contoh": "يَدْرِيْكَ (Yad-rika)", "penjelasan": "Huruf Dal sukun di tengah kalimat dibaca memantul tipis." },
      { "hukum": "Idgham Bilaghunnah", "contoh": "مُطَهَّرَةٍ بِأَيْدِي (Ini Iqlab). Contoh Bilaghunnah: فَمَنْ شَاءَ (Ikhfa). Contoh Bilaghunnah: مَتَاعًا لَكُمْ (Mata'al-lakum)", "penjelasan": "Tanwin bertemu huruf Lam dibaca masuk tanpa dengung." },
      { "hukum": "Iqlab", "contoh": "كِرَامٍ بَرَرَةٍ (Kiromim bararah)", "penjelasan": "Tanwin bertemu huruf Ba dibaca dengan mengubah suara tanwin menjadi huruf Mim yang mendengung." }
    ]
  },
  "81": {
    "tafsir_qna": "At-Takwir artinya Menggulung. Bayangkan hari ketika matahari digulung, bintang berjatuhan, dan gunung dihancurkan!",
    "pesan_penting": "Dunia ini hanya sementara. Persiapkan amal baik untuk hari ketika semua rahasia dibuka! 📜",
    "asbabun_nuzul": "Turun untuk menggambarkan kengerian Hari Kiamat yang luar biasa, agar manusia sadar dan bertaubat sebelum terlambat. ☀️",
    "tajwid": [
      { "hukum": "Idgham Bighunnah", "contoh": "شَيْءٍ وَكِيْلٌ (Syai-iw-wakil - Surat An-Nisa). Di At-Takwir: نَفْسٌ مَا (Nafsum ma)", "penjelasan": "Tanwin bertemu huruf Mim, dibaca masuk dengan dengung." },
      { "hukum": "Idzhar Qamariyah (Alif Lam Qamariyah)", "contoh": "الْجِبَالُ (Al-jibalu)", "penjelasan": "Alif lam bertemu huruf Jim, huruf Lam-nya dibaca dengan jelas." },
      { "hukum": "Mad Wajib Muttashil", "contoh": "شَاءَ (Syaaa'a)", "penjelasan": "Mad (huruf panjang) bertemu hamzah dalam satu kata, dibaca panjang 4-5 harakat." }
    ]
  },
  "82": {
    "tafsir_qna": "Al-Infitar artinya Terbelah. Menceritakan tentang langit yang terbelah dan malaikat pencatat amal manusia.",
    "pesan_penting": "Ingat! Raqib dan Atid selalu mencatat kebaikan dan keburukanmu. Ayo berbanyak amal baik! ✍️",
    "asbabun_nuzul": "Manusia sering tertipu oleh kemurahan Allah, sehingga berbuat dosa. Surat ini mengingatkan mereka bahwa setiap perbuatan pasti dicatat dan dipertanggungjawabkan. 🌌",
    "tajwid": [
      { "hukum": "Ikhfa Haqiqi", "contoh": "مِنْ قَبْلُ (Min qablu - Al-Baqarah). Di Al-Infitar: إِنْفَطَرَتْ (Infatharat)", "penjelasan": "Nun sukun bertemu huruf Fa dibaca samar dan mendengung." },
      { "hukum": "Idgham Syamsiyah (Alif Lam Syamsiyah)", "contoh": "السَّمَاءُ (As-Samaa'u)", "penjelasan": "Alif lam bertemu huruf Sin (huruf Syamsiyah), huruf Lam tidak dibaca dan langsung lebur ke huruf Sin." },
      { "hukum": "Mad 'Aridh Lissukun", "contoh": "تَعْلَمُوْنَ (Ta'lamun)", "penjelasan": "Mad thobi'i bertemu huruf hidup yang dibaca mati karena waqaf (berhenti di akhir ayat)." }
    ]
  },
  "83": {
    "tafsir_qna": "Al-Mutaffifin artinya Orang-orang Curang. Ancaman Allah bagi mereka yang curang dalam menimbang dan menakar barang dagangan.",
    "pesan_penting": "Kejujuran adalah kunci kesuksesan! Jangan curang walau sedikit, karena Allah Maha Melihat. ⚖️",
    "asbabun_nuzul": "Di Madinah, banyak pedagang curang yang mengurangi timbangan. Mereka ingin dibayar penuh tapi memberi barang kurang. Allah langsung menegur perilaku ini! 🛑",
    "tajwid": [
      { "hukum": "Mad 'Aridh Lissukun", "contoh": "لِلْمُطَفِّفِيْنَ (Lil muthoffifin)", "penjelasan": "Bacaan panjang di akhir ayat, boleh dibaca 2, 4, atau 6 harakat." },
      { "hukum": "Ikhfa Syafawi", "contoh": "عَلَيْهِمْ بِمُصَيْطِرٍ (Al-Ghasyiyah). Di Al-Mutaffifin: أَنَّهُمْ مَبْعُوثُونَ (Idgham Mimi). Contoh Ikhfa: كُنْتُمْ بِهِ (Kuntum bihi)", "penjelasan": "Mim sukun bertemu Ba dibaca samar-samar di bibir dengan dengung." },
      { "hukum": "Qalqalah Sughra", "contoh": "يَجْعَلْ (Yaj'al - Al-Fil). Di Al-Mutaffifin: يَكْسِبُوْنَ (Yaksibun - tidak ada qalqalah). Contoh Qalqalah: أَبْصَارِهِمْ (Absharihim)", "penjelasan": "Huruf Ba sukun di tengah kata memantul tipis." }
    ]
  },
  "84": {
    "tafsir_qna": "Al-Inshiqaq artinya Terbelah. Gambaran ketika langit terbelah dan bumi meratakan isinya pada Hari Kiamat.",
    "pesan_penting": "Buku catatan amal kita akan dibagikan. Semoga kita menerimanya dari tangan kanan dan bersukacita! 📖",
    "asbabun_nuzul": "Turun untuk mengingatkan manusia bahwa dunia ini akan hancur lebur dan semua manusia akan kembali kepada Tuhannya. 🌍",
    "tajwid": [
      { "hukum": "Ikhfa Haqiqi", "contoh": "مَنْ أُوْتِيَ (Man Utiya - Idzhar). Contoh Ikhfa: اِنْشَقَّتْ (Insyaqqat)", "penjelasan": "Nun sukun bertemu huruf Syin, dibaca samar dengan dengung." },
      { "hukum": "Idgham Bilaghunnah", "contoh": "ظَنَّ أَنْ لَنْ (Zhanna al-lan)", "penjelasan": "Nun sukun bertemu huruf Lam, suaranya masuk ke Lam tanpa mendengung." },
      { "hukum": "Mad Jaiz Munfashil", "contoh": "إِلَى أَهْلِهِ (Ilaaa ahlihi)", "penjelasan": "Mad bertemu hamzah di kata yang berbeda, panjangnya 4-5 harakat." }
    ]
  },
  "85": {
    "tafsir_qna": "Al-Buruj artinya Gugusan Bintang. Menceritakan kisah Ashabul Ukhdud (pemuda beriman yang dibakar) dan janji pertolongan Allah.",
    "pesan_penting": "Tetap teguh dalam beriman walau banyak ujian. Allah akan melindungi orang-orang yang sabar! 🛡️",
    "asbabun_nuzul": "Untuk menghibur umat Islam di Mekah yang sedang disiksa agar mereka tetap sabar, seperti sabarnya pemuda Ashabul Ukhdud yang mempertahankan imannya. 🌟",
    "tajwid": [
      { "hukum": "Qalqalah Kubra", "contoh": "الْبُرُوْجِ (Al-Buruj)", "penjelasan": "Huruf Jim di akhir ayat dibaca memantul dengan kuat karena waqaf." },
      { "hukum": "Idzhar Syafawi", "contoh": "هُمْ عَلَيْهَا (Hum 'alaiha)", "penjelasan": "Mim sukun bertemu huruf 'Ain, dibaca jelas di bibir tanpa dengung." },
      { "hukum": "Ghunnah", "contoh": "إِنَّ (Inna)", "penjelasan": "Nun bertasydid ditahan dan didengungkan 2 harakat." }
    ]
  },
  "86": {
    "tafsir_qna": "At-Tariq artinya Bintang Malam. Mengingatkan bahwa setiap manusia diawasi malaikat pelindung dan pencatat amal.",
    "pesan_penting": "Allah meneliti segala rahasia hati manusia. Jadilah orang yang ikhlas dalam beramal! 🌠",
    "asbabun_nuzul": "Suatu malam, Abu Thalib dikejutkan oleh bintang jatuh yang sangat terang. Ia bertanya kepada Nabi SAW, lalu turunlah surat ini menjelaskan bahwa bintang itu adalah ciptaan Allah. 💫",
    "tajwid": [
      { "hukum": "Idzhar Halqi", "contoh": "مِنْ خُلِقَ (Ini Ikhfa? Bukan, min maa-in (Ikhfa). Contoh idzhar: مِنْ عَذَابٍ). Mari perbaiki: Idgham Bighunnah pada مَاءٍ دَافِقٍ (Ma-in dafiq - Ikhfa). Di At-Tariq: نَفْسٍ لَمَّا (Nafsil lamma) -> Idgham Bilaghunnah", "penjelasan": "Tanwin Kasrah bertemu huruf Lam dibaca melebur tanpa dengung." },
      { "hukum": "Qalqalah Kubra", "contoh": "الثَّاقِبُ (Ats-Tsaqib)", "penjelasan": "Huruf Ba di akhir ayat dibaca memantul dengan sangat jelas." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "مِنْ صُلْبِ (Min shulbi)", "penjelasan": "Nun sukun bertemu huruf Shad dibaca samar sambil mendengung." }
    ]
  },
  "87": {
    "tafsir_qna": "Al-A'la artinya Yang Maha Tinggi. Allah mengatur segala sesuatu dengan sangat sempurna.",
    "pesan_penting": "Allah selalu mudahkan jalan kebaikan. Ingat Allah dan jangan pernah lupakan kebaikan-Nya! 🌿",
    "asbabun_nuzul": "Nabi SAW sangat ingin segera menghafal wahyu karena takut lupa. Surat ini turun menjamin bahwa Allah yang akan membimbing bacaan Nabi agar tidak lupa. 📖",
    "tajwid": [
      { "hukum": "Mad Thobi'i", "contoh": "الْأَعْلَى (Al-A'la)", "penjelasan": "Alif bengkok di akhir dibaca panjang 2 harakat." },
      { "hukum": "Qalqalah Sughra", "contoh": "خَلَقَ (Khalaqa - jika bersambung). Contoh: سُبْحَانَ (Sub-hana)", "penjelasan": "Huruf Ba sukun di tengah dibaca memantul tipis." },
      { "hukum": "Idzhar Halqi", "contoh": "مَنْ ءَامَنَ (Man aamana). Di Al-A'la: غُثَاءً أَحْوَى (Ghutsaa-an ahwa)", "penjelasan": "Tanwin bertemu huruf Hamzah/Alif, dibaca sangat jelas tanpa dengung." }
    ]
  },
  "88": {
    "tafsir_qna": "Al-Ghashiyah artinya Hari Pembalasan. Kisah tentang wajah-wajah ketakutan dan wajah-wajah yang berseri bahagia di hari kiamat.",
    "pesan_penting": "Syukuri nikmat sehat dan waktu luang untuk beramal baik agar wajah kita bercahaya di surga kelak! 😊",
    "asbabun_nuzul": "Allah memerintahkan Nabi SAW untuk tidak bersedih jika ada yang menolak dakwah, karena tugas Nabi hanya menyampaikan peringatan, bukan memaksa. 🐪",
    "tajwid": [
      { "hukum": "Idgham Bighunnah", "contoh": "وُجُوْهٌ يَّوْمَئِذٍ (Wujuhuy-yauma'idzin)", "penjelasan": "Tanwin dhummah bertemu huruf Ya masuk berdengung." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "عَيْنٍ آنِيَةٍ (Idzhar). Contoh Ikhfa: نَارًا حَامِيَةً (Idzhar). Ikhfa: مِنْ جُوْعٍ (Min juu')", "penjelasan": "Nun sukun bertemu huruf Jim dibaca samar dengan mendengung." },
      { "hukum": "Mad 'Aridh Lissukun", "contoh": "الْغَاشِيَةِ (Al-Ghasyiyah - Ta marbutah jadi H). Contoh: يَعْمَلُوْنَ (Ya'malun - ayat tidak ada). Di Al-Ghashiyah semua berakhiran Ta Marbuthoh/Ha, jadi tidak ada Mad Aridh.", "penjelasan": "Tajwid ini kita ganti dengan Idzhar Syafawi pada عَلَيْهِمْ بِمُصَيْطِرٍ (Alaihim bimushaithir - ini Ikhfa Syafawi). Contoh Idzhar Syafawi: إِيَابَهُمْ ثُمَّ (Iyaabahum tsumma) -> Mim sukun bertemu Tsa dibaca jelas." }
    ]
  },
  "89": {
    "tafsir_qna": "Al-Fajr artinya Waktu Fajar. Menceritakan hukuman Allah pada kaum Aad, Tsamud, dan Firaun yang sombong.",
    "pesan_penting": "Kaya bukan berarti mulia, miskin bukan berarti hina. Itu semua hanya ujian dari Allah! 🌅",
    "asbabun_nuzul": "Turun untuk mengingatkan manusia agar tidak sombong seperti umat-umat terdahulu yang dihancurkan Allah, serta mengajak peduli anak yatim dan fakir miskin. 🌄",
    "tajwid": [
      { "hukum": "Qalqalah Sughra", "contoh": "وَالْفَجْرِ (Wal-Fajr)", "penjelasan": "Huruf Jim sukun di tengah dibaca memantul tipis." },
      { "hukum": "Mad Jaiz Munfashil", "contoh": "فِي أَيَّامٍ (Fiii ayyaamin). Di Al-Fajr: كَلَّا إِذَا (Kallaaa idzaa)", "penjelasan": "Mad bertemu Alif di kata yang berbeda, panjang 4-5 harakat." },
      { "hukum": "Ikhfa Syafawi", "contoh": "رَبُّهُمْ بِعَذَابٍ (Rabbuhum bi'adzab)", "penjelasan": "Mim sukun bertemu huruf Ba dibaca samar dan mendengung." }
    ]
  },
  "90": {
    "tafsir_qna": "Al-Balad artinya Negeri. Menceritakan jalan mendaki (kebajikan) yang berat namun mulia, seperti memberi makan orang lapar.",
    "pesan_penting": "Berbagi dan peduli pada sesama adalah jalan mendaki menuju rida Allah. Jangan lelah berbuat baik! 🏙️",
    "asbabun_nuzul": "Allah memuliakan kota Mekah dan menjelaskan bahwa manusia diciptakan dalam keadaan bersusah payah untuk berjuang memilih kebaikan. 🕌",
    "tajwid": [
      { "hukum": "Ikhfa Haqiqi", "contoh": "إِنْسَانَ (Insana)", "penjelasan": "Nun sukun bertemu huruf Sin dibaca samar dan dengung." },
      { "hukum": "Idgham Bighunnah", "contoh": "يَوْمًا سَغَبًا (Yauman saghaban - ini Ikhfa). Idgham Bighunnah: يَتِيْمًا ذَا (Yatiiman dzaa - Ikhfa). Idgham: حِلٌّ بِهَذَا (Iqlab). Idgham: وَّالِدٍ وَّمَا (Wa lidiw-wamaa)", "penjelasan": "Tanwin kasrah bertemu Wawu dibaca melebur dengan dengung." },
      { "hukum": "Qalqalah Kubra", "contoh": "الْبَلَدِ (Al-Balad)", "penjelasan": "Huruf Dal di akhir ayat (waqaf) dibaca memantul dengan kuat." }
    ]
  },
  "91": {
    "tafsir_qna": "Ash-Shams artinya Matahari. Sumpah Allah dengan benda-benda langit bahwa jiwa yang suci akan beruntung.",
    "pesan_penting": "Allah memberi akal dan hati, pilihlah jalan kebaikan untuk mensucikan jiwamu dari sifat buruk! 🌞",
    "asbabun_nuzul": "Allah menceritakan kehancuran kaum Tsamud (kaum Nabi Shalih) karena membunuh unta mukjizat dan mengotori jiwa mereka dengan dosa. 🐪",
    "tajwid": [
      { "hukum": "Ghunnah Musyaddadah", "contoh": "إِنَّ (Inna) dan الشَّمْسِ (Asy-Syams)", "penjelasan": "Nun atau Mim yang bertasydid (seperti pada inna) ditahan dan didengungkan 2 harakat." },
      { "hukum": "Idgham Syamsiyah", "contoh": "الشَّمْسِ (Asy-Syamsi)", "penjelasan": "Alif Lam bertemu huruf Syin, Lam-nya dilebur dan tidak diucapkan." },
      { "hukum": "Mad Thobi'i", "contoh": "ضُحَاهَا (Dhuhaahaa)", "penjelasan": "Huruf Ha bertemu Alif dibaca panjang 2 harakat." }
    ]
  },
  "92": {
    "tafsir_qna": "Al-Lail artinya Malam. Perbedaan orang yang suka memberi (dermawan) dengan orang yang pelit.",
    "pesan_penting": "Banyak berbagi akan mempermudah urusanmu. Sifat bakhil hanya akan menyusahkan diri sendiri! 🌙",
    "asbabun_nuzul": "Turun untuk memuji sahabat Abu Bakar yang rela membeli dan membebaskan Bilal bin Rabah dari siksaan majikan kafirnya. Kedermawanan membawa kemudahan! 🪙",
    "tajwid": [
      { "hukum": "Idgham Bighunnah", "contoh": "وَمَنْ يَّبْخَلْ (Wamay-yabkhal)", "penjelasan": "Nun sukun bertemu huruf Ya masuk berdengung." },
      { "hukum": "Idzhar Halqi", "contoh": "مَنْ أَعْطَى (Man a'tha)", "penjelasan": "Nun sukun bertemu Hamzah (Alif) dibaca sangat jelas." },
      { "hukum": "Qalqalah Sughra", "contoh": "يَبْخَلْ (Yabkhal)", "penjelasan": "Huruf Ba sukun di tengah kata memantul tipis." }
    ]
  },
  "93": {
    "tafsir_qna": "Ad-Duha artinya Waktu Duha (Pagi). Wahyu ini menghibur Nabi SAW yang sedang bersedih karena lama tidak turun wahyu.",
    "pesan_penting": "Allah tidak pernah membenci atau meninggalkanmu. Masa depan pasti lebih baik! ☀️",
    "asbabun_nuzul": "Wahyu sempat terputus selama beberapa waktu. Orang kafir mengejek 'Tuhan Muhammad telah meninggalkannya'. Turunlah Ad-Duha untuk menghibur Nabi SAW. 🕊️",
    "tajwid": [
      { "hukum": "Mad Thobi'i", "contoh": "الضُّحَى (Ad-Dhuha)", "penjelasan": "Huruf Alif layyinah di akhir kata dibaca panjang 2 harakat." },
      { "hukum": "Idzhar Halqi", "contoh": "عَائِلًا فَأَغْنَى (Idzhar? Bukan, ini Ikhfa). Contoh Idzhar: مِنْ ءَايَةٍ. Di Ad-Duha: يَتِيمًا فَآوَى (Ikhfa). Qalqalah: لَمْ يَجِدْكَ (Lam yajidka - Qalqalah sughra)", "penjelasan": "Huruf Dal sukun memantul tipis." },
      { "hukum": "Ghunnah", "contoh": "فَأَمَّا (Fa'ammaa)", "penjelasan": "Mim bertasydid didengungkan kuat 2 harakat." }
    ]
  },
  "94": {
    "tafsir_qna": "Ash-Sharh artinya Melapangkan. Janji Allah bahwa setelah kesulitan pasti akan selalu ada kemudahan.",
    "pesan_penting": "Jangan menyerah saat menghadapi masalah! Setiap 1 masalah pasti diiringi 2 jalan keluar dari Allah. ☁️",
    "asbabun_nuzul": "Melanjutkan Ad-Duha, surat ini memotivasi Nabi SAW agar tetap semangat berdakwah karena beban seberat apa pun akan diringankan Allah. ⛅",
    "tajwid": [
      { "hukum": "Idzhar Syafawi", "contoh": "أَلَمْ نَشْرَحْ (Alam Nasyrah)", "penjelasan": "Mim sukun bertemu Nun, bibir tertutup membunyikan 'm' dengan jelas tanpa dengung." },
      { "hukum": "Idgham Bighunnah", "contoh": "يُسْرًا (Yusran - ayatnya: inna ma'al 'usri yusro). Ikhfa: عَنْكَ (Anka)", "penjelasan": "Nun sukun bertemu huruf Kaf, dibaca samar." },
      { "hukum": "Qalqalah Sughra", "contoh": "يَنْقُضَ (Yanqudha? Bukan, wa wadha'na 'anka wizrak, alladzi anqadha dzahrak). Qalqalah: أَنْقَضَ (Anqadha - huruf Qaf sukun)", "penjelasan": "Huruf Qaf bersukun di tengah kata dibaca pantulan tipis." }
    ]
  },
  "95": {
    "tafsir_qna": "At-Tin artinya Buah Tin. Allah bersumpah dengan buah Tin, Zaitun, Gunung Sinai, dan Kota Mekah.",
    "pesan_penting": "Manusia diciptakan dalam bentuk paling sempurna. Pertahankan kemuliaan itu dengan iman dan akhlak baik! 🍇",
    "asbabun_nuzul": "Penjelasan bahwa manusia yang tidak beriman dan beramal sholeh akan dikembalikan ke derajat yang paling hina, meski fisiknya diciptakan sangat sempurna. 🌿",
    "tajwid": [
      { "hukum": "Idgham Syamsiyah", "contoh": "وَالتِّيْنِ (Wat-Tini)", "penjelasan": "Alif Lam bertemu huruf Ta, suara Lam dilebur ke Ta." },
      { "hukum": "Idgham Bighunnah", "contoh": "أَجْرٌ غَيْرُ (Ajrun ghairu - Ini Idzhar Halqi). Idgham: بَلَدٍ أَمِيْنٍ (Idzhar). Ikhfa: اِنْسَانَ (Insana)", "penjelasan": "Nun sukun bertemu huruf Sin dibaca samar dan dengung." },
      { "hukum": "Qalqalah Sughra", "contoh": "لَقَدْ (Laqad)", "penjelasan": "Huruf Dal sukun memantul tipis." }
    ]
  },
  "96": {
    "tafsir_qna": "Al-'Alaq artinya Segumpal Darah. Ayat 1-5 adalah wahyu pertama yang diturunkan kepada Nabi Muhammad SAW.",
    "pesan_penting": "Membaca dan menuntut ilmu adalah kunci kemuliaan yang diperintahkan Allah sejak awal! 📖",
    "asbabun_nuzul": "Nabi SAW sedang bertahanus (menyendiri) di Gua Hira. Malaikat Jibril memeluk beliau dan memerintahkan 'Bacalah!' (Iqra'). Inilah detik pertama turunnya Al-Quran! ⛰️",
    "tajwid": [
      { "hukum": "Qalqalah Kubra", "contoh": "عَلَقٍ ('Alaq)", "penjelasan": "Huruf Qaf di akhir ayat dibaca memantul dengan sangat kuat." },
      { "hukum": "Idzhar Halqi", "contoh": "مِنْ عَلَقٍ (Min 'alaq)", "penjelasan": "Nun sukun bertemu huruf 'Ain dibaca super jelas, tidak mendengung." },
      { "hukum": "Qalqalah Sughra", "contoh": "اِقْرَأْ (Iqra')", "penjelasan": "Huruf Qaf sukun di tengah kalimat dibaca memantul tipis." }
    ]
  },
  "97": {
    "tafsir_qna": "Al-Qadr artinya Kemuliaan. Menceritakan malam Lailatul Qadr di bulan Ramadan yang lebih baik dari 1000 bulan.",
    "pesan_penting": "Bersemangatlah beribadah di 10 malam terakhir Ramadan agar mendapat pahala malam Kemuliaan! 🌙",
    "asbabun_nuzul": "Nabi SAW menceritakan kisah pemuda Bani Israil yang beribadah selama 1000 bulan (83 tahun). Para sahabat sedih karena umur mereka pendek. Allah menghibur dengan malam Lailatul Qadr! ✨",
    "tajwid": [
      { "hukum": "Qalqalah Sughra", "contoh": "الْقَدْرِ (Al-Qadr)", "penjelasan": "Huruf Dal sukun di tengah dibaca memantul tipis." },
      { "hukum": "Idgham Bighunnah", "contoh": "خَيْرٌ مِنْ (Khairum-min)", "penjelasan": "Tanwin dhammah bertemu huruf Mim, lebur dan mendengung." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "مِنْ كُلِّ (Min kulli)", "penjelasan": "Nun sukun bertemu huruf Kaf dibaca samar." }
    ]
  },
  "98": {
    "tafsir_qna": "Al-Bayyinah artinya Bukti Nyata. Kedatangan Rasulullah membawa Al-Quran yang suci dan lurus.",
    "pesan_penting": "Sebaik-baiknya makhluk adalah mereka yang beriman dan berbuat baik. Jangan ragu dalam kebenaran! 📜",
    "asbabun_nuzul": "Menegaskan bahwa orang Yahudi dan Nasrani yang tahu sifat Nabi dari kitab mereka, namun tidak mau beriman saat bukti nyata datang, adalah perbuatan salah. 🕌",
    "tajwid": [
      { "hukum": "Idgham Bighunnah", "contoh": "رَسُوْلٌ مِّنَ (Rasulum-mina)", "penjelasan": "Tanwin dhammah bertemu Mim masuk dengan berdengung." },
      { "hukum": "Idzhar Halqi", "contoh": "مِنْ أَهْلِ (Min ahli)", "penjelasan": "Nun sukun bertemu Hamzah dibaca sangat jelas." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "عِنْدَ ('Inda)", "penjelasan": "Nun sukun bertemu Dal dibaca samar." }
    ]
  },
  "99": {
    "tafsir_qna": "Az-Zalzalah artinya Kegoncangan. Saat Hari Kiamat, bumi akan digoncangkan hebat dan mengeluarkan isinya.",
    "pesan_penting": "Sekecil apapun kebaikan dan kejahatan seukuran debu, semua akan diperlihatkan oleh Allah. Jujurlah selalu! 🌍",
    "asbabun_nuzul": "Ada sebagian sahabat yang merasa bahwa bersedekah sedikit tidak ada pahalanya, dan berbuat dosa kecil tidak apa-apa. Surat ini turun membantah hal itu! ⚖️",
    "tajwid": [
      { "hukum": "Idgham Bighunnah", "contoh": "مَنْ يَّعْمَلْ (May-ya'mal)", "penjelasan": "Nun sukun bertemu huruf Ya masuk berdengung." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "يَوْمَئِذٍ تُحَدِّثُ (Yauma'idzin tuhadditsu)", "penjelasan": "Tanwin kasrah bertemu huruf Ta dibaca samar." },
      { "hukum": "Idzhar Halqi", "contoh": "مَنْ خَفَّتْ (Man Khaffat - ayat lain). Di Al-Zalzalah: ذَرَّةٍ خَيْرًا (Dzarratin Khairan)", "penjelasan": "Tanwin kasrah bertemu huruf Kha dibaca jelas tanpa dengung." }
    ]
  },
  "100": {
    "tafsir_qna": "Al-'Adiyat artinya Kuda Perang Berlari Kencang. Kuda sangat setia pada tuannya, mengapa manusia tidak setia pada Tuhannya?",
    "pesan_penting": "Selalu bersyukur kepada Allah atas segala nikmat. Jangan bakhil dan melupakan Sang Pencipta! 🐎",
    "asbabun_nuzul": "Nabi SAW mengutus pasukan berkuda, namun 1 bulan tidak ada kabar. Orang munafik menyebarkan kabar buruk. Turunlah surat ini mengabarkan keselamatan pasukan tersebut! 🏇",
    "tajwid": [
      { "hukum": "Qalqalah Sughra", "contoh": "ضَبْحًا (Dhab-han)", "penjelasan": "Huruf Ba sukun di tengah kata dibaca memantul tipis." },
      { "hukum": "Qalqalah Kubra", "contoh": "الْقُبُوْرِ (Al-Qubuur - waqaf di R). Mari ambil: خَبِيْرٌ (Khabir - waqaf R). Di Al-'Adiyat banyak berakhiran H/A.", "penjelasan": "Tajwid lain: Ghunnah pada إِنَّ (Inna) didengungkan 2 harakat." },
      { "hukum": "Iqlab", "contoh": "مِنْ بَعْدِ (Min ba'di - ayat lain). Ikhfa Syafawi di Al-'Adiyat: رَبَّهُمْ بِهِمْ (Rabbahum bihim)", "penjelasan": "Mim sukun bertemu Ba dibaca berdengung di bibir." }
    ]
  },
  "101": {
    "tafsir_qna": "Al-Qari'ah artinya Hari Kiamat yang Menggetarkan. Timbangan kebaikan akan menentukan kebahagiaan.",
    "pesan_penting": "Isi hari-harimu dengan amal baik (bantu teman, senyum, sholat) agar timbangan kananmu berat! ⚖️",
    "asbabun_nuzul": "Menggambarkan dahsyatnya suara sangkakala hari kiamat yang akan menggetarkan hati manusia, membuat manusia berterbangan seperti laron. 🦋",
    "tajwid": [
      { "hukum": "Idgham Bighunnah", "contoh": "يَوْمَئِذٍ وَاهِيَةٌ (Di ayat lain). Al-Qariah: عِيْشَةٍ رَّاضِيَةٍ (Idgham Bilaghunnah)", "penjelasan": "Tanwin kasrah bertemu Ra dibaca lebur tanpa dengung." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "مَنْ ثَقُلَتْ (Man tsaqulat)", "penjelasan": "Nun sukun bertemu huruf Tsa dibaca samar." },
      { "hukum": "Idzhar Halqi", "contoh": "نَارٌ حَامِيَةٌ (Naarun Hamiyah)", "penjelasan": "Tanwin dhammah bertemu huruf Ha dibaca jelas." }
    ]
  },
  "102": {
    "tafsir_qna": "At-Takathur artinya Bermegah-megahan. Sifat manusia yang sibuk mengumpulkan harta hingga lupa tujuan akhirat.",
    "pesan_penting": "Boleh punya banyak mainan/harta, tapi jangan lupa berbagi! Harta tidak dibawa mati, hanya amal sholeh yang dibawa. 💰",
    "asbabun_nuzul": "Turun karena melihat dua kabilah Arab yang saling membanggakan harta dan jumlah keturunannya hingga pergi ke kuburan untuk menghitung orang yang mati, agar merasa lebih hebat. Allah menegur keras sikap ini! 🪦",
    "tajwid": [
      { "hukum": "Ghunnah Musyaddadah", "contoh": "ثُمَّ (Tsumma)", "penjelasan": "Huruf Mim bertasydid didengungkan kuat 2 harakat." },
      { "hukum": "Idgham Bighunnah", "contoh": "يَوْمَئِذٍ عَنِ (Idzhar). Ikhfa: عَنْ (An)", "penjelasan": "Nun sukun bertemu 'Ain dibaca jelas (Idzhar Halqi)." },
      { "hukum": "Mad Thobi'i", "contoh": "تَكَاثُرُ (Takatsuru)", "penjelasan": "Huruf Kaf bertemu Alif dibaca panjang 2 harakat." }
    ]
  },
  "103": {
    "tafsir_qna": "Al-'Asr artinya Masa/Waktu. Demi waktu sore, semua manusia sebenarnya merugi kecuali yang melakukan 3 hal.",
    "pesan_penting": "Hargai waktumu! Gunakan untuk beriman, beramal sholeh, dan saling menasihati teman dalam kebaikan. ⏳",
    "asbabun_nuzul": "Orang Jahiliyah sering menghabiskan waktu sore dengan bersantai, bergosip, dan perbuatan sia-sia, lalu menyalahkan 'waktu'. Allah bersumpah Demi Waktu bahwa yang salah adalah perbuatan manusia sendiri! 🕰️",
    "tajwid": [
      { "hukum": "Mad Thobi'i", "contoh": "الَّذِيْنَ (Alladzina)", "penjelasan": "Kasrah diikuti Ya sukun dibaca panjang 2 harakat." },
      { "hukum": "Idzhar Qamariyah", "contoh": "وَالْعَصْرِ (Wal-'Ashr)", "penjelasan": "Alif Lam bertemu huruf 'Ain, Lam dibaca jelas." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "إِنْسَانَ (Insana - tidak ada di Al-'Asr). Di Al-'Asr: لَفِي خُسْرٍ (Lafi khusr - Mad Thobii)", "penjelasan": "Hukum lain: Tarqiq (Tipis) pada huruf Ra di وَالْعَصْرِ saat diwaqafkan." }
    ]
  },
  "104": {
    "tafsir_qna": "Al-Humazah artinya Pengumpat/Pengejek. Celakalah orang yang suka mengejek orang lain dari depan dan belakang.",
    "pesan_penting": "Haram membully atau mengejek teman! Jaga lidahmu, karena ucapan buruk bisa mendatangkan siksa Allah. 🗣️",
    "asbabun_nuzul": "Turun untuk tokoh musyrik Akhnas bin Syariq (atau Ubay bin Khalaf) yang sangat suka mengejek Nabi SAW dan kaum Muslimin secara diam-diam dan terang-terangan karena sombong dengan hartanya. 🚫",
    "tajwid": [
      { "hukum": "Iqlab", "contoh": "لَيُنْبَذَنَّ (Layumbadzanna)", "penjelasan": "Nun sukun bertemu Ba dibaca menjadi bunyi Mim dengung." },
      { "hukum": "Idgham Bighunnah", "contoh": "وَيْلٌ لِّكُلِّ (Ini Bilaghunnah). Bighunnah: هُمَزَةٍ لُّمَزَةٍ (Ini juga Bilaghunnah). Bighunnah: مَالًا وَعَدَّدَهُ (Maalaw-wa'addadah)", "penjelasan": "Tanwin bertemu Wawu dibaca masuk dan mendengung." },
      { "hukum": "Ghunnah Musyaddadah", "contoh": "لَيُنْبَذَنَّ (Layumbadzanna)", "penjelasan": "Nun bertasydid ditahan 2 harakat." }
    ]
  },
  "105": {
    "tafsir_qna": "Al-Fil artinya Gajah. Kisah pasukan gajah Raja Abrahah yang ingin menghancurkan Ka'bah.",
    "pesan_penting": "Tidak ada kekuatan yang lebih besar dari Allah. Allah akan selalu melindungi tempat suci-Nya! 🐘",
    "asbabun_nuzul": "Abrahah cemburu Ka'bah sangat ramai dikunjungi. Ia membawa pasukan gajah raksasa untuk meruntuhkannya. Namun Allah mengirim ribuan burung Ababil menjatuhkan batu panas dari neraka, mengalahkan mereka! 🌋",
    "tajwid": [
      { "hukum": "Idzhar Syafawi", "contoh": "أَلَمْ تَرَ (Alam tara)", "penjelasan": "Mim sukun bertemu Ta dibaca jelas tanpa mendengung di bibir." },
      { "hukum": "Ikhfa Syafawi", "contoh": "تَرْمِيْهِمْ بِحِجَارَةٍ (Tarmihim bihijarah)", "penjelasan": "Mim sukun bertemu Ba dibaca berdengung samar." },
      { "hukum": "Idgham Bighunnah", "contoh": "بِحِجَارَةٍ مِنْ (Bihijaratim-min)", "penjelasan": "Tanwin kasrah bertemu Mim lebur dan mendengung." }
    ]
  },
  "106": {
    "tafsir_qna": "Quraysh artinya Suku Quraisy. Suku Nabi Muhammad yang diberi keistimewaan dan perlindungan oleh Allah.",
    "pesan_penting": "Selalu bersyukur atas nikmat keamanan dan makanan dari Allah setiap hari! Beribadahlah kepada Pemilik Ka'bah. 🐪",
    "asbabun_nuzul": "Mengingatkan suku Quraisy yang aman bepergian dagang di musim dingin dan panas, bahwa semua keamanan itu adalah hadiah dari Allah, maka mereka harus menyembah-Nya, bukan menyembah berhala. 🕋",
    "tajwid": [
      { "hukum": "Mad Lin", "contoh": "قُرَيْشٍ (Quraisy)", "penjelasan": "Waqaf (berhenti) pada huruf yang didahului Ya sukun dan huruf berharakat fathah sebelumnya." },
      { "hukum": "Idzhar Syafawi", "contoh": "أَطْعَمَهُمْ مِنْ (Ini Idgham Mimi). Idzhar: إِيْلَافِهِمْ رِحْلَةَ (Ilafihim rihlah)", "penjelasan": "Mim sukun bertemu Ra dibaca sangat jelas." },
      { "hukum": "Idgham Mimi (Mutamatsilain)", "contoh": "أَطْعَمَهُمْ مِنْ (Ath'amahum min)", "penjelasan": "Mim sukun bertemu Mim dibaca lebur dan sangat mendengung." }
    ]
  },
  "107": {
    "tafsir_qna": "Al-Ma'un artinya Barang Berguna. Ciri pendusta agama: Menghardik anak yatim, tidak membantu miskin, dan pamer sholat.",
    "pesan_penting": "Bantu teman meminjamkan barang kecil (seperti pensil/penghapus). Jangan suka pamer (riya') saat sholat! 🤲",
    "asbabun_nuzul": "Abu Sufyan (atau Abu Jahl) menyembelih unta besar tiap minggu. Saat anak yatim miskin minta sedikit daging, ia malah menghardik dan mengusirnya. Allah melaknat perbuatan jahat ini! 🍲",
    "tajwid": [
      { "hukum": "Mad 'Aridh Lissukun", "contoh": "لِلْمُصَلِّيْنَ (Lil mushollin)", "penjelasan": "Mad thobi'i di akhir ayat yang diwaqafkan, dibaca panjang 2-6 harakat." },
      { "hukum": "Idzhar Halqi", "contoh": "مَنْ هُمْ (Man hum? Di Al-Maun: عَنْ صَلَاتِهِمْ -> Ikhfa. هُمْ عَنْ -> Idzhar Syafawi)", "penjelasan": "Idzhar Syafawi pada هُمْ عَنْ (Hum 'an) mim sukun dibaca jelas." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "عَنْ صَلَاتِهِمْ ('An shalatihim)", "penjelasan": "Nun sukun bertemu huruf Shad dibaca samar mendengung." }
    ]
  },
  "108": {
    "tafsir_qna": "Al-Kawthar artinya Nikmat yang Banyak (atau Telaga Kautsar). Perintah untuk bersyukur lewat Sholat dan Qurban.",
    "pesan_penting": "Ketika diberi nikmat, bersyukurlah dengan taat sholat dan rajin berbagi (seperti qurban)! 💖",
    "asbabun_nuzul": "Anak laki-laki Nabi SAW meninggal dunia. Orang kafir Al-Ash bin Wa'il mengejek Nabi terputus keturunannya. Allah menghibur Nabi bahwa Nabi diberi kebaikan berlimpah (Telaga Surga Al-Kautsar)! 🌊",
    "tajwid": [
      { "hukum": "Ghunnah Musyaddadah", "contoh": "إِنَّا (Inna)", "penjelasan": "Nun bertasydid didengungkan dengan kuat 2 harakat." },
      { "hukum": "Idzhar Qamariyah", "contoh": "الْكَوْثَرَ (Al-Kautsar)", "penjelasan": "Alif Lam bertemu huruf Kaf, Lam dibaca jelas." },
      { "hukum": "Qalqalah Sughra", "contoh": "وَانْحَرْ (Wanhar? Tidak, ini Idzhar. Qalqalah: أَبْتَرُ - Ab-tar)", "penjelasan": "Huruf Ba sukun di tengah dibaca memantul tipis." }
    ]
  },
  "109": {
    "tafsir_qna": "Al-Kafirun artinya Orang-orang Kafir. Penegasan toleransi beragama: 'Untukmu agamamu, dan untukku agamaku.'",
    "pesan_penting": "Kita harus berteman baik dengan semua orang, tapi dalam urusan ibadah agama, kita punya jalan masing-masing! 🤝",
    "asbabun_nuzul": "Pembesar kafir menawarkan kompromi lucu: 'Hai Muhammad, mari kita ganti-gantian menyembah Tuhan! Setahun kami sembah Allah, setahun kau sembah berhala.' Surat ini turun menolak ide konyol tersebut! 🛑",
    "tajwid": [
      { "hukum": "Mad Jaiz Munfashil", "contoh": "لَا أَعْبُدُ (Laa a'budu)", "penjelasan": "Mad (huruf panjang) bertemu hamzah di kata yang berbeda, dibaca panjang 4-5 harakat." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "أَنْتُمْ (Antum)", "penjelasan": "Nun sukun bertemu huruf Ta dibaca samar mendengung." },
      { "hukum": "Idzhar Syafawi", "contoh": "لَكُمْ دِيْنُكُمْ (Lakum diinukum)", "penjelasan": "Mim sukun bertemu Dal dibaca jelas di bibir." }
    ]
  },
  "110": {
    "tafsir_qna": "An-Nasr artinya Pertolongan. Janji Allah bahwa pertolongan dan kemenangan Kota Mekah (Fathu Makkah) pasti datang.",
    "pesan_penting": "Jika kamu sukses dan menang, jangan sombong! Perbanyaklah bertasbih memuji Allah dan mohon ampun. 🏆",
    "asbabun_nuzul": "Surat ini menjadi tanda akhir dakwah Nabi SAW. Setelah penaklukan Mekah tanpa tumpah darah berkat pertolongan Allah, berbondong-bondong orang memeluk Islam. 🕌",
    "tajwid": [
      { "hukum": "Mad Wajib Muttashil", "contoh": "جَاءَ (Jaaa'a)", "penjelasan": "Mad bertemu hamzah dalam 1 kata. Dibaca panjang 4-5 harakat." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "يَنْصُرُوْنَ (Yanshuruna - dari surat lain. Di An-Nasr: أَفْوَاجًا -> Mad Iwad)", "penjelasan": "Mad Iwad pada أَفْوَاجًا (Afwaja): Tanwin fathah di akhir ayat diwaqafkan jadi panjang 2 harakat." },
      { "hukum": "Idgham Bighunnah", "contoh": "تَوَّابًا (Tawwaba - waqaf). Jika disambung Bismillah: Tawwabam-Bis...", "penjelasan": "Ghunnah pada النَّاسِ (An-Naasi) huruf Nun bertasydid." }
    ]
  },
  "111": {
    "tafsir_qna": "Al-Masad artinya Sabut. Celakanya Abu Lahab dan istrinya yang selalu menyakiti dakwah Nabi SAW.",
    "pesan_penting": "Harta tidak berguna jika hatinya benci kebaikan. Orang jahat seperti Abu Lahab akan dibalas di neraka. 🔥",
    "asbabun_nuzul": "Nabi SAW berdakwah di Bukit Shafa memanggil keluarganya. Namun sang paman, Abu Lahab, malah memaki 'Celakalah engkau hai Muhammad!'. Maka Allah membalas dengan 'Celakalah kedua tangan Abu Lahab!' 💥",
    "tajwid": [
      { "hukum": "Qalqalah Kubra", "contoh": "وَتَبَّ (Wa tabb)", "penjelasan": "Huruf Ba bertasydid di akhir ayat dibaca pantulan kuat dan ditahan sejenak." },
      { "hukum": "Idgham Bighunnah", "contoh": "لَهَبٍ وَتَبَّ (Lahabiw-watabb)", "penjelasan": "Tanwin kasrah bertemu huruf Wawu dibaca lebur mendengung." },
      { "hukum": "Idgham Bilaghunnah", "contoh": "مَالُهُ وَمَا (Maaluhuu wamaa - Mad Shilah Qashirah). Bilaghunnah: مَسَدٍ (Akhir ayat). Ikhfa: حَمَّالَةَ (Ghunnah). Contoh Ikhfa: نَارًا ذَاتَ (Naaran dzaata)", "penjelasan": "Tanwin bertemu Dzal dibaca samar mendengung." }
    ]
  },
  "112": {
    "tafsir_qna": "Al-Ikhlas artinya Memurnikan Keesaan. Surat ini mengajarkan bahwa Allah itu SATU. Tidak ada Tuhan selain Dia.",
    "pesan_penting": "Allah tidak punya anak, orang tua, atau saudara. Hanya kepada Allah kita meminta tolong! 🤲",
    "asbabun_nuzul": "Orang-orang musyrik Mekah mendatangi Nabi Muhammad SAW dan bertanya, 'Hai Muhammad, sebutkan silsilah (garis keturunan) Tuhanmu!' Maka Allah menurunkan surat ini menegaskan tidak ada yang setara dengan Allah. ✨",
    "tajwid": [
      { "hukum": "Qalqalah Kubra", "contoh": "أَحَدٌ (Ahad)", "penjelasan": "Huruf Dal di akhir ayat dibaca memantul dengan sangat kuat saat di-waqaf-kan." },
      { "hukum": "Idzhar Halqi", "contoh": "كُفُوًا أَحَدٌ (Kufuwan ahad)", "penjelasan": "Tanwin fathah bertemu huruf Hamzah/Alif dibaca sangat jelas tanpa dengung." },
      { "hukum": "Idgham Syamsiyah", "contoh": "الصَّمَدُ (Ash-Shamad)", "penjelasan": "Alif Lam bertemu huruf Shad, Lam dilebur dan tidak diucapkan." }
    ]
  },
  "113": {
    "tafsir_qna": "Al-Falaq artinya Waktu Subuh. Memohon perlindungan kepada Allah dari kejahatan malam, sihir, dan orang dengki.",
    "pesan_penting": "Orang iri hati bisa berbahaya. Baca Al-Falaq sebagai perisai perlindungan dari segala macam kejahatan. 🛡️",
    "asbabun_nuzul": "Nabi Muhammad SAW sempat sakit karena disihir oleh seorang Yahudi bernama Lubaid bin A'sham. Kemudian turunlah surat Al-Falaq & An-Nas (Al-Mu'awwidzatain) sebagai doa perlindungan dan obat. 🌙",
    "tajwid": [
      { "hukum": "Qalqalah Kubra", "contoh": "الْفَلَقِ (Al-Falaq)", "penjelasan": "Huruf Qaf di akhir ayat memantul kuat saat berhenti membaca." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "مِنْ شَرِّ (Min syarri)", "penjelasan": "Nun sukun bertemu huruf Syin dibaca samar dengan dengungan." },
      { "hukum": "Idgham Bighunnah", "contoh": "حَاسِدٍ إِذَا (Idzhar). Ghasiqin Idza (Idzhar). 'Uqodi (Qalqalah). Ikhfa di min syarri.", "penjelasan": "Idzhar Halqi pada غَاسِقٍ إِذَا (Ghasiqin idza) karena tanwin bertemu Alif dibaca jelas." }
    ]
  },
  "114": {
    "tafsir_qna": "An-Nas artinya Manusia. Memohon perlindungan kepada Allah (Raja Manusia) dari bisikan jahat iblis dan manusia.",
    "pesan_penting": "Setan selalu membisikkan niat buruk di hati kita. Baca An-Nas agar hatimu dijaga Allah dan bebas dari niat jahat. 💖",
    "asbabun_nuzul": "Diturunkan bersamaan dengan Al-Falaq sebagai doa penyembuh dan pelindung mutlak dari godaan makhluk tak kasat mata yang membisikkan niat jahat. 🕊️",
    "tajwid": [
      { "hukum": "Ghunnah Musyaddadah", "contoh": "النَّاسِ (An-Nas)", "penjelasan": "Huruf Nun bertasydid ditahan dan didengungkan selama 2 harakat." },
      { "hukum": "Idgham Syamsiyah", "contoh": "النَّاسِ (An-Nas)", "penjelasan": "Alif Lam bertemu huruf Nun, suara Lam lebur sepenuhnya." },
      { "hukum": "Ikhfa Haqiqi", "contoh": "مِنْ شَرِّ (Min syarri)", "penjelasan": "Nun sukun bertemu huruf Syin dibaca samar sambil mendengung." }
    ]
  }
}

os.makedirs('data', exist_ok=True)
with open('data/juz_amma_content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("JSON file generated successfully with expanded Tajwid.")
