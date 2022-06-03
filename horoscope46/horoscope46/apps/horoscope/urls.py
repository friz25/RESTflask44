from django.urls import path

from . import views

app_name = 'horoscope'
urlpatterns = [
    path('', views.index0, name = 'index'),
    path('<int:month>/<int:day>/', views.get_info_by_date),
    path('<int:zodiac_sign>/', views.get_info_about_zodiacs_by_number),
    path('<str:zodiac_sign>/', views.get_info_about_zodiacs, name = 'horoscope-name'),
]