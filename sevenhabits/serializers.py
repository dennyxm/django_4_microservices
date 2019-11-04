from rest_framework import serializers

from sevenhabits.models import Roles, Goals


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"

class GoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goals
        fields = "__all__"