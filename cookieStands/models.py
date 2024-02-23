from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class CookieStand(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    cookie_sales = models.IntegerField(default=0)
    avg_cookie_per_hour = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        
        return reverse('cookiestand_detail', args=[str(self.id)])

