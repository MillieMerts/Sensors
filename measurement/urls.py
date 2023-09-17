from django.urls import path
from .views import CreateSensor, UpdateSensor, AddMeasurement, SensorList, SensorInfo

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor/', CreateSensor.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view()),
    path('measurements/', AddMeasurement.as_view()),
    path('sensors/', SensorList.as_view()),
    path('sensor/info/<pk>/', SensorInfo.as_view())

]
