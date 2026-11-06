from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='drivers')
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.number})"