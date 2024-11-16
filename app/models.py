from django.db import models

# Create your models here.

class Flavor(models.Model):
    name = models.CharField(max_length=100, unique=True)
    season = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class CustomerSuggestion(models.Model):
    flavor_suggestion = models.CharField(max_length=100)
    allergy_concern = models.TextField(default="No allergy concerns")

    def __str__(self):
        return self.flavor_suggestion
