from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from .models import *
from rest_framework import fields, serializers
# Create your views here.

class YearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year
        fields = '__all__'


class Academic_ManpowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academic_Manpower
        fields = '__all__'


class Service_ManpowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Manpower
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'


class Academice_OutstandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Academice_Outstand
        fields = '__all__'
        

class Service_OutstandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Outstand
        fields = '__all__'
        

class leave_timeSerializer(serializers.ModelSerializer):
    class Meta:
        model = leave_time
        fields = '__all__'


class Study_leaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study_leave
        fields = '__all__'


class PendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pending
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'


class Year_planSerializer(serializers.ModelSerializer):
    class Meta:
        model = Year_plan
        fields = '__all__'


class Human_resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human_resource
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'