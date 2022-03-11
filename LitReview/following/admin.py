from django.contrib import admin

from . import models


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ('user', 'followed_user', )


admin.site.register(models.UserFollows, UserFollowsAdmin)
# Register your models here.
