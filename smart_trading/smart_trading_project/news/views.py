from django.shortcuts import render
from .models import News

# Create your views here.
def index(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/index.html', {'news': news})

def index_prnewswire(request):
    news = News.objects.filter(source='prnewswire.com').order_by('-date')
    return render(request, 'news/index.html', {'news': news})

def index_yahoo(request):
    news = News.objects.filter(source='yahoo.com').order_by('-date')
    return render(request, 'news/index.html', {'news': news})

