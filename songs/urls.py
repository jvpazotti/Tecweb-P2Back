from django.urls import path

from . import views

urlpatterns = [
    path('', views.fav_song),
    path('favoritesBack', views.fav_list),
    path('homeDel', views.unfav),
    path('del', views.delete_fav)
]