from django.urls import path
from .views import Home, CreateArtwork, DeleteArtwork, UpdateArtwork

app_name = 'artwork'

urlpatterns = [
    path('', Home.as_view(), name='list'),
    path('artwork/create/', CreateArtwork.as_view(), name='create'),
    path('artwork/update/<int:pk>/', UpdateArtwork.as_view(), name='update'),
    path('artwork/delete/<int:pk>/', DeleteArtwork.as_view(), name='delete')
]
