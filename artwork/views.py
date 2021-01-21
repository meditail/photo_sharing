from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Artwork
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
import base64

# Create your views here.
class Home(ListView):
    model = Artwork
    template_name = 'artwork/index.html'

class CreateArtwork(View):
    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        artwork = Artwork()
        artwork.title = title
        artwork.description = description
        artwork.image = request.FILES['photo']

        artwork.save()

        return redirect('artwork:list')

class UpdateArtwork(UpdateView):
    model = Artwork
    fields = ['title', 'description', 'downloads']

class DeleteArtwork(DeleteView):
    model = Artwork
    success_url = reverse_lazy('artwork:home')

class Download(View):
    pass
