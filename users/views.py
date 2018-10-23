from django.shortcuts import render

from django.views.generic import CreateView

from .forms import ParticipantCreationForm

from django.urls import reverse_lazy

class SignUpView(CreateView):
    form_class = ParticipantCreationForm
    success_url = reverse_lazy("home")
    template_name = "signup.html"