from rest_framework import serializers
from .models import PostedUrls

class PostedUrlsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostedUrls
        fields = '__all__'
