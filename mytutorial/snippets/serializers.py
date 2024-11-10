from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.ModelSerializer):
    # `source` argument controls which attribute is used to populate a field.
    # Alternative: `CharField(read_only=True)`
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Snippet
        fields = ["id", "title", "code", "linenos", "language", "style", "owner"]


class UserSerializer(serializers.ModelSerializer):
    # Reverse relationship will not be included by default.
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ["id", "username", "snippets"]
