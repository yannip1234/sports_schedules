from django.urls import path
from . import views

urlpatterns = [
    path('', views.today, name='today'),
    path('week', views.week, name='week'),
    path('test', views.test),
    path('nba', views.NBA),
    path('nba/m3u', views.NBA_m3u8),
    path('mlb', views.MLB),
    path('mlb/m3u', views.MLB_m3u8)
]
