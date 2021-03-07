from django.db import models

class Person(models.Model):
    g = (
        ("M", "Male"), ("F", "Female")
    )
    al = (
        ("Sedentary", "Sedentary"), ("LightlyActive", "LightlyActive"),
        ("Active", "Active"), ("HighlyActive", "HighlyActive")
    )
    height = models.PositiveIntegerField(null=True)
    weight = models.PositiveIntegerField(null=True)
    gender = models.CharField(max_length=150, choices=g)
    age = models.PositiveIntegerField()
    activityLevel = models.CharField(max_length=150, choices=al)


