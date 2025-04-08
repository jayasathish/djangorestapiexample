from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    iso3 = models.CharField(max_length=3, null=True)
    numeric_code = models.CharField(max_length=3, null=True)
    iso2 = models.CharField(max_length=2, null=True)
    phonecode = models.CharField(max_length=255, null=True)
    capital = models.CharField(max_length=255, null=True)
    currency = models.CharField(max_length=255, null=True)
    currency_name = models.CharField(max_length=255, null=True)
    currency_symbol = models.CharField(max_length=255, null=True)
    tld = models.CharField(max_length=255, null=True)
    native = models.CharField(max_length=255, null=True)
    region = models.CharField(max_length=255, null=True)
    subregion = models.CharField(max_length=255, null=True)
    timezones = models.TextField()
    translations = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, null=True)
    emoji = models.CharField(max_length=191, null=True)
    emojiU = models.CharField(max_length=191, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now=True)
    flag = models.BooleanField(default=True)
    wikiDataId = models.CharField(max_length=255, null=True, db_column='wikiDataId', db_comment='Rapid API GeoDB Cities')

    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.name
