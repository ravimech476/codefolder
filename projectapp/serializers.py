from projectapp.models import StudentDetails
from rest_framework import serializers
# serializers for StudentDetails
class Serializers_For_Student(serializers.ModelSerializer):
    class Meta:
        model=StudentDetails
        fields="__all__"
        