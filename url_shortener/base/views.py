from django.shortcuts import render, redirect

from .forms import CreateShortenedURLForm

from .helpers import generate_short_code
from .models import ShortenedURL
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    form = CreateShortenedURLForm()
    return render(request, 'base/url_form.html', context={'form': form})

def create(request):
    if request.method == 'POST':
        link = request.POST['url']
        short_code = generate_short_code()
        while True:
            if not ShortenedURL.objects.filter(short_code=short_code).exists():
                new_url = ShortenedURL(url=link, short_code=short_code)
                new_url.save()
                break
            else:
                short_code = generate_short_code()

        return HttpResponse(short_code)

def detail(request, code):
    try:
        url_object = ShortenedURL.objects.get(short_code=code)
    except ShortenedURL.DoesNotExist:
        return HttpResponseNotFound()

    return render(request, 'base/url_detail.html', context={'url_object': url_object})

def traverse(request, code):
    url_details = ShortenedURL.objects.get(short_code=code)
    return redirect(url_details.url)