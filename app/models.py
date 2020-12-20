from django.db import models
from datetime import datetime
from django.contrib import admin
from django.urls import reverse
from django.contrib.auth.models import User

#Модель Блог
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")
    image = models.FileField(default = 'temp.jpg', verbose_name ="Путь к изображению") #Для загрузки изображения

    def get_absolute_url(self):
        return reverse("blogpost", args=[str(self.id)])

    def _str_(self):
        return self.title

    class Meta:
        db_table = "Posts"
        ordering = ["-posted"]
        verbose_name = "Статья блога"
        verbose_name_plural = "Статья Блога"

#Модель Комментарий
class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")

    def _str_(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = "Comments"
        ordering = ["-date"]
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий к статьям блога"
        
#Модель Запись
class Register(models.Model):
    rauthor = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Имя пользователя")
    rname = models.CharField(max_length = 100, verbose_name = "Имя")
    rnumber = models.CharField(max_length = 100, verbose_name = "Номер телефона")
    remail = models.EmailField(verbose_name = "E-mail")
    rdate = models.DateField(verbose_name = "Дата")
    rtime = models.TimeField(verbose_name = "Время")
    rcount = models.CharField(max_length = 100, verbose_name = "Количество человек")
    ready = models.CharField(default='0', max_length = 1, verbose_name = "Статус")

    def _str_(self):
        return self.rauthor

    class Meta:
        db_table = "Register"
        ordering = ["rdate"]
        verbose_name = "Запись"
        verbose_name_plural = "Запись"



#Отображение моделей в административном разделе
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Register)
