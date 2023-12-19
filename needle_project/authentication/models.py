from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    intro=models.CharField(max_length=50, default='')
    contact_number=models.IntegerField(default='9800000000')
    image = models.ImageField(upload_to='profile-picture', default='default.jpg')
    background_cover=models.ImageField(upload_to='profile-picture', default='back-default.jpg')


    def __str__(self):
        return f'{self.user.username} Profile'
