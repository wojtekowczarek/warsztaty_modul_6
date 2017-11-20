from .models import Movie, Person
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'description', 'director_name', 'actors_list', 'year', 'director')

    # def create(self, data):
    #     print(data)
    #     director_id = data.pop('director')
    #     # actors_list = data.pop('actors_list')
    #     data['director'] = Person.objects.get(pk=director_id)
    #     movie = Movie.objects.create(**data)
    #     return movie


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
