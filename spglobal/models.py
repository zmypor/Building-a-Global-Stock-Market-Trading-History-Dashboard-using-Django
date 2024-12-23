from django.db import models

class SPGlobalIndex(models.Model):
    index_id = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    constituents = models.IntegerField()
    value = models.FloatField()
    market_cap = models.FloatField(null=True, blank=True)
    divisor = models.FloatField(null=True, blank=True)
    daily_return = models.FloatField()
    dividend = models.FloatField(null=True, blank=True)
    adjusted_market_cap = models.FloatField(null=True, blank=True)
    adjusted_divisor = models.FloatField(null=True, blank=True)
    adjusted_constituents = models.IntegerField()
    currency_code = models.CharField(max_length=10)
    currency_name = models.CharField(max_length=50)
    currency_symbol = models.CharField(max_length=10)
    last_update = models.DateField()

    def __str__(self):
        return self.name


class IndexConstituent(models.Model):
    index = models.ForeignKey(
        SPGlobalIndex, on_delete=models.CASCADE, related_name="components"
    )
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    sector = models.CharField(max_length=50)
    industry = models.CharField(max_length=100)
    weight = models.FloatField()

    def __str__(self):
        return self.name

# Create your models here.
