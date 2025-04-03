from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField('Фото пользователя', default='default.png', upload_to='user_images')

    receive_newsletter = models.BooleanField(default=False, verbose_name="Подписка на рассылку")

    CHOICES = (('male', 'Мужской'), ('female', 'Женский'))
    
    gender = models.CharField(max_length=6, choices=CHOICES, default='female', verbose_name="Пол")

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'
    
    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 350 or image.width > 256:
            resize = (350, 256)
            image.thumbnail(resize)
            image.save(self.img.path)

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'