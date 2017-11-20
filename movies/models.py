from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    director = models.ForeignKey(Person, related_name='directed_by')
    actors = models.ManyToManyField(Person, through='Role', null=True)
    year = models.IntegerField(null=True)

    @property
    def actors_list(self):
        return ", ".join([str(t) for t in self.actors.all()])

    @property
    def director_name(self):
        return self.director.name

    def __str__(self):
        return self.title


class Role(models.Model):
    role = models.TextField()
    movies = models.ForeignKey(Movie)
    persons = models.ForeignKey(Person)

    def __str__(self):
        return self.role
