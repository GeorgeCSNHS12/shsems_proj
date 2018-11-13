from django.shortcuts import render

from django.views.generic import ListView

from .models import Attendance

class AttendanceListView(ListView):
    model = Attendance

