from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
#จัดฟิลด์ข้อมูลในรูปแบบ dict เป็น json
    class Meta:
        model = Task
        fields = ('id', 'seq', 'description', 'complete')