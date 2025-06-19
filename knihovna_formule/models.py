from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    founded_year = models.PositiveIntegerField()
    image = models.ImageField(upload_to='teams/', blank=True, null=True)

    def __str__(self):
        return self.name

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)  
    wins = models.PositiveIntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='drivers/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Track(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    length_km = models.DecimalField(max_digits=5, decimal_places=3)
    image = models.ImageField(upload_to='tracks/', blank=True, null=True)

    def __str__(self):
        return self.name

class GrandPrix(models.Model):
    name = models.CharField(max_length=100)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.date.strftime('%Y-%m-%d')})" 
