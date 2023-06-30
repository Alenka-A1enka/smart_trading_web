from django.shortcuts import render
from .models import CompanyPredictions
from datetime import datetime, timedelta
from portfolio.models import CustomSettings


def index(request):

    # смотрим какие компании, новостные ресурсы и алгоритмы пользователь себе добавил
    settings_bd = CustomSettings.objects.filter(user_name=request.user.username)
    settings = []
    for i in settings_bd:
        settings.append(i.company_ticker)


    current_datetime = datetime.now() - timedelta(hours=4)
    all_data = []
    for j in range(len(settings)):
        data = CompanyPredictions.objects.filter(time_release__gt=current_datetime, ticker=settings[j]).order_by('-time_release')
        all_data.append(data)

    return render(request, 'predictions/index.html', {'all_data': all_data, 'settings': settings})