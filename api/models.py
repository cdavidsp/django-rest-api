from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class FoodEntry(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    product = models.CharField(max_length=255)
    calories = models.PositiveIntegerField()
    entry_date = models.DateTimeField()
    user_id = models.ForeignKey(User, related_name='FoodEntry_user', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.product
