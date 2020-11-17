from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True, null=True)

    def __str__(self):
        return f'{self.pk} {self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True, null=True)

    def __str__(self):
        return f'{self.pk} {self.name}'


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    description = models.TextField(null=True)
    genre = models.ManyToManyField(Genre, related_name='titles')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='titles')

    def __str__(self):
        return f'{self.pk} {self.name}'
