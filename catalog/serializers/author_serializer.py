from rest_framework import serializers
from catalog.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name','bio', 'date_of_birth', 'nationality']