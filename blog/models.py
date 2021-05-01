from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField


class userProfile(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num       = models.CharField(max_length = 15)
    age             = models.IntegerField(null=True)
    profile_pic     = models.ImageField(default='assets/profile.png', upload_to='images/profile/', null='true', blank='true')
    @property
    def get_profile_pic(self):
        if self.profile_pic and hasattr(self.profile_pic, 'url'):
            return self.profile_pic.url
        else:
         return "images/assets/profile.png"

class contactus(models.Model):
    fullname        = models.CharField(max_length=35)
    phone_num       = models.CharField(max_length=15)
    email           = models.EmailField()
    message         = models.TextField(max_length=1000)


class blog(models.Model):
    category        = models.CharField(max_length=35)
    title           = models.CharField(max_length=350)
    date_created    = models.DateTimeField(default=datetime.now)
    image           = models.ImageField(default='assets/blog.png', upload_to='images/blog/images', null='true', blank='true')
    description     = RichTextField(null='true', blank='true')
    status          = models.IntegerField(default=1)
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
