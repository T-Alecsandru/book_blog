from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)  # userul nu o sa poata sa schimbe timpul
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.created_on}'


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # orice user este logat va fi pus pe aceasta linie
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} - {self.post}'


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile',
                                on_delete=models.CASCADE)  # One to one = on user one profile sau invers
    first_name = models.CharField(max_length=45, blank=True, null=True)
    last_name = models.CharField(max_length=45, blank=True,
                                 null=True)  # blank poate fi lasat liber, null-poate fi gol in baza de date
    bio = models.TextField(max_length=500, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/profile_pictures',
                                default='uploads/profile_pictures/default.png', blank=True)

    def __str__(self):
        return f'{self.user} - {self.location}'
