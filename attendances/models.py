from django.db import models
from django.urls import reverse

class Attendance(models.Model):

    for_date = models.DateField("For Date", null=True)

    time_arrived = models.TimeField("Time Arrived", null=True, blank=True)
    time_left = models.TimeField("Time Left", null=True, blank=True)

    security_key = models.CharField(max_length=10, blank=True, null=True)
    registration = models.ForeignKey(to='registrations.Registration', on_delete = models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("attendance_summary", kwargs={"pk": self.pk})
