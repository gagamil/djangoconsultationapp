from django.contrib.auth.models import User
from django.db import transaction
from djoser.serializers import UserCreateSerializer
from djoser.conf import settings


class CustomUserCreateSerializer(UserCreateSerializer):
    def perform_create(self, validated_data):
        with transaction.atomic():
            validated_data['username'] = validated_data['email']
            user = User.objects.create_user(**validated_data)
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user
