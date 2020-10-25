from django.db import models

# Create your models here.


class Author(models.Model):
    autor = models.CharField(
        'Автора книги',
        max_length=200,
        blank=False,
        null=False
    )


class References(models.Model):
    name = models.CharField(
        'Название жанра',
        max_length=200,
        blank=False,
        null=False
    )

class Publisher(models.Model):
    title = models.CharField(
        'Серия',
        max_length=200,
        blank=False,
        null=False
    )

class Series(models.Model):
    title = models.CharField(
        'Серия',
        max_length=200,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.choice_text