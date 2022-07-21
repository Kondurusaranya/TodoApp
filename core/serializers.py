from rest_framework import serializers
from .models import Task


# Serializers define the API representation.
class TaskSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    dead_line = serializers.DateTimeField(required=False)

    class Meta:
        model = Task
        fields = "__all__"

    def save(self, **kwargs):
        return super(TaskSerializer, self).save(**kwargs)
