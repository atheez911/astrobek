from django.urls import path
from . import views

app_name = 'astronomy'

urlpatterns = [
    path('', views.home, name='home'),
    path('sayyoralar/', views.planets_list, name='planets'),
    path('sayyoralar/<slug:slug>/', views.planet_detail, name='planet_detail'),
    path('oy/', views.moon_view, name='moon'),
    path('yer/', views.earth_view, name='earth'),
]
