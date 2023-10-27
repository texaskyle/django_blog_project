from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', default='default.jfif')
    bio = models.TextField()

    def __str__(self):
        return f'{self.user.username} profile'

    # overriding the save method so that i save am image which have been resized
    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)

        img = Image.open(self.profile_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            # save the image in the same path as the larger image would have been saved
            img.save(self.profile_picture.path)




