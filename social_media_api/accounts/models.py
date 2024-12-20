from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='followers')

    def __str__(self):
        return self.username
    

class CustomUser(AbstractUser):
    # other fields...

    followers = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='following',  # Change reverse accessor to 'following'
        blank=True
    )

    following = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='followers',  # Change reverse accessor to 'followers'
        blank=True
    )
