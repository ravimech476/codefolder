# necessary modules for run project
from django.shortcuts import render
#from rest_framework.renderers import JSONRenderer
from projectapp.models import StudentDetails
from projectapp.serializers import Serializers_For_Student
import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
#necessary functions for student Crud operations
class View_for_Student(APIView):
    def get(self,request,*args,**kwargs): 
        data=request.data  
        #emp=StudentDetails.objects.order_by('-id')[2]
        emp=StudentDetails.objects.all()
        #emp=StudentDetails.objects.filter(Student_Name__startswith="r").values('Student_Name')
        #print(emp)
        seri=Serializers_For_Student(emp,many=True)
        return Response(seri.data)
    def post(self,request,*args,**kwargs):
        data=request.data  
        #emp=StudentDetails.objects.order_by('-id')[2]
       # emp=StudentDetails.objects.filter(Student_Name__startswith="r").values('Student_Name','Student_Depatment')
        emp=StudentDetails.objects.values('Student_Name')
       
        print(emp)
        seri=Serializers_For_Student(emp,data=data)
        if seri.is_valid():
            seri.save()
            print(seri.data)
        return Response(seri.data)



