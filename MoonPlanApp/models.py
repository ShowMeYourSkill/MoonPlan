from django.db import models
from django.contrib.auth.models import User



CATEGORIES = (
    (1, "DAILY ACTIVITIES"),
    (2, "SCIENCE"),
    (3, "HOBBY"),
    (4, "SPORT"),
    (5, "MOTORSPORT"),
    (6, "COOKING"),
)

class Activity(models.Model):
    theme = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    category = models.IntegerField(choices=CATEGORIES)

    @property
    def name(self):
        return "{} {}".format(self.theme, self.description)

    def __str__(self):
        return self.name

class Groups(models.Model):
    descriptions = models.CharField(max_length=64, blank=True)
    attendees = models.ManyToManyField(Activity, blank=True)


    @property
    def name(self):
        return "{} {}".format(self.descriptions, self.attendees)

    def __str__(self):
        return self.name

class PhoneNumber(models.Model):
    number = models.CharField(max_length=64)


class Places(models.Model):
    cities = models.CharField(max_length=64, blank=True)
    numbers = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)




    @property
    def name(self):
        return "{} {}".format(self.cities, self.attendees)

    def __str__(self):
        return self.name








