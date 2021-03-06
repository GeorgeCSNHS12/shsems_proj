from django.urls import path

from .views import JoinEventView, RegistrationDetailView, RegistrationListView, MyActivitiesListView, CreateAttendanceView

urlpatterns = [
    path("myactivities/", MyActivitiesListView.as_view(), name="activity_list"),
    path("events/my/<int:pk>/updateattendance/", CreateAttendanceView.as_view(), name="update_attendance"),
    path("registration/<int:pk>/", RegistrationDetailView.as_view(), name="registration_detail"),
    path("events/<int:event_pk>/join/", JoinEventView.as_view(), name="join_event"),
    path("registration/<int:event_pk>/participants/", RegistrationListView.as_view(), name="registration_list")
]