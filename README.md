# Koinot Sayohati — Astronomiya veb-sayti (Django)

Bu loyiha Quyosh sistemasi haqida interaktiv, 3D ko'rinishli ta'lim saytidir.
Bosh menyuda 3 ta bo'lim bor: **Sayyoralar**, **Oy** va **Yer**. Har bir
sayyora sahifasida uni sichqoncha bilan aylantirib, kattalashtirib ko'rish
mumkin (Three.js yordamida chizilgan, haqiqiy 3D sfera).

## PyCharm'da ishga tushirish

1. Ushbu papkani (`astro_koinot`) PyCharm orqali oching (File → Open).
2. Terminalni oching (pastdagi *Terminal* tab) va virtual muhit yarating:
   ```bash
   python -m venv .venv
   ```
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
3. Kerakli paketni o'rnating:
   ```bash
   pip install -r requirements.txt
   ```
4. Loyihani ishga tushiring:
   ```bash
   python manage.py runserver
   ```
5. Brauzerda oching: **http://127.0.0.1:8000/**

PyCharm avtomatik ravishda `manage.py`ni "Django" loyihasi sifatida taniydi;
shu tugma orqali ham (yashil ▶ Run tugmasi) ishga tushirsangiz bo'ladi.

## Loyiha tuzilishi

```
astro_koinot/          — Django sozlamalari (settings, urls)
astronomy/              — asosiy ilova
  data.py                — sayyoralar, Oy haqidagi ma'lumotlar (matn shu yerda tahrirlanadi)
  views.py                — sahifalarni ko'rsatuvchi funksiyalar
  urls.py                 — manzillar (/, /sayyoralar/, /oy/, /yer/ ...)
  templates/astronomy/    — HTML sahifalar
  static/astronomy/
    css/style.css          — kosmik dizayn
    js/planet3d.js          — 3D sayyoralarni chizuvchi Three.js kodi
```

## Matnni / ma'lumotlarni o'zgartirish

Har bir sayyoraning nomi, tavsifi, radiusi va boshqa faktlari
`astronomy/data.py` faylida — oddiy Python lug'atlarida joylashgan.
Shu faylni tahrirlab, matnni o'zingizga moslashtirishingiz mumkin.

## Eslatma

3D sayyoralar endi **haqiqiy fotorealistik teksturalar** (NASA va Planetary
Pixel Emporium manbalaridan olingan xaritalar) bilan chiziladi — Merkuriydan
Neptungacha, shu jumladan Saturn va Uranning halqalari va Oyning haqiqiy
krater xaritasi. Barcha rasm fayllari loyiha ichida
(`astronomy/static/astronomy/img/`) saqlanadi, shuning uchun internetga
ulanmasdan ham (faqat Three.js kutubxonasi CDN orqali yuklanadi) to'liq
ishlaydi. Ikonlar uchun Font Awesome, shriftlar uchun Google Fonts
(Orbitron, Exo 2) CDN orqali ulangan.
