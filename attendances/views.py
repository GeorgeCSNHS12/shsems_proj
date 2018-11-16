from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Attendance
from registrations.models import Registration

from django.contrib.auth.mixins import LoginRequiredMixin

class AttendanceTemplateView(TemplateView):
    model = Attendance
    template_name = "attendance_summary.html"
    context_object_name = "attendance_sum"
    

