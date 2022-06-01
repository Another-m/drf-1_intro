from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, MeasurementTemp


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', ]


@admin.register(MeasurementTemp)
class MeasurementTemp(admin.ModelAdmin):
    list_display = ['id', 'name_sensor', 'temperature', 'date_measure']