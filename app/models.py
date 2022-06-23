from django.db import models

# Create your models here.
class Rickshaw(models.Model):
    destination=models.CharField(max_length=200)
    fare=models.IntegerField()
    time=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()



class Bus(models.Model):
    destination=models.CharField(max_length=200)
    fare=models.IntegerField()
    time=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()



class Van(models.Model):
    destination=models.CharField(max_length=200)
    fare=models.IntegerField()
    time=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    phone=models.IntegerField()

    
