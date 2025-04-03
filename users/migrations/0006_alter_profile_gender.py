# Generated by Django 5.1.5 on 2025-02-03 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'Мужчина'), ('female', 'Женщина')], default='female', max_length=6, verbose_name='Пол'),
        ),
    ]
