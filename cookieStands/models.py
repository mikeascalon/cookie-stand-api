from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

class CookieStand(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)  # Store location as the city name
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )  # Optional owner relationship
    description = models.TextField(blank=True)  # Optional description
    hourly_sales = models.TextField(blank=True, null=True) 
    minimum_customers_per_hour = models.IntegerField(default=0)  # Optional minimum customers
    maximum_customers_per_hour = models.IntegerField(default=0)  # Optional maximum customers
    # Added field for average cookies per sale
    average_cookies_per_sale = models.FloatField(default=0)  # Average number of cookies sold per transaction

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cookiestand_detail', args=[str(self.id)])