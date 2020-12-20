from datetime import datetime
from django.urls import path

"""Активация администраивного раздела"""
from django.urls import include
from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'), #ссылка на обработку Главная страница
    path('accounts/profile/', views.home, name='home'), #избавляемся от бага при логине (только в vs19)
    path('contact/', views.contact, name='contact'), #ссылка на обработку Контакты
    path('links/', views.links, name='links'), #ссылка на обработку Полезные ресурсы
    path('about/', views.about, name='about'), #ссылка на обработку О нас
    path('pool/', views.pool, name='pool'), #ссылка на обработку Отзыв
    path('video/', views.video, name='video'), #ссылка на обработку Видео
    path('blog/', views.blog, name='blog'), #ссылка на обработку Блог
    path('newpost/', views.newpost, name='newpost'), #ссылка на обработку Новая статья
    path('register/', views.register, name='register'), #ссылка на обработку Запись
    path('myregister/', views.myregister, name='myregister'), #ссылка на обработку Мои записи
    path('allregister/', views.allregister, name='allregister'), #ссылка на обработку Управление записями
    path('(?P<parametr>\d+)/', views.blogpost, name='blogpost'), #ссылка на обработку Статья блога
    path('delregister/(?P<did>\d+)/', views.delregister, name='delregister'), #ссылка на обработку Удалить запись
    path('status1/(?P<sid>\d+)/', views.status1, name='status1'), #ссылка на обработку Статуса
    path('status2/(?P<sid>\d+)/', views.status2, name='status2'), #ссылка на обработку Статуса
    path('registration/', views.registration, name='registration'), #ссылка на обработку Регистрация
    path('login/', #обработка стандартной авторизации
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Вход',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

"""Для загрузки изображений"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()