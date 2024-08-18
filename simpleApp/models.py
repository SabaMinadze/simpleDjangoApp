from django.db import models

class BigBox(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.FloatField()

    def __str__(self):
        return self.firstname



class Offer(models.Model):
    code = models.CharField(max_length=10)
    desription = models.CharField(max_length=255)
    discount = models.FloatField()

    def __str__(self):
        return self.code