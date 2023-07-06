from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='news-home'),
    path('/prnewswire', views.index_prnewswire, name='news-home-prnewswire'),
    path('/yahoo', views.index_yahoo, name='news-home-yahoo'),
]