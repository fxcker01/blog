from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import News
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

class ShowNewsView(ListView):
    model = News
    template_name = 'blog/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3


    def get_context_data(self, **kwards):
        ctx = super(ShowNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Главная страница сайта'
        return ctx


class UserAllNewsView(ListView):
    model = News
    template_name = 'blog/user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(avtor=user).order_by('-date')

    def get_context_data(self, **kwards):
        ctx = super(UserAllNewsView, self).get_context_data(**kwards)

        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
        return ctx


class NewsDetailView(DetailView):
    model = News
    
    def get_context_data(self, **kwards):
        ctx = super(NewsDetailView, self).get_context_data(**kwards)

        ctx['title'] = News.objects.get(pk=self.kwargs['pk'])
        return ctx


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx
    

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        
        return False


    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'
    template_name = 'blog/delete-news.html'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.avtor:
            return True
        
        return False



class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    template_name = 'blog/create_news.html'

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)

        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

    def form_valid(self, form):
        form.instance.avtor = self.request.user
        return super().form_valid(form)

def contacti(request):
    return render(request, 'blog/contacti.html', {'title': 'Страница контакты'})

def contacti(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Відправка повідомлення на пошту
            subject = f"Повідомлення від {name}"
            plain_message = f"Від: {name}\nEmail: {email}\n\nПовідомлення:\n{message}"
            from_email = settings.EMAIL_HOST_USER  # пошта відправника (встановлено в settings.py)
            to = "andriykushnir05@gmail.com"  # пошта отримувача

            send_mail(subject, plain_message, from_email, [to])

            # Збереження повідомлення в базі
            # Якщо потрібно, створіть модель для зберігання повідомлень

            # Повідомлення про успішну відправку
            messages.success(request, 'Ваше повідомлення надіслано! Ми з вами зв’яжемось найближчим часом.')
            return render(request, 'blog/contacti.html', {'form': form})

    else:
        form = ContactForm()

    return render(request, 'blog/contacti.html', {'form': form})