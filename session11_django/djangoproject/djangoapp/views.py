from django.shortcuts import render, redirect
from .models import text
import datetime
# Create your views here.
def index(request):
    movie_count = text.objects.filter(category='movie').count()
    drama_count = text.objects.filter(category='drama').count()
    entertain_count = text.objects.filter(category='entertain').count()
    return render(request, 'index.html', {
    'movie_count' : movie_count,
    'drama_count' : drama_count,
    'entertain_count' : entertain_count
    })

def movie(request):
    movie_title = text.objects.filter(category='movie')
    return render(request, 'movie.html', {'movie_title': movie_title})

def drama(request):
    drama_title = text.objects.filter(category='drama')
    return render(request, 'drama.html', {'drama_title': drama_title})

def entertain(request):
    entertain_title = text.objects.filter(category='entertain')
    return render(request, 'entertain.html', {'entertain_title': entertain_title})

def detail(request, primary_key):
    detail_info = text.objects.get(pk=primary_key)
    return render(request, 'detail.html', {'detail_info' : detail_info})

def new(request):
    if request.method == 'POST' :
        new_text = text.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
            time = datetime.datetime.now(),
        )
        return redirect('detail', primary_key = new_text.pk)

    else :
        return render(request, 'new.html')
    