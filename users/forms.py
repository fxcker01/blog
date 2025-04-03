from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label= 'Введите логин', 
        required=True, 
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин:'})
    )
    email = forms.EmailField(
        label= 'Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email:'})
    )
    # some = forms.ModelChoiceField(queryset=User.objects.all())
    password1 = forms.CharField(label= 'Введите пароль', 
    required=True, 
    help_text='Пароль не должен быть маленьким и простым',
    widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль:'})
    )
    password2 = forms.CharField(
        label= 'Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Повторно введите пароль:'})
    )



    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(
        label= 'Введите логин', 
        required=True, 
        help_text='Нельзя вводить символы: @, /, _',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин:'})
    )
    email = forms.EmailField(
        label = 'Введите Email',
        required = True,
        widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email:'})
    )
    

    class Meta:
        model = User
        fields = ['email', 'username']

    def save(self, commit = True):
        user = super().save(commit = False)
        
        profile, created = Profile.objects.get_or_create(user=user)

        if commit:
            user.save()
            profile.save()

        return user


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label= 'Загрузить фото',
        required=False,
        widget=forms.FileInput
    )
    gender = forms.ChoiceField(
        label='Выберите пол',
        choices = Profile.CHOICES,
        required = True,
        widget = forms.Select(attrs={'class': 'form-control'})
    )
    receive_newsletter = forms.BooleanField(
        label = 'Получать новости',
        required = False,
        widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    class Meta:
        model = Profile
        fields = ['img', 'gender', 'receive_newsletter']


