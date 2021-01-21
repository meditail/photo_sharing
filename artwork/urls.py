from django.urls import path
from .views import Home, CreateArtwork, DeleteArtwork, MyGallery, Download

app_name = 'artwork'

urlpatterns = [
    path('', Home.as_view(), name='list'),
    path('artwork/create/', CreateArtwork.as_view(), name='create'),
    path('artwork/myartworks/', MyGallery.as_view(), name='my-artworks'),
    path('artwork/delete/<int:pk>/', DeleteArtwork.as_view(), name='delete'),
    path('artwork/download/<int:pk>/', Download.as_view(), name='download')
]
