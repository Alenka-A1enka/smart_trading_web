from django.db import models

# News, Resources
class News(models.Model):
    header = models.TextField('Заголовок статьи', max_length=500)
    annotation = models.TextField('Аннотация', max_length=1000, default='')
    date = models.DateTimeField('Дата и время публикации')
    source = models.CharField('Новостной источник')
    company_name = models.CharField('Название компании')

    def __str__(self):
        return f'{self.header} {self.date} ({self.source}, {self.company_name})'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Resources(models.Model):
    source = models.CharField('Новостной ресурс')

    def __str__(self):
        return f'{self.source}'

    class Meta:
        verbose_name = 'Новостной ресурс'
        verbose_name_plural = 'Новостные ресурсы'