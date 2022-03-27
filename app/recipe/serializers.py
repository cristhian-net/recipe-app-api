from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        """Serializer for Tag objects"""
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
