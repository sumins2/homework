from django.shortcuts import render, redirect
from .models import post
import datetime
# Create your views here.
def home(request):
    posts= post.objects.all().order_by('date')
    return render(request, 'home.html', {'posts' : posts})

def new(request):
    if request.method == 'POST':
        new_post = post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            date= request.POST['date']
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

def detail(request, name_of_pk):
    detail_of_post = post.objects.get(pk=name_of_pk)
    return render (request, 'detail.html', {'detail_of_post': detail_of_post})

def delete(request, name_of_pk):
    detail_of_post = post.objects.get(pk=name_of_pk)
    detail_of_post.delete()
    return redirect('home')

def edit(request, name_of_pk):
    detail_of_post = post.objects.get(pk=name_of_pk)
    
    if request.method == 'POST':
        post.objects.filter(pk=name_of_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            date= request.POST['date']

        )
        return redirect('detail', name_of_pk)
    return render(request, 'edit.html', {'detail_of_post':detail_of_post})