from django.shortcuts import render

from django.views.generic import ListView

from .models import Attendance
from registrations.models import Registration

from django.contrib.auth.mixins import LoginRequiredMixin

class AttendanceTemplateView(ListView):
    model = Attendance
    template_name = "attendance_summary.html"
    context_object_name = "attendance_summary"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(registration = self.kwargs['registration_pk'])