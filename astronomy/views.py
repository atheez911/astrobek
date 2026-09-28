from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .data import PLANETS, MOON, EARTH


def home(request):
    return render(request, 'astronomy/home.html')


def planets_list(request):
    context = {'planets': PLANETS}
    return render(request, 'astronomy/planets.html', context)


def planet_detail(request, slug):
    planet = next((p for p in PLANETS if p['slug'] == slug), None)
    if planet is None:
        raise Http404("Bunday sayyora topilmadi")
    idx = PLANETS.index(planet)
    prev_planet = PLANETS[idx - 1] if idx > 0 else PLANETS[-1]
    next_planet = PLANETS[idx + 1] if idx < len(PLANETS) - 1 else PLANETS[0]
    context = {'planet': planet, 'prev_planet': prev_planet, 'next_planet': next_planet}
    return render(request, 'astronomy/planet_detail.html', context)


def moon_view(request):
    context = {'moon': MOON}
    return render(request, 'astronomy/moon.html', context)


def earth_view(request):
    context = {'earth': EARTH}
    return render(request, 'astronomy/earth.html', context)
