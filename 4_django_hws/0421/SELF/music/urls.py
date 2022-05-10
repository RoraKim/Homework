from django.urls import path, include
from . import views

app_name = 'artists'
urlpatterns = [
    path('artists/', views.artist_list_create, name='artist_list_create'),
    # path('artists/create', views.artist_create, name='artist_create'),
    path('artists/<int:artist_pk>/', views.artist_detail, name='artist_detail')
]
