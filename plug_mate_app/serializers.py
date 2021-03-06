from rest_framework import serializers
from .models import RemoteData, ScheduleData, PresenceData, AchievementsBonus

class RemoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RemoteData
        fields = ('id', 'user_id', 'device_type', 'device_state')

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleData
        fields = ('id', 'user_id', 'event_id', 'event_start', 'event_end', 'event_name', 'event_rrule', 'device_type_id', 'device_type')

class PresenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresenceData
        fields = ('id', 'user_id', 'device_type', 'presence_setting')

class AchievementsBonusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AchievementsBonus
        fields = ('id', 'user_id', 'tree_first', 'tree_fifth', 'tree_tenth', 'redeem_reward', 'first_remote', 'first_schedule', 'first_presence')


