from django.urls import path
from measurement.views import MeasurementView, SensorView, SensorUpdateView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('measurements/', MeasurementView.as_view()),
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorUpdateView.as_view()),
]