from . import models

def get_user_followed_users(user):
    users_follows = models.UserFollows.objects.filter(user_id=user.id)
    return [user_follow.followed_user for user_follow in users_follows]