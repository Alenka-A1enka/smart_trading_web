from django.db import models


class CompanyPredictions(models.Model):
    ticker = models.CharField('Тикер компании')
    company_name = models.CharField('Название компании')
    time_release = models.DateTimeField('Время выхода новости')
    time_stop = models.DateTimeField('Время окончания прогноза')
    source = models.CharField('Источник')
    header = models.TextField('Заголовок статьи', max_length=500)
    annotation = models.TextField('Аннотация', max_length=1000, default='')
    prediction = models.TextField('Прогноз')

    #id, тикер, название компании, время выхода, время остановки, источник, заголовок, аннотация, прогноз


    def __str__(self):
        return f'{self.prediction} {self.time_stop}'

    class Meta:
        verbose_name = 'Прогноз'
        verbose_name_plural = 'Прогнозы'