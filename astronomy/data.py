# -*- coding: utf-8 -*-
"""
Quyosh sistemasidagi sayyoralar haqidagi statik ma'lumotlar.
Har bir sayyora uchun: slug, nomi, tavsifi, fizik parametrlari va
3D ko'rinishini chizish uchun rang/uslub sozlamalari (JS tomonida ishlatiladi).
"""

PLANETS = [
    {
        "slug": "merkuriy",
        "texture": "mercury.jpg",
        "name": "Merkuriy",
        "order": 1,
        "tagline": "Quyoshga eng yaqin, eng kichik sayyora",
        "radius_km": "2 440 km",
        "distance": "57,9 mln km",
        "orbit_period": "88 kun",
        "rotation_period": "59 kun",
        "moons": "Yo'q",
        "temp": "-180°C dan +430°C gacha",
        "description": (
            "Merkuriy — Quyosh sistemasidagi eng kichik va Quyoshga eng yaqin sayyora. "
            "Uning atmosferasi deyarli yo'q, shu sababli kunduzi juda issiq, "
            "kechasi esa juda sovuq bo'ladi. Sirti Oyga o'xshab kraterlar bilan qoplangan."
        ),
        "style": "rocky",
        "base_color": "#8c8378",
        "accent_color": "#5a5148",
        "ring": False,
        "icon": "fa-solid fa-circle-dot",
    },
    {
        "slug": "venera",
        "texture": "venus.jpg",
        "name": "Venera",
        "order": 2,
        "tagline": "Quyosh sistemasidagi eng issiq sayyora",
        "radius_km": "6 052 km",
        "distance": "108,2 mln km",
        "orbit_period": "225 kun",
        "rotation_period": "243 kun (teskari)",
        "moons": "Yo'q",
        "temp": "~465°C",
        "description": (
            "Venera qalin, zaharli bulutlar bilan qoplangan bo'lib, kuchli issiqxona "
            "effekti tufayli Quyosh sistemasidagi eng issiq sayyora hisoblanadi. "
            "U o'z o'qi atrofida boshqa sayyoralarga teskari yo'nalishda aylanadi."
        ),
        "style": "rocky",
        "base_color": "#e6c27a",
        "accent_color": "#b8873f",
        "ring": False,
        "icon": "fa-solid fa-smog",
    },
    {
        "slug": "yer",
        "texture": "earth_day.jpg",
        "name": "Yer",
        "order": 3,
        "tagline": "Bizning uyimiz — hayot mavjud yagona sayyora",
        "radius_km": "6 371 km",
        "distance": "149,6 mln km",
        "orbit_period": "365,25 kun",
        "rotation_period": "24 soat",
        "moons": "1 (Oy)",
        "temp": "o'rtacha +15°C",
        "description": (
            "Yer — Quyosh sistemasida hayot mavjudligi ma'lum bo'lgan yagona sayyora. "
            "Sirtining 70% i suv bilan qoplangan, atmosferasi kislorodga boy va bitta "
            "tabiiy yo'ldoshi — Oy bor."
        ),
        "style": "earth",
        "base_color": "#2a6fb0",
        "accent_color": "#3f8f4f",
        "ring": False,
        "icon": "fa-solid fa-earth-asia",
    },
    {
        "slug": "mars",
        "texture": "mars.jpg",
        "name": "Mars",
        "order": 4,
        "tagline": "Qizil sayyora",
        "radius_km": "3 390 km",
        "distance": "227,9 mln km",
        "orbit_period": "687 kun",
        "rotation_period": "24,6 soat",
        "moons": "2 (Fobos, Deymos)",
        "temp": "~-65°C",
        "description": (
            "Mars sirtidagi temir oksidi (zang) tufayli qizg'ish rangga ega bo'lib, "
            "'Qizil sayyora' deb ataladi. Unda Quyosh sistemasidagi eng baland vulqon "
            "— Olimp tog'i joylashgan."
        ),
        "style": "rocky",
        "base_color": "#b1502f",
        "accent_color": "#7a3320",
        "ring": False,
        "icon": "fa-solid fa-mountain-sun",
    },
    {
        "slug": "yupiter",
        "texture": "jupiter.jpg",
        "name": "Yupiter",
        "order": 5,
        "tagline": "Quyosh sistemasidagi eng katta sayyora",
        "radius_km": "69 911 km",
        "distance": "778,5 mln km",
        "orbit_period": "12 yil",
        "rotation_period": "9,9 soat",
        "moons": "95+",
        "temp": "~-110°C",
        "description": (
            "Yupiter — gigant gaz sayyora bo'lib, barcha sayyoralar ichida eng kattasi. "
            "Uning mashhur Katta Qizil Dog'i — yuzlab yillardan beri davom etayotgan "
            "ulkan bo'ron."
        ),
        "style": "gas",
        "base_color": "#c9a06a",
        "accent_color": "#8a5a3a",
        "ring": False,
        "icon": "fa-solid fa-circle",
    },
    {
        "slug": "saturn",
        "texture": "saturn.jpg",
        "name": "Saturn",
        "order": 6,
        "tagline": "Ajoyib halqalari bilan mashhur",
        "radius_km": "58 232 km",
        "distance": "1 434 mln km",
        "orbit_period": "29 yil",
        "rotation_period": "10,7 soat",
        "moons": "146+",
        "temp": "~-140°C",
        "description": (
            "Saturn o'zining muz va tosh zarralaridan tashkil topgan ajoyib halqalar "
            "tizimi bilan mashhur. U shu qadar yengilki, suvga solinsa cho'kmay suzib "
            "yurgan bo'lar edi."
        ),
        "style": "gas",
        "base_color": "#d9c48a",
        "accent_color": "#a58a52",
        "ring": True,
        "ring_texture": "saturn_ring.png",
        "icon": "fa-solid fa-ring",
    },
    {
        "slug": "uran",
        "texture": "uranus.jpg",
        "name": "Uran",
        "order": 7,
        "tagline": "Yon tomonga aylanadigan sayyora",
        "radius_km": "25 362 km",
        "distance": "2 871 mln km",
        "orbit_period": "84 yil",
        "rotation_period": "17 soat",
        "moons": "27",
        "temp": "~-195°C",
        "description": (
            "Uran o'ziga xos tarzda, deyarli yon tomonga yotgan holda Quyosh atrofida "
            "aylanadi. Metan gazi uning och ko'k-yashil rangini beradi."
        ),
        "style": "gas",
        "base_color": "#8fd6e0",
        "accent_color": "#5aa3ae",
        "ring": True,
        "ring_texture": "uranus_ring.png",
        "icon": "fa-solid fa-circle-notch",
    },
    {
        "slug": "neptun",
        "texture": "neptune.jpg",
        "name": "Neptun",
        "order": 8,
        "tagline": "Quyoshdan eng uzoqdagi sayyora",
        "radius_km": "24 622 km",
        "distance": "4 495 mln km",
        "orbit_period": "165 yil",
        "rotation_period": "16 soat",
        "moons": "14",
        "temp": "~-200°C",
        "description": (
            "Neptun Quyosh sistemasidagi eng uzoq sayyora bo'lib, Quyosh sistemasidagi "
            "eng kuchli shamollarga ega — tezligi soatiga 2 000 km gacha yetadi."
        ),
        "style": "gas",
        "base_color": "#3a5fd9",
        "accent_color": "#26409e",
        "ring": False,
        "icon": "fa-solid fa-wind",
    },
]

MOON = {
    "name": "Oy",
    "texture": "moon.jpg",
    "tagline": "Yerning yagona tabiiy yo'ldoshi",
    "radius_km": "1 737 km",
    "distance": "384 400 km (Yerdan)",
    "orbit_period": "27,3 kun",
    "rotation_period": "27,3 kun (sinxron)",
    "temp": "-173°C dan +127°C gacha",
    "description": (
        "Oy — Yerning yagona tabiiy yo'ldoshi va Quyosh sistemasidagi beshinchi "
        "eng katta yo'ldosh. Uning tortishish kuchi Yerdagi dengiz sathi to'lqinlarini "
        "(prilivlarni) boshqaradi. Oy doim bir tomoni bilan Yerga qaragan holda aylanadi, "
        "shuning uchun biz uning faqat bitta yuzini ko'ramiz."
    ),
    "style": "moon",
    "base_color": "#b9b6ad",
    "accent_color": "#7d7a72",
}

EARTH = next(p for p in PLANETS if p["slug"] == "yer")


def get_planet(slug):
    for p in PLANETS:
        if p["slug"] == slug:
            return p
    return None
