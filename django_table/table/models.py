from django.db import models

class Table(models.Model):
    date = models.DateField('Дата')
    name = models.CharField('Название', max_length=50)
    quantity = models.IntegerField('Количество')
    distance = models.IntegerField('Расстояние')

    def __str__(self):
        return self.name