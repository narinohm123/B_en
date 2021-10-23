from django.db.models.fields import EmailField
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import response, viewsets


from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from account import serializers
from .models import *
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime 


class YearSerializer(viewsets.ModelViewSet):
    queryset = Year.objects.all()
    serializer_class = YearSerializer


class Academic_ManpowerSerializer(viewsets.ModelViewSet):
    queryset = Academic_Manpower.objects.all()
    serializer_class = Academic_ManpowerSerializer


class Service_ManpowerSerializer(viewsets.ModelViewSet):
    queryset = Service_Manpower.objects.all()
    serializer_class = Service_ManpowerSerializer


class EventSerializer(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class BudgetSerializer(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class Academice_OutstandSerializer(viewsets.ModelViewSet):
    queryset = Academice_Outstand.objects.all()
    serializer_class = Academice_OutstandSerializer


class Service_OutstandSerializer(viewsets.ModelViewSet):
    queryset = Service_Outstand.objects.all()
    serializer_class = Service_OutstandSerializer


class leave_timeSerializer(viewsets.ModelViewSet):
    queryset = leave_time.objects.all()
    serializer_class = leave_timeSerializer


class Study_leaveSerializer(viewsets.ModelViewSet):
    queryset = Study_leave.objects.all()
    serializer_class = Study_leaveSerializer


class PendingSerializer(viewsets.ModelViewSet):
    queryset = Pending.objects.all()
    serializer_class = PendingSerializer


class DocumentSerializer(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class ApprovalSerializer(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer



class Year_planSerializer(viewsets.ModelViewSet):
    queryset = Year_plan.objects.all()
    serializer_class = Year_planSerializer

class Human_resourceSerializer(viewsets.ModelViewSet):
    queryset = Human_resource.objects.all()
    serializer_class = Human_resourceSerializer


class ReportSerializer(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer