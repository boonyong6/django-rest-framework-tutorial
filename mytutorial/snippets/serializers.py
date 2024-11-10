from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippet


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # `source` argument controls which attribute is used to populate a field.
    # Alternative: `CharField(read_only=True)`
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html"
    )

    class Meta:
        model = Snippet
        fields = [
            "url",
            "id",
            "highlight",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Reverse relationship will not be included by default.
    snippets = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="snippet-detail"
    )

    class Meta:
        model = User
        fields = ["url", "id", "username", "snippets"]
