from django.db import models

class NeuroMethods(models.Model):
    method_name = models.CharField('Название метода')

    def __str__(self):
        return f'{self.method_name}'

    class Meta:
        verbose_name = 'Метод'
        verbose_name_plural = 'Методы'

class TimeLaps(models.Model):
    time_value = models.CharField('Временной промежуток')

    def __str__(self):
        return f'{self.time_value})'

    class Meta:
        verbose_name = 'Временной промежуток'
        verbose_name_plural = 'Временные промежутки'

class Companies(models.Model):
    ticker = models.CharField('Тикер компании', unique=True)
    company_name = models.CharField('Название компании')

    def __str__(self):
        return f'{self.company_name} ({self.ticker})'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

class CustomSettings(models.Model):
    user_name = models.CharField('Логин пользователя')
    company_ticker = models.CharField('Тикер компании')
    company_name = models.CharField('Название компании', default='company')
    neuro_methods_list = models.TextField('Список методов для данной компании', default='Нейросетевой анализ,Семантический анализ')
    time_laps_list = models.CharField('Список временных промежутков')
    news_source_list = models.TextField('Список новостных ресурсов для парсинга', default='prnewswire.com,yahoo.com')

    def __str__(self):
        return f'{self.user_name}: {self.company_ticker} ({self.neuro_methods_list}, {self.time_laps_list})'

    class Meta:
        verbose_name = 'Настройки пользователя'
        verbose_name_plural = 'Настройки пользователей'
        unique_together = ('user_name', 'company_ticker')