from django.db import models

# Create your models here.
class Map(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to='maps/')

    def __str__(self):
        return self.name

class Building(models.Model):
    name = models.CharField(max_length=100)
    map = models.ForeignKey(Map, on_delete=models.CASCADE, related_name='buildings')
    description = models.TextField()
    picture = models.ImageField(upload_to='buildings/')

    def __str__(self):
        return self.name
    
class Floor(models.Model):
    number = models.IntegerField()
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='floors')
    description = models.TextField()
    picture = models.ImageField(upload_to='floors/')

    def __str__(self):
        return f"Floor {self.number} of {self.building.name}"
    
class Room(models.Model):
    number = models.CharField(max_length=10)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE, related_name='rooms')
    description = models.TextField()
    picture = models.ImageField(upload_to='rooms/')

    def __str__(self):
        return f"Room {self.number} on {self.floor}"