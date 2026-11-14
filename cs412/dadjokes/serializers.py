# David Chung, dwjchung@bu.edu
# serializers file for Joke and Picture

from rest_framework import serializers
from .models import *

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = ['text', 'name']
    
    # add methods to customize the Create/Read/Update/Delete operations
    def create(self, validated_data):
        # create method for joke and save to databse
        joke = Joke(**validated_data)
        joke.save()
        return joke

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ['image_url', 'name']
    
    # add methods to customize the Create/Read/Update/Delete operations
    def create(self, validated_data):
        # create method for picture and save to databse
        picture = Picture(**validated_data)
        picture.save()
        return picture