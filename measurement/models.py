from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} ({self.description})'


class MeasurementTemp(models.Model):
    name_sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='MT')
    temperature = models.IntegerField(verbose_name='Температура')
    date_measure = models.DateField(auto_now=True, verbose_name='Дата измерения')


