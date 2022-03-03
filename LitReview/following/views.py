from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import CustomUser
from django.contrib import messages
from . import models


@login_required
def subcription_page(request):
    users_follow = models.UserFollows.objects.filter(user_id=request.user.id)
    users_follow_id = [user.followed_user_id for user in users_follow]
    
    followed_by = models.UserFollows.objects.filter(followed_user_id=request.user.id)

    search = request.session['found_users'] if "found_users" in request.session else ""
    if search:
        found_users = CustomUser.objects.filter(
                        username__contains=search
                    ).exclude(
                        id__in=users_follow_id
                    ).exclude(
                        username=request.user.username)

        if not found_users:
            messages.add_message(request, messages.INFO, "il n'y a pas d'utilisateur correspond a votre rechercher.")
    else:
        found_users = []

    context = {
        'found_users': found_users,
        'users_follow': users_follow,
        'followed_by': followed_by}
    return render(request, 'following/subcription.html', context)


@login_required
def search_users(request):
    search = request.POST.get('search')
    request.session['found_users'] = search
    return redirect('subcription')


@login_required
def subscribe_user(request):
    username = request.POST.get('username')
    user_follow = models.UserFollows()
    user_follow.user = request.user
    user_follow.followed_user = CustomUser.objects.filter(username=username)[0]
    user_follow.save()
    return redirect('subcription')


@login_required
def unsubscribe_user(request, follow_id):
    following = models.UserFollows.objects.get(id=follow_id)
    if request.method =="POST":
        user_name = following.followed_user.username
        following.delete()
        messages.add_message(request, messages.INFO, f"Vous vous êtes désabonné a l'utilisateur {user_name}!")
    return redirect('subcription')