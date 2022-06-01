from django.urls import path
from rest_framework.routers import DefaultRouter

from measurement.views import api, SensorViewSet, MeasuremenViewSet # , SensorView, MeasurementView, SensorsView

r = DefaultRouter()
r.register('sensor', SensorViewSet)
r.register('measurement', MeasuremenViewSet)

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('', api, name='api'),  # подключаем маршруты из приложения measurement
    # path('sensor/', SensorsView.as_view(), name='sensors'),
    # path('sensor/<pk>/', SensorView.as_view(), name='sensor'),
    # path('measurement/', MeasurementView.as_view(), name='measurement'),
] + r.urls


