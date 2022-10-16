from django.db import models
from django.contrib.sites.models import Site
import cyrtranslit


# Create your models here.
nb = dict(null=True, blank=True, default=None)


def complex_dir_path(instance, filename):

    name = instance.name.replace(' ', '_')
    dir_name = cyrtranslit.to_latin(name, 'ru').lower()

    filename = filename.replace(' ', '_')
    filename = cyrtranslit.to_latin(filename, 'ru').lower()

    return f'primary/{dir_name}/{filename}'


class SiteData(models.Model):
    site = models.OneToOneField(
        Site,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        'Заголовок',
        help_text='Название сайта во вкладке',
        max_length=180,
    )
    meta_description = models.TextField(
        'Краткое описание',
        help_text='Описание сайта (для ссылко) CEO',
        max_length=500
    )
    scripts = models.TextField(
        'Скрипты аналитики',
        max_length=500
    )
    header_phone = models.CharField(
        'Телефон',
        max_length=40
    )
    addres = models.TextField(
        'Адрес',
        max_length=400
    )
    footer_phones = models.TextField(
        'Телефоны внизу',
        max_length=400
    )
    created_at =  models.DateTimeField(
        'Создан',
        auto_now_add=True
    )
    class Meta:
        verbose_name = 'Данные сайта'
        verbose_name_plural = 'Данные сайтов'
    
    def __str__(self) -> str:
        return f'{self.site}'

    @property
    def site_domain(self):
        return self.site.domain


class Client(models.Model):
    site = models.ForeignKey(
        SiteData,
        on_delete=models.CASCADE,
        verbose_name='Сайт'
    )
    name = models.CharField(
        'ФИО',
        max_length=180, **nb
    )
    complex = models.CharField(
        'Страница',
        max_length=180,
    )
    phone = models.CharField(
        "Телефон",
        max_length=80, **nb
    )
    email = models.CharField(
        'Email',
        max_length=80, **nb
    )
    created_at = models.DateTimeField(
        'Создан',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self) -> str:
        return f'{self.name}'



class Specialist(models.Model):

    name = models.CharField(
        'ФИО',
        max_length=180
    )
    photo = models.ImageField(
        "Фото",
        upload_to=complex_dir_path, **nb
    )
    role = models.CharField(
        'Роль в проекте',
        max_length=180
    )
    phone = models.CharField(
        'Номер телефона',
        max_length=18
    )
    email = models.CharField(
        'Почта',
        max_length=40
    )
    tg_link = models.CharField(
        'Telegram ссылка',
        max_length=250
    )
    wh_link = models.CharField(
        'WhatsApp ссылка',
        max_length=250
    )

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'
        ordering = ['-name']

    def __str__(self) -> str:
        return f'{self.name}'


class Area(models.Model):
    site = models.ForeignKey(
        SiteData,
        on_delete=models.CASCADE,
        verbose_name='Сайт'
    )

    name = models.CharField(
        'Название района',
        max_length=180
    )

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'
        ordering = ['-name']

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def about(self):
        return AreaPeculiarity.objects.filter(area=self)


class AreaPeculiarity(models.Model):
    name = models.CharField(
        'Название',
        max_length=100
    )
    amount = models.IntegerField(
        'Кол-во',
        default=0
    )
    photo = models.ImageField(
        "Фото",
        upload_to=complex_dir_path
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        verbose_name='Район'
    )

    class Meta:
        verbose_name = 'Особенность района'
        verbose_name_plural = 'Особенности района'
        ordering = ['-name']

    def __str__(self) -> str:
        return f'{self.name}'
