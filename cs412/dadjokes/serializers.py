from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ['text', 'name']
    
    # add methods to customize the Create/Read/Update/Delete operations
    def create(self, validated_data):
        joke = Joke(**validated_data)
        joke.save()
        return joke

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['image_url', 'name']
    
    # add methods to customize the Create/Read/Update/Delete operations
    def create(self, validated_data):
        picture = Picture(**validated_data)
        picture.save()
        return picture