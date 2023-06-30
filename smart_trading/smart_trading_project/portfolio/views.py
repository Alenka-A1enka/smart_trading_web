from django.shortcuts import render, redirect
from .models import CustomSettings, Companies, NeuroMethods, TimeLaps
from news.models import Resources
from django.contrib.auth.models import User
from .forms import CustomSettingsForm
from django.views.generic import DetailView, DeleteView

# Create your views here.
def index(request):
    tickers = CustomSettings.objects.filter(user_name = request.user.username).order_by('company_ticker')

    return render(request, 'portfolio/index.html', {'tickers': tickers})

class CompanyDeleteView(DeleteView):
    model = CustomSettings
    success_url = '/portfolio/'
    template_name = 'portfolio/companydelete_view.html'


class CompanyDetailView(DetailView):
    model = CustomSettings
    template_name = 'portfolio/companydetails_view.html'
    context_object_name = 'companies'

def add_company(request):
    error = ''
    if request.method == 'POST':
        form = CustomSettingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portfolio-home')
        else:
            error = 'Компания ранее уже была добавлена'

    companies = Companies.objects.order_by('ticker')
    methods = NeuroMethods.objects.order_by('method_name')
    times = TimeLaps.objects.all()
    sources = Resources.objects.order_by('source')

    form = CustomSettingsForm()

    return render(request, 'portfolio/add_company.html', {'companies': companies, 'methods': methods,
                                                          'times': times, 'sources': sources, 'form': form,
                                                          'error': error})

