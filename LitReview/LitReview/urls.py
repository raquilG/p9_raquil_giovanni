"""LitReview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
import core.views
import following.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
            template_name="core/login.html",
            redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='core/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='core/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', core.views.signup_page, name='signup'),
    path('home/', core.views.home, name='home'),
    path('subscription/', following.views.subcription_page, name='subcription'),
    path('search_users/', following.views.search_users, name='search-users'),
]
