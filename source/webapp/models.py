from django.db import models

STATUS_CHOICES = [('active', 'Активно'), ('blocked', 'Заблокировано')]


class Record(models.Model):
    author = models.TextField(max_length=30, verbose_name='Имя')
    mail = models.EmailField(max_length=20, verbose_name='Почта')
    description = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=40, choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0][0], verbose_name='Статус')


def __str__(self):
    return "{}. {}".format(self.pk, self.author)


class Meta:
    db_table = "Guests book"
    verbose_name = "Запись"
    verbose_name_plural = "Записи"
