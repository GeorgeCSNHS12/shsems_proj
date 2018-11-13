from django.db import models

class Attendance(models.Model):

    for_date = models.DateField("For Date", null=True)

    time_arrived = models.TimeField("Time Arrived", null=True)
    time_left = models.TimeField("Time Left", null=True)

    registration = models.ForeignKey(to='registrations.Registration', on_delete = models.CASCADE)

