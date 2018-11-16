from django.urls import path
from .views import AttendanceTemplateView

urlpatterns = [
    path('myactivities/<int:registration_pk>/attendance/', AttendanceTemplateView.as_view(), name='attendance_summary')
]