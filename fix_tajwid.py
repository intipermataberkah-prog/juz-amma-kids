import json

with open('data/juz_amma_content.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Clean tajwid data - replace messy entries with clean ones
clean = {
"78": [
  {"hukum":"Ghunnah Musyaddadah","contoh":"عَمَّ ('Amma)","penjelasan":"Mim bertasydid didengungkan 2 harakat."},
  {"hukum":"Idgham Bighunnah","contoh":"سِرَاجًا وَهَّاجًا (Sirajaw-wahhaja)","penjelasan":"Tanwin bertemu Wawu, masuk dengan dengung."},
  {"hukum":"Qalqalah Sughra","contoh":"نَجْعَلِ (Naj'ali)","penjelasan":"Jim sukun di tengah kata memantul tipis."}
],
"79": [
  {"hukum":"Mad Thobi'i","contoh":"وَالنَّازِعَاتِ (Wan-nazi'ati)","penjelasan":"Alif setelah fathah panjang 2 harakat."},
  {"hukum":"Ikhfa Haqiqi","contoh":"يَنْظُرُ (Yanzhuru)","penjelasan":"Nun sukun bertemu Zha, samar mendengung."},
  {"hukum":"Idzhar Halqi","contoh":"عَنْهَا ('Anha)","penjelasan":"Nun sukun bertemu Ha, jelas tanpa dengung."}
],
"80": [
  {"hukum":"Qalqalah Sughra","contoh":"يَدْرِيْكَ (Yad-rika)","penjelasan":"Dal sukun di tengah memantul tipis."},
  {"hukum":"Idgham Bilaghunnah","contoh":"مَتَاعًا لَكُمْ (Mata'al-lakum)","penjelasan":"Tanwin bertemu Lam, masuk tanpa dengung."},
  {"hukum":"Iqlab","contoh":"كِرَامٍ بَرَرَةٍ (Kiromim bararah)","penjelasan":"Tanwin bertemu Ba, berubah jadi Mim dengung."}
],
"81": [
  {"hukum":"Idgham Bighunnah","contoh":"نَفْسٌ مَا (Nafsum-ma)","penjelasan":"Tanwin bertemu Mim, masuk dengan dengung."},
  {"hukum":"Idzhar Qamariyah","contoh":"الْجِبَالُ (Al-Jibalu)","penjelasan":"Alif Lam bertemu Jim, Lam dibaca jelas."},
  {"hukum":"Mad Wajib Muttashil","contoh":"شَاءَ (Syaaa'a)","penjelasan":"Mad bertemu hamzah dalam 1 kata, panjang 4-5 harakat."}
],
"82": [
  {"hukum":"Ikhfa Haqiqi","contoh":"إِنْفَطَرَتْ (Infatharat)","penjelasan":"Nun sukun bertemu Fa, samar mendengung."},
  {"hukum":"Idgham Syamsiyah","contoh":"السَّمَاءُ (As-Samaa'u)","penjelasan":"Alif Lam bertemu Sin, Lam lebur ke Sin."},
  {"hukum":"Mad 'Aridh Lissukun","contoh":"تَعْلَمُوْنَ (Ta'lamun)","penjelasan":"Mad di akhir ayat saat waqaf, panjang 2-6 harakat."}
],
"83": [
  {"hukum":"Mad 'Aridh Lissukun","contoh":"لِلْمُطَفِّفِيْنَ (Lil-muthoffifin)","penjelasan":"Mad di akhir ayat saat waqaf, panjang 2-6 harakat."},
  {"hukum":"Ikhfa Syafawi","contoh":"كُنْتُمْ بِهِ (Kuntum bihi)","penjelasan":"Mim sukun bertemu Ba, samar di bibir."},
  {"hukum":"Ghunnah","contoh":"إِنَّ (Inna)","penjelasan":"Nun bertasydid didengungkan 2 harakat."}
],
"84": [
  {"hukum":"Ikhfa Haqiqi","contoh":"اِنْشَقَّتْ (Insyaqqat)","penjelasan":"Nun sukun bertemu Syin, samar mendengung."},
  {"hukum":"Idgham Bilaghunnah","contoh":"أَنْ لَنْ (Al-lan)","penjelasan":"Nun sukun bertemu Lam, masuk tanpa dengung."},
  {"hukum":"Mad Jaiz Munfashil","contoh":"إِلَى أَهْلِهِ (Ilaaa ahlihi)","penjelasan":"Mad bertemu hamzah di kata berbeda, 4-5 harakat."}
],
"85": [
  {"hukum":"Qalqalah Kubra","contoh":"الْبُرُوْجِ (Al-Buruj)","penjelasan":"Jim di akhir ayat memantul kuat saat waqaf."},
  {"hukum":"Idzhar Syafawi","contoh":"هُمْ عَلَيْهَا (Hum 'alaiha)","penjelasan":"Mim sukun bertemu 'Ain, jelas tanpa dengung."},
  {"hukum":"Ghunnah","contoh":"إِنَّ (Inna)","penjelasan":"Nun bertasydid didengungkan 2 harakat."}
],
"86": [
  {"hukum":"Qalqalah Kubra","contoh":"الثَّاقِبُ (Ats-Tsaqib)","penjelasan":"Ba di akhir ayat memantul kuat saat waqaf."},
  {"hukum":"Idgham Bilaghunnah","contoh":"نَفْسٍ لَمَّا (Nafsil-lamma)","penjelasan":"Tanwin bertemu Lam, melebur tanpa dengung."},
  {"hukum":"Ikhfa Haqiqi","contoh":"مِنْ صُلْبِ (Min shulbi)","penjelasan":"Nun sukun bertemu Shad, samar mendengung."}
],
"87": [
  {"hukum":"Mad Thobi'i","contoh":"الْأَعْلَى (Al-A'la)","penjelasan":"Alif layyinah di akhir panjang 2 harakat."},
  {"hukum":"Qalqalah Sughra","contoh":"سُبْحَانَ (Sub-hana)","penjelasan":"Ba sukun di tengah memantul tipis."},
  {"hukum":"Idzhar Halqi","contoh":"غُثَاءً أَحْوَى (Ghutsaa-an ahwa)","penjelasan":"Tanwin bertemu Hamzah, jelas tanpa dengung."}
],
"88": [
  {"hukum":"Idgham Bighunnah","contoh":"وُجُوْهٌ يَّوْمَئِذٍ (Wujuhuy-yauma'idzin)","penjelasan":"Tanwin bertemu Ya, masuk berdengung."},
  {"hukum":"Ikhfa Haqiqi","contoh":"مِنْ جُوْعٍ (Min juu')","penjelasan":"Nun sukun bertemu Jim, samar mendengung."},
  {"hukum":"Idzhar Syafawi","contoh":"إِيَابَهُمْ ثُمَّ (Iyaabahum tsumma)","penjelasan":"Mim sukun bertemu Tsa, jelas di bibir."}
],
"89": [
  {"hukum":"Qalqalah Sughra","contoh":"وَالْفَجْرِ (Wal-Fajr)","penjelasan":"Jim sukun di tengah memantul tipis."},
  {"hukum":"Mad Jaiz Munfashil","contoh":"كَلَّا إِذَا (Kallaaa idzaa)","penjelasan":"Mad bertemu hamzah di kata berbeda, 4-5 harakat."},
  {"hukum":"Ikhfa Syafawi","contoh":"رَبُّهُمْ بِعَذَابٍ (Rabbuhum bi'adzab)","penjelasan":"Mim sukun bertemu Ba, samar mendengung."}
],
"90": [
  {"hukum":"Ikhfa Haqiqi","contoh":"إِنْسَانَ (Insana)","penjelasan":"Nun sukun bertemu Sin, samar mendengung."},
  {"hukum":"Idgham Bighunnah","contoh":"وَّالِدٍ وَّمَا (Wa lidiw-wamaa)","penjelasan":"Tanwin bertemu Wawu, masuk berdengung."},
  {"hukum":"Qalqalah Kubra","contoh":"الْبَلَدِ (Al-Balad)","penjelasan":"Dal di akhir ayat memantul kuat saat waqaf."}
],
"91": [
  {"hukum":"Ghunnah Musyaddadah","contoh":"إِنَّ (Inna)","penjelasan":"Nun bertasydid didengungkan 2 harakat."},
  {"hukum":"Idgham Syamsiyah","contoh":"الشَّمْسِ (Asy-Syamsi)","penjelasan":"Alif Lam bertemu Syin, Lam dilebur."},
  {"hukum":"Mad Thobi'i","contoh":"ضُحَاهَا (Dhuhaahaa)","penjelasan":"Fathah bertemu Alif, panjang 2 harakat."}
],
"92": [
  {"hukum":"Idgham Bighunnah","contoh":"وَمَنْ يَّبْخَلْ (Wamay-yabkhal)","penjelasan":"Nun sukun bertemu Ya, masuk berdengung."},
  {"hukum":"Idzhar Halqi","contoh":"مَنْ أَعْطَى (Man a'tha)","penjelasan":"Nun sukun bertemu Hamzah, jelas tanpa dengung."},
  {"hukum":"Qalqalah Sughra","contoh":"يَبْخَلْ (Yabkhal)","penjelasan":"Ba sukun di tengah memantul tipis."}
],
"93": [
  {"hukum":"Mad Thobi'i","contoh":"الضُّحَى (Ad-Dhuha)","penjelasan":"Alif layyinah di akhir panjang 2 harakat."},
  {"hukum":"Qalqalah Sughra","contoh":"لَمْ يَجِدْكَ (Lam yajidka)","penjelasan":"Dal sukun di tengah memantul tipis."},
  {"hukum":"Ghunnah","contoh":"فَأَمَّا (Fa'ammaa)","penjelasan":"Mim bertasydid didengungkan 2 harakat."}
],
"94": [
  {"hukum":"Idzhar Syafawi","contoh":"أَلَمْ نَشْرَحْ (Alam Nasyrah)","penjelasan":"Mim sukun bertemu Nun, jelas di bibir."},
  {"hukum":"Ikhfa Haqiqi","contoh":"عَنْكَ (Anka)","penjelasan":"Nun sukun bertemu Kaf, samar mendengung."},
  {"hukum":"Qalqalah Sughra","contoh":"أَنْقَضَ (Anqadha)","penjelasan":"Qaf sukun di tengah memantul tipis."}
],
"95": [
  {"hukum":"Idgham Syamsiyah","contoh":"وَالتِّيْنِ (Wat-Tini)","penjelasan":"Alif Lam bertemu Ta, Lam dilebur ke Ta."},
  {"hukum":"Ikhfa Haqiqi","contoh":"إِنْسَانَ (Insana)","penjelasan":"Nun sukun bertemu Sin, samar mendengung."},
  {"hukum":"Qalqalah Sughra","contoh":"لَقَدْ (Laqad)","penjelasan":"Dal sukun di tengah memantul tipis."}
],
"96": [
  {"hukum":"Qalqalah Kubra","contoh":"عَلَقٍ ('Alaq)","penjelasan":"Qaf di akhir ayat memantul sangat kuat."},
  {"hukum":"Idzhar Halqi","contoh":"مِنْ عَلَقٍ (Min 'alaq)","penjelasan":"Nun sukun bertemu 'Ain, jelas tanpa dengung."},
  {"hukum":"Qalqalah Sughra","contoh":"اِقْرَأْ (Iqra')","penjelasan":"Qaf sukun di tengah memantul tipis."}
],
"97": [
  {"hukum":"Qalqalah Sughra","contoh":"الْقَدْرِ (Al-Qadr)","penjelasan":"Dal sukun di tengah memantul tipis."},
  {"hukum":"Idgham Bighunnah","contoh":"خَيْرٌ مِنْ (Khairum-min)","penjelasan":"Tanwin bertemu Mim, masuk berdengung."},
  {"hukum":"Ikhfa Haqiqi","contoh":"مِنْ كُلِّ (Min kulli)","penjelasan":"Nun sukun bertemu Kaf, samar mendengung."}
],
"98": [
  {"hukum":"Idgham Bighunnah","contoh":"رَسُوْلٌ مِّنَ (Rasulum-mina)","penjelasan":"Tanwin bertemu Mim, masuk berdengung."},
  {"hukum":"Idzhar Halqi","contoh":"مِنْ أَهْلِ (Min ahli)","penjelasan":"Nun sukun bertemu Hamzah, jelas tanpa dengung."},
  {"hukum":"Ikhfa Haqiqi","contoh":"عِنْدَ ('Inda)","penjelasan":"Nun sukun bertemu Dal, samar mendengung."}
],
"99": [
  {"hukum":"Idgham Bighunnah","contoh":"مَنْ يَّعْمَلْ (May-ya'mal)","penjelasan":"Nun sukun bertemu Ya, masuk berdengung."},
  {"hukum":"Ikhfa Haqiqi","contoh":"يَوْمَئِذٍ تُحَدِّثُ (Yauma'idzin tuhadditsu)","penjelasan":"Tanwin bertemu Ta, samar mendengung."},
  {"hukum":"Idzhar Halqi","contoh":"ذَرَّةٍ خَيْرًا (Dzarratin khairan)","penjelasan":"Tanwin bertemu Kha, jelas tanpa dengung."}
],
"100": [
  {"hukum":"Qalqalah Sughra","contoh":"ضَبْحًا (Dhab-han)","penjelasan":"Ba sukun di tengah memantul tipis."},
  {"hukum":"Ghunnah","contoh":"إِنَّ (Inna)","penjelasan":"Nun bertasydid didengungkan 2 harakat."},
  {"hukum":"Ikhfa Syafawi","contoh":"رَبَّهُمْ بِهِمْ (Rabbahum bihim)","penjelasan":"Mim sukun bertemu Ba, samar di bibir."}
],
"101": [
  {"hukum":"Idgham Bilaghunnah","contoh":"عِيْشَةٍ رَّاضِيَةٍ ('Isyatar-radhiyah)","penjelasan":"Tanwin bertemu Ra, masuk tanpa dengung."},
  {"hukum":"Ikhfa Haqiqi","contoh":"مَنْ ثَقُلَتْ (Man tsaqulat)","penjelasan":"Nun sukun bertemu Tsa, samar mendengung."},
  {"hukum":"Idzhar Halqi","contoh":"نَارٌ حَامِيَةٌ (Naarun Hamiyah)","penjelasan":"Tanwin bertemu Ha, jelas tanpa dengung."}
],
"102": [
  {"hukum":"Ghunnah Musyaddadah","contoh":"ثُمَّ (Tsumma)","penjelasan":"Mim bertasydid didengungkan 2 harakat."},
  {"hukum":"Idzhar Halqi","contoh":"عَنْ (An)","penjelasan":"Nun sukun bertemu 'Ain, jelas tanpa dengung."},
  {"hukum":"Mad Thobi'i","contoh":"تَكَاثُرُ (Takatsuru)","penjelasan":"Fathah bertemu Alif, panjang 2 harakat."}
],
"103": [
  {"hukum":"Mad Thobi'i","contoh":"الَّذِيْنَ (Alladzina)","penjelasan":"Kasrah diikuti Ya sukun, panjang 2 harakat."},
  {"hukum":"Idzhar Qamariyah","contoh":"وَالْعَصْرِ (Wal-'Ashr)","penjelasan":"Alif Lam bertemu 'Ain, Lam jelas."},
  {"hukum":"Ikhfa Haqiqi","contoh":"الْإِنْسَانَ (Al-Insana)","penjelasan":"Nun sukun bertemu Sin, samar mendengung."}
],
"104": [
  {"hukum":"Iqlab","contoh":"لَيُنْبَذَنَّ (Layumbadzanna)","penjelasan":"Nun sukun bertemu Ba, berubah jadi Mim dengung."},
  {"hukum":"Idgham Bighunnah","contoh":"مَالًا وَعَدَّدَهُ (Maalaw-wa'addadah)","penjelasan":"Tanwin bertemu Wawu, masuk berdengung."},
  {"hukum":"Ghunnah","contoh":"لَيُنْبَذَنَّ (Layumbadzanna)","penjelasan":"Nun bertasydid di akhir didengungkan 2 harakat."}
],
"105": [
  {"hukum":"Idzhar Syafawi","contoh":"أَلَمْ تَرَ (Alam tara)","penjelasan":"Mim sukun bertemu Ta, jelas tanpa dengung."},
  {"hukum":"Ikhfa Syafawi","contoh":"تَرْمِيْهِمْ بِحِجَارَةٍ (Tarmihim bihijarah)","penjelasan":"Mim sukun bertemu Ba, samar mendengung."},
  {"hukum":"Idgham Bighunnah","contoh":"بِحِجَارَةٍ مِنْ (Bihijaratim-min)","penjelasan":"Tanwin bertemu Mim, masuk berdengung."}
],
"106": [
  {"hukum":"Mad Lin","contoh":"قُرَيْشٍ (Quraisy)","penjelasan":"Waqaf pada huruf didahului Ya sukun setelah fathah."},
  {"hukum":"Idzhar Syafawi","contoh":"إِيْلَافِهِمْ رِحْلَةَ (Ilafihim rihlah)","penjelasan":"Mim sukun bertemu Ra, jelas di bibir."},
  {"hukum":"Idgham Mimi","contoh":"أَطْعَمَهُمْ مِنْ (Ath'amahum-min)","penjelasan":"Mim sukun bertemu Mim, lebur mendengung."}
],
"107": [
  {"hukum":"Mad 'Aridh Lissukun","contoh":"لِلْمُصَلِّيْنَ (Lil-mushollin)","penjelasan":"Mad di akhir ayat saat waqaf, panjang 2-6 harakat."},
  {"hukum":"Idzhar Syafawi","contoh":"هُمْ عَنْ (Hum 'an)","penjelasan":"Mim sukun bertemu 'Ain, jelas di bibir."},
  {"hukum":"Ikhfa Haqiqi","contoh":"عَنْ صَلَاتِهِمْ ('An shalatihim)","penjelasan":"Nun sukun bertemu Shad, samar mendengung."}
],
"108": [
  {"hukum":"Ghunnah Musyaddadah","contoh":"إِنَّا (Inna)","penjelasan":"Nun bertasydid didengungkan 2 harakat."},
  {"hukum":"Idzhar Qamariyah","contoh":"الْكَوْثَرَ (Al-Kautsar)","penjelasan":"Alif Lam bertemu Kaf, Lam jelas."},
  {"hukum":"Qalqalah Sughra","contoh":"أَبْتَرُ (Ab-tar)","penjelasan":"Ba sukun di tengah memantul tipis."}
],
"109": [
  {"hukum":"Mad Jaiz Munfashil","contoh":"لَا أَعْبُدُ (Laa a'budu)","penjelasan":"Mad bertemu hamzah di kata berbeda, 4-5 harakat."},
  {"hukum":"Ikhfa Haqiqi","contoh":"أَنْتُمْ (Antum)","penjelasan":"Nun sukun bertemu Ta, samar mendengung."},
  {"hukum":"Idzhar Syafawi","contoh":"لَكُمْ دِيْنُكُمْ (Lakum dinukum)","penjelasan":"Mim sukun bertemu Dal, jelas di bibir."}
],
"110": [
  {"hukum":"Mad Wajib Muttashil","contoh":"جَاءَ (Jaaa'a)","penjelasan":"Mad bertemu hamzah dalam 1 kata, panjang 4-5 harakat."},
  {"hukum":"Mad Iwad","contoh":"أَفْوَاجًا (Afwaja)","penjelasan":"Tanwin fathah di akhir ayat saat waqaf, panjang 2 harakat."},
  {"hukum":"Ghunnah","contoh":"النَّاسِ (An-Naasi)","penjelasan":"Nun bertasydid didengungkan 2 harakat."}
],
"111": [
  {"hukum":"Qalqalah Kubra","contoh":"وَتَبَّ (Wa tabb)","penjelasan":"Ba bertasydid di akhir ayat memantul kuat."},
  {"hukum":"Idgham Bighunnah","contoh":"لَهَبٍ وَتَبَّ (Lahabiw-watabb)","penjelasan":"Tanwin bertemu Wawu, masuk berdengung."},
  {"hukum":"Ikhfa Haqiqi","contoh":"نَارًا ذَاتَ (Naaran dzaata)","penjelasan":"Tanwin bertemu Dzal, samar mendengung."}
],
"112": [
  {"hukum":"Qalqalah Kubra","contoh":"أَحَدٌ (Ahad)","penjelasan":"Dal di akhir ayat memantul sangat kuat saat waqaf."},
  {"hukum":"Idzhar Halqi","contoh":"كُفُوًا أَحَدٌ (Kufuwan ahad)","penjelasan":"Tanwin bertemu Hamzah, jelas tanpa dengung."},
  {"hukum":"Idgham Syamsiyah","contoh":"الصَّمَدُ (Ash-Shamad)","penjelasan":"Alif Lam bertemu Shad, Lam dilebur."}
],
"113": [
  {"hukum":"Qalqalah Kubra","contoh":"الْفَلَقِ (Al-Falaq)","penjelasan":"Qaf di akhir ayat memantul kuat saat waqaf."},
  {"hukum":"Ikhfa Haqiqi","contoh":"مِنْ شَرِّ (Min syarri)","penjelasan":"Nun sukun bertemu Syin, samar mendengung."},
  {"hukum":"Idzhar Halqi","contoh":"غَاسِقٍ إِذَا (Ghasiqin idza)","penjelasan":"Tanwin bertemu Hamzah, jelas tanpa dengung."}
],
"114": [
  {"hukum":"Ghunnah Musyaddadah","contoh":"النَّاسِ (An-Nas)","penjelasan":"Nun bertasydid didengungkan 2 harakat."},
  {"hukum":"Idgham Syamsiyah","contoh":"النَّاسِ (An-Nas)","penjelasan":"Alif Lam bertemu Nun, Lam lebur sepenuhnya."},
  {"hukum":"Ikhfa Haqiqi","contoh":"مِنْ شَرِّ (Min syarri)","penjelasan":"Nun sukun bertemu Syin, samar mendengung."}
]
}

for k, v in clean.items():
    if k in data:
        data[k]["tajwid"] = v

with open('data/juz_amma_content.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# Also regenerate JS version
with open('data/juz_amma_content.json', 'r', encoding='utf-8') as f:
    raw = f.read()
with open('data/juz_amma_content.js', 'w', encoding='utf-8') as f:
    f.write('const juzAmmaData = ' + raw + ';')

print("Tajwid data cleaned and saved!")
