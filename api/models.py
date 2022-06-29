from django.db import models

# Create your models here.
from django.db import models


class FoodEntry(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()
    created_date = models.DateTimeField()

    def __str__(self):
        return self.product
