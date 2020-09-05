from rest_framework import serializers
from .models import Employee
from datetime import datetime


class EmployeeSerializers(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    dept_str = serializers.CharField(source='get_dept_display', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def get_age(self, edob):
        return (datetime.now().year - edob.dob.year)
