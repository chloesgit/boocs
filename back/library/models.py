from django.db import models

# Create your models here.
class Author (models.Model):
    name = models.CharField(verbose_name="Nom", max_length = 100)

    def __str__(self):
        return self.name

class Book (models.Model):
    name = models.CharField(verbose_name="Nom", max_length = 100)
    description = models.CharField(verbose_name="Description", max_length = 200)
    content = models.TextField()
    active = models.BooleanField(default=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name
