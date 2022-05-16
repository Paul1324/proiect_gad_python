from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.


class MyModel(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Profile(MyModel):
    class Meta:
        db_table = 'profiles'

    image = models.CharField(max_length=60)
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    bio = models.CharField(max_length=200)
    followers = models.CharField(max_length=50)
    following = models.CharField(max_length=50)

    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, default=1)
    # repos = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Repo', related_name='repos')

    def __str__(self):
        return f"{self.username}"


class Repo(MyModel):
    class Meta:
        db_table = 'repos'

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=60, unique=True)
    language = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def profile_username(self):
        return self.profile.username

    def __str__(self):
        return f'{self.id}'
