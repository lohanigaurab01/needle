from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='post-pictures', default='defaultimage.png')
    time = models.DateTimeField(default=timezone.now)
    is_deletable = models.BooleanField(default=True)

    def delete(self, *args, **kwargs):
        if self.is_deletable:
            super().delete(*args, **kwargs)

    def __str__(self):
        return f'{self.author} Post'

    def get_absolute_url(self):
        return reverse("detailpost", kwargs={"username": self.author.username, "pk": self.pk})

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('home.Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} likes {self.post}'
