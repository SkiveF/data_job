from django.db import models


class CovidStatsRegion(models.Model):
    iso = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.iso} - {self.name}"


class CovidStats(models.Model):
    country = models.CharField(max_length=100)
    date = models.DateField()
    confirmed_cases = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    recovered = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.country} - {self.date}"
