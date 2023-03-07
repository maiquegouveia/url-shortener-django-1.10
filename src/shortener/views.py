from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            'title': 'URL.co',
            'form': the_form,
        }
        return render(request, 'shortener/home.html', context)
    
    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data.get('url'))
        
        context = {
            'title': 'URL.co',
            'form': form,
        }
        return render(request, 'shortener/home.html', context)
    
    
class KirrCBView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)