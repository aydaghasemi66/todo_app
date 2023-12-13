from rest_framework import serializers
from ...models import Task


# class CourseApiSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     title = serializers.CharField(max_length=200)
#     price = serializers.IntegerField()


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ["id", "title",]


