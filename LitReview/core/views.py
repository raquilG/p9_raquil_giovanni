from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from . import forms
from ticketing import models


@login_required
def home(request):
    tickets = models.Ticket.objects.all()
    return render(request, 'core/home.html', context={'tickets': tickets})


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'core/signup.html', context={'form': form})
