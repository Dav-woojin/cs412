from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    # profile serializer class converts all the necessary data
    class Meta:
        model = Profile
        fields = ["id", "username", "display_name", "profile_image_url", "bio_text", "join_date"]

        def create(self, validated_data):
            # create function to save a new profile if its ever created
            profile = Profile(**validated_data)
            profile.user = User.objects.first()
            profile.save()
            return profile


class PostSerializer(serializers.ModelSerializer):
    # post serializer creates two new fields, one for reading a photo url and one for allowing new post creations to add a url
    photo_url = serializers.SerializerMethodField()
    photo_url_input = serializers.URLField(write_only = True, required=False)
    class Meta:
        model = Post
        fields = ["photo_url", "caption", "photo_url_input"]

    def create(self, validated_data):
        # create function saves new post as well as creates a new photo object with provided url
        photo_url = validated_data.pop("photo_url_input", None)
        post = Post(**validated_data)
        post.profile = Profile.objects.filter(user = self.context["request"].user).first()
        post.save()
        if photo_url:
            Photo.objects.create(post = post, image_url = photo_url)
        return post

    def get_photo_url(self, obj):
        # this function gets the correct photo url attached to a post and then gives that back as a field
        photos = Photo.objects.filter(post = obj)
        if photos:
            first_photo_url = photos.first().image_url
            return first_photo_url
        return None


