from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.HyperlinkedModelSerializer):
    author=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model=Book
        fields=['url','author','id','title','book_price','category']

class UserSerializer(serializers.ModelSerializer):
    books=serializers.HyperlinkedRelatedField(many=True, view_name='book-detail', read_only=True)
    class Meta:
        model=User
        fields=['url','id','username','books']