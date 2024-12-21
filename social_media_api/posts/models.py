from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Post(models.Model):
    author = models.ForeignKey(
        "accounts.CustomUser",  # Assuming 'accounts.CustomUser' is your custom user model
        on_delete=models.CASCADE,
        related_name="posts",
        null=True, 
        blank=True 
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the custom user model defined in settings
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Ensures it points to the custom user model
        on_delete=models.CASCADE
    )
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')


    def __str__(self):
        return f"Like by {self.user} on {self.post}"
