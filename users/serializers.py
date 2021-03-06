from django.db.models import fields
from rest_framework import serializers
from django.conf import settings


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = "__all__"
