from django.shortcuts import render
from django.db import IntegrityError
from django.shortcuts import render_to_response

from django.views.generic import CreateView, DetailView, TemplateView, ListView

from .models import Registration
from users.models import Participant
from events.models import Event
from attendances.models import Attendance

from django.contrib.auth.mixins import LoginRequiredMixin

class JoinEventView (CreateView):
    model = Registration

    fields = ['parents_permit', 'parents_contact_number', 'waiver']

    template_name = "join_event.html"
    
    def form_valid(self, form):
        try:
            form.instance.participant = self.request.user
            qs = Event.objects.filter(pk = self.kwargs['event_pk'])
            form.instance.event = qs.first()
            return super().form_valid(form)
        except IntegrityError as e:
            return render_to_response("evaluate_user_join.html", {"message" : e.args[0]})
    

class RegistrationDetailView (DetailView):
    model = Registration
    template_name = "registration_detail.html"
    context_object_name = "registration"

class RegistrationListView (TemplateView):
    template_name = "registration_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        qs = Registration.objects.all()
        data ["registration_list"] = qs
        return data

class MyActivitiesListView(LoginRequiredMixin, ListView):
    model = Registration
    template_name = "activity_list.html"
    context_object_name = "activity_list"

    login_url = "login"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(participant = self.request.user)

class CreateAttendanceView(CreateView):
    model = Attendance

    fields = ['for_date']

    template_name = "create_attendance.html"

    def form_valid(self, form):
        form.instance.registration = self.request.user
        return super().form_valid(form)