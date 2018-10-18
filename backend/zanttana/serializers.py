from rest_framework import serializers
from .models import Profile, Zantta, Lodging, Logistics


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'user',
            'bio',
            'current_loc',
            'join_date',
            'invited_by',
        )
        model = Profile
        
class ZanttaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'zantta_name',
            'description',
            'start_date',
            'end_date',
            'members'
        )
        model = Zantta

class LodgingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'reserver',
            'lodge_name',
            'lodge_address',
            'arrive_date',
            'leave_date',
            'members_booked'
        )
        model = Lodging

class LogisticsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'owner',
            'zantta',
            'method',
            'depart_loc',
            'arrive_loc',
            'depart_time',
            'arrive_time',
            'members_booked'
        )
        model = Logistics