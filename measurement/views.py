# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer

class GetCreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class GetUpdateSensor(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class AddMeasurement(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
