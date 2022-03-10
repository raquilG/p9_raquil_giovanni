from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from . import forms
from ticketing import models
from following import utils


@login_required
def home(request):
    users_followed = utils.get_user_followed_users(request.user)
    tickets = models.Ticket.objects.filter(Q(user_id__in = users_followed) | Q(user = request.user))
    print(tickets)
    reviews = models.Review.objects.filter(Q(user_id__in = users_followed) | Q(user = request.user))
    print(reviews)
    posts = list(tickets) + list(reviews)
    posts.sort(key= lambda x : x.time_created, reverse=True)
    context = {
        'posts': posts}
    return render(request, 'core/home.html', context)


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
