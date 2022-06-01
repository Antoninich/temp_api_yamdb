from django.contrib.auth.models import AbstractUser
from django.db import models

ROLES = [
    ('user', 'user'),
    ('moderator', 'moderator'),
    ('admin', 'admin'),
]


class UserProfile(AbstractUser):
    role = models.SlugField(choices=ROLES, default='user')
    bio = models.TextField()

    def __str__(self):
        return self.username
