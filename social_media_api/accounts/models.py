from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Define related names for follower/followed relationships explicitly
    followers = models.ManyToManyField(
        'self',
        through='CustomUserFollowers',
        symmetrical=False,
        related_name='following_users'
    )
    following = models.ManyToManyField(
        'self',
        through='CustomUserFollowing',
        symmetrical=False,
        related_name='followers_users'
    )


class CustomUserFollowers(models.Model):
    follower = models.ForeignKey(
        CustomUser,
        related_name="follower_relationships",  # Unique related name
        on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        CustomUser,
        related_name="followed_by_relationships",  # Unique related name
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} follows {self.followed}"


class CustomUserFollowing(models.Model):
    follower = models.ForeignKey(
        CustomUser,
        related_name="following_relationships",  # Unique related name
        on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        CustomUser,
        related_name="followed_relationships",  # Unique related name
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower} follows {self.followed}"
