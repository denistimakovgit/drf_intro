from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer

class SensorView(ListCreateAPIView):
    """создание датчика, получение датчиков (GET, POST)"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdateView(RetrieveUpdateAPIView):
    """ получение информации по датчику, обновление датчика (PATCH, GET) """
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

class MeasurementView(ListCreateAPIView):
    """Внесение данных измерения (POST) """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer