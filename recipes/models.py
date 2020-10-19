from django.contrib.auth import get_user_model

from django.db import models


User = get_user_model()


class Ingredient(models.Model):
    name = models.CharField(max_length=15)
    quantity = models.IntegerField()
    measure_unit = models.CharField(max_length=4)

    def __str__(self):
        return self.name


# class Tag(models.Model):
#    name = models.CharField()


class Recipe(models.Model):
    tags_aviable = (
        ("Завтрак", "Завтрак"),
        ("Обед", "Обед"),
        ("Ужин", "Ужин"),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    tags = models.CharField(max_length=15, choices=tags_aviable)
    ingredients = models.ManyToManyField(Ingredient)
    cooking_time = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(upload_to='posts/', blank=True, null=True)

    def __str__(self):
        return self.name
