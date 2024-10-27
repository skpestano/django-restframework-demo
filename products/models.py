from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    stock = models.PositiveBigIntegerField()

    def __str__(self) -> str:
        return self.name