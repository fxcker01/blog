from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class News(models.Model):
    title = models.CharField('Article title', max_length=100, unique=True)
    text = models.TextField('Main article content')
    date = models.DateTimeField('Publication date', default=timezone.now)
    avtor = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)

    views = models.IntegerField('Views', db_default=1)
    # sizes = (
    #     ('S', 'Small'),
    #     ('M', 'Medium'),
    #     ('L', 'Large'),
    #     ('XL', 'X Large'),
    # )

    # shop_sizes = models.CharField(max_length=2, verbose_name='Размеры', choices=sizes, default='S')

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta: 
        verbose_name = 'News article'
        verbose_name_plural = 'News'