from django.db import models


class Ingredient(models.Model):
    name = models.CharField()
    quantity = models.IntegerField()
    measure_unit = models.CharField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField()
    tags = models.Choices(choices=['завтрак', 'обед', 'ужин'])
    ingredients = models.ManyToManyField(Ingredient)
    cooking_time = models.IntegerField()
    description = models.TextField()
    photo = models.IntegerField()

    def __str__(self):
        return self.name
