from datetime import datetime
from django.db import models
from datetime import date

#Models for to store student details
class StudentDetails(models.Model):
    Create_Studentmodel=models.DateTimeField(date.today)
    Student_Name=models.CharField(max_length=20)
    Student_Rollno=models.IntegerField()
    Student_Depatment=models.CharField(max_length=30)
    Is_Student_Id_delete=models.BooleanField(default=False)
