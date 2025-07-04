from django.db import models

# Create your models here.
class Load(models.Model):
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    pickup_date = models.DateField()
    delivery_date = models.DateField()
    weight_lbs = models.IntegerField()
    distance_miles = models.IntegerField()
    rate_usd = models.DecimalField(max_digits=10, decimal_places=2)
    equipment_type = models.CharField(max_length=50)
    broker = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.origin} → {self.destination} (${self.rate_usd})"