# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import redirect, render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from .serializers import SensorSerializer, MeasurementSerializer

from measurement.models import Sensor, MeasurementTemp


def index(request):
    return redirect('api')

def api(request):
    template = 'index.html'
    return render(request, template)




class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasuremenViewSet(ModelViewSet):
    queryset = MeasurementTemp.objects.all()
    serializer_class = MeasurementSerializer