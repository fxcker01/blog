from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('User photo', default='default.png', upload_to='user_images')

    receive_newsletter = models.BooleanField(default=False, verbose_name="Subscribe to newsletter")

    CHOICES = (('male', 'Male'), ('female', 'Female'))
    
    gender = models.CharField(max_length=6, choices=CHOICES, default='male', verbose_name="Gender")

    def __str__(self):
        return f'User profile: {self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 350 or image.width > 256:
            resize = (350, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'