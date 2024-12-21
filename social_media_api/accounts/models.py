from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Allows users to have an optional biography
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers', blank=True)
    profile_picture = models.ImageField(
        upload_to="profile_pictures/",  # Directory where profile pictures will be stored
        blank=True,  # Optional field
        null=True    # Allows no picture to be uploaded
    )
    followers = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='following'  # Ensures reverse accessor does not clash
    )

    def __str__(self):
        return self.username



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
