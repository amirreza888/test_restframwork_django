from rest_framework import serializers
from .models import Book, BookNumber, Character, Author

class BookNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookNumber
        fields = ['sibn_10','sibn_13']

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name','surname']


class BookSerializer(serializers.ModelSerializer):
    number = BookNumberSerializer(many=False)
    character = CharacterSerializer(many=True)
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id','title', 'price', 'description', 'number','character','authors']


class BookMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title',]