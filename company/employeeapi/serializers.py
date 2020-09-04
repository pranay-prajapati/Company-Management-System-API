from rest_framework import serializers
from .models import Employee
from datetime import datetime


class EmployeeSerializers(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_age(self,edob):
        return (datetime.now().year - edob.dob.year)