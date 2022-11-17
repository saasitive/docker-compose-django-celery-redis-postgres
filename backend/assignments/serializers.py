from rest_framework import serializers

from assignments.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        read_only_fields = ("id", "sum")
        fields = ("id", "first_term", "second_term", "sum")
