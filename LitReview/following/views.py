from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from core.models import CustomUser


@login_required
def subcription_page(request):
    found_users = request.session['found_users']
    return render(request, 'following/subcription.html', context={'found_users' : found_users})


@login_required
def search_users(request):
    search = request.POST.get('search')
    print(search)
    users = CustomUser.objects.exclude(username =request.user.username)
    print(users)
    request.session['found_users'] = users
    return redirect('subcription')