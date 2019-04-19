from django.db import models

# Create your models here.
class Offer(models.Model):
    coupon_id = models.CharField(max_length=100, unique=True)
    amount = models.CharField(max_length=100, null=True, blank=True)
    offer_value = models.CharField(max_length=50, null=True, blank=True)
    verified_on = models.CharField(max_length=100, null=True, blank=True)
    product = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.amount) + " - " + str(self.offer_value)