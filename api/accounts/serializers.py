from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}".strip()
