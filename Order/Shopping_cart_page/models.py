from django.db import models

# Create your models here.

class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.TextField(null=True, blank=True, default='')
    user_number = models.IntegerField(null=True, blank=True, default=380000000000)
