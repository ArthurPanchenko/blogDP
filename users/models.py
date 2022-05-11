from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def get_name(self):
        return self.first_name + ' ' + self.last_name
