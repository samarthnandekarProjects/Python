from django.db import models

class BillingOffice(models.Model):
    name = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=200)
    address_line2 = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=10)
    country = models.CharField(max_length=15)
    phoneNumber = models.CharField(max_length=10)
    email = models.CharField(max_length=15)

    class Meta:
        db_table = "billingOffice"

    def __str__(self):
        return self.name;

