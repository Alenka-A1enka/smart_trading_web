from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='portfolio-home'),
    path('add_company', views.add_company, name='portfolio-add'),
    path('<int:pk>', views.CompanyDetailView.as_view(), name='company-detail'),
    path('<int:pk>/delete', views.CompanyDeleteView.as_view(), name='company-delete'),
]