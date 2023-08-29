from django.db import models

class Sensor(models.Model):
    """Датчики"""

    name = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=200, blank=True)


class Measurement(models.Model):
    """Измерение температуры датчике"""

    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    measurement_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.temperature, self.measurement_date