from rest_framework import serializers
from .models import Zantta


class ZanttaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = Zantta