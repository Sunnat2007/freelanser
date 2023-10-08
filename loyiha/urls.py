from django.urls import path
from . import views

urlpatterns = [
    path('' , views.base , name='base'),
    path('video-darslar/' , views.video_darslar , name='video_darslar'),
    path('korsatmalar/' , views.korsatmalar , name='korsatmalar'),
    path('darslar/<slug:slug>/', views.dars, name='dars'),
    path('vakansiyalar/' , views.vakansiyalar , name='vakansiyalar'),
    path('istedodlilar/' , views.istedodlilar , name='istedodlilar'),
    path('foydali_havolalar/' , views.foydali_havolalar , name='foydali_havolalar'),
]