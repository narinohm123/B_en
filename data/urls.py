from django.urls import path
from django.urls.conf import include

from . import views
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
# router.register('profile',views.Profile_Detail)
# router.register('degree',views.Degree_Detail)
# router.register('user',views.User_detail)
router.register('Year',views.YearSerializer)
router.register('Academic_Manpower',views.Academic_ManpowerSerializer)
router.register('Service_Manpower',views.Service_ManpowerSerializer)
router.register('Event',views.EventSerializer)
router.register('Budget',views.BudgetSerializer)
router.register('Academice_Outstand',views.Academice_OutstandSerializer)
router.register('Service_Outstand',views.Service_OutstandSerializer)
router.register('leave_time',views.leave_timeSerializer)
router.register('Study_leave',views.Study_leaveSerializer)
router.register('Pending',views.PendingSerializer)
router.register('Document',views.DocumentSerializer)
router.register('Approval',views.ApprovalSerializer)
router.register('Year_plan',views.Year_planSerializer)
router.register('Human_resource',views.Human_resourceSerializer)
router.register('Report',views.ReportSerializer)


urlpatterns = [
    path('',include(router.urls)),
    
]