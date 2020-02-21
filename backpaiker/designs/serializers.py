from rest_framework import serializers
from designs.models import Design

# Design Serializer
class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = "__all__"

