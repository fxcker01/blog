from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'receive_newsletter', 'img')  # Додаємо поле receive_newsletter
    list_filter = ('gender', 'receive_newsletter')  # Можна фільтрувати за gender та receive_newsletter
    search_fields = ('user__username',)  # Шукати за іменем користувача

admin.site.register(Profile, ProfileAdmin)
