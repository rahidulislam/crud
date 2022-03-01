from core.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title', 'description',)
        
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ('title', 'description',)