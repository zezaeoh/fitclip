from rest_framework import serializers

from fitclib.accounts.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = UserProfile
        fields = '__all__'
