from django.db import models

class PaymentDetails(models.Model):
    name: models.CharField(max_length=50)
    card_details: models.CharField()