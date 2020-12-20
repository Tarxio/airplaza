from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from .models import Comment
from .models import Blog
from .models import Register

class BootstrapAuthenticationForm(AuthenticationForm):
    """Форма стандартной авторизации"""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))


class PoolForm(forms.Form):
    """Форма Отзыв"""
    name = forms.CharField(label='Ваше имя', min_length = 2, max_length = 100)
    receiver = forms.ChoiceField(label='Тип услуги',
                             choices=[('1','Свободные прыжки'),
                                      ('2','Посещение мероприятия')],
                             widget=forms.RadioSelect, initial=1)
    score = forms.ChoiceField(label='Общее впечатление',
                             choices=[('1','Отлично'),('2','Хорошо'),
                                      ('3','Плохо')],initial=1)
    message = forms.CharField(label='Отзыв', widget=forms.Textarea(attrs={'rows':10,'cols':100}))
    agree = forms.BooleanField(label='Я согласен на отправление моего отзыва', required=True)
    test = forms.DateField(label='Дата посещения')
    test1 = forms.TimeField(label='Время посещения')


class CommentForm (forms.ModelForm):
    """Форма Комментарий"""
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {'text': "Добавить комментарий"}


class BlogForm (forms.ModelForm):
    """Форма Новая статья"""
    class Meta:
        model = Blog
        fields = ('title','description','content','image')
        labels = {'title': "Заголовок",'description': "Краткое содержание",'content': "Полное содержание",'image': "Изображение"}

class RegisterForm (forms.ModelForm):
    """Форма Запись"""
    class Meta:
        model = Register
        fields = ('rname','rnumber','remail','rdate','rtime','rcount')
        labels = {'rname': "Ваше имя",'rnumber': "Номер телефона",'remail': "E-mail",'rtime': "Время",'rcount': "Количество людей"}
        widgets = {
            'rdate': forms.SelectDateWidget(years=range(2020, 2025))
        }