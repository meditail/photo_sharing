from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Artwork
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
import base64
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
import os
from django.conf import settings

# Create your views here.
class Home(ListView):
    model = Artwork
    template_name = 'artwork/index.html'
    queryset = Artwork.objects.order_by('downloads')

class CreateArtwork(LoginRequiredMixin, View):
    def post(self, request): 
        title = request.POST.get('title')
        description = request.POST.get('description')
        artwork = Artwork()
        artwork.title = title
        artwork.description = description
        artwork.image = request.FILES['photo']
        artwork.creator = request.user

        artwork.save()

        return redirect('artwork:my-artworks')

class DeleteArtwork(LoginRequiredMixin, DeleteView):
    def post(self, request, pk):
        artwork = get_object_or_404(Artwork, pk=pk)
        artwork.delete()
        return redirect('artwork:my-artworks')

class Download(View):
    def get(self, request, pk):

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        print(ip)

        artwork = get_object_or_404(Artwork, pk=pk)
        artwork.downloads += 1
        artwork.save()
        path = os.path.join(settings.MEDIA_ROOT, artwork.image.path)
        
        with open(path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(path)
            response['Location'] = '/redirect/success/'
            
            return response


class MyGallery(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'artworks' : Artwork.objects.filter(creator=request.user)
        }
        return render(request, 'artwork/myGallery.html', context)

