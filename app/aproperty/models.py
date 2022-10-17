from email.policy import default
from django.db import models
from django.contrib.sites.models import Site
import cyrtranslit
import re

# Create your models here.
nb = dict(null=True, blank=True, default=None)


def _get_name(name, filename):
    dir_name = cyrtranslit.to_latin(name, 'ru').lower()
    filename = filename.replace(' ', '_')
    filename = cyrtranslit.to_latin(filename, 'ru').lower()
    return f'primary/{dir_name}/{filename}'

def complex_dir_path(instance, filename):
    name = instance.name.replace(' ', '_')
    return _get_name(name, filename)
   

def complex_dir_path1(instance, filename):
    name = instance.site.name.replace(' ', '_')
    return _get_name(name, filename)

def complex_dir_path11(instance, filename):
    name = instance.site.site.name.replace(' ', '_')
    return _get_name(name, filename)


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
    title_image = models.ImageField(
        "Фото",
        help_text='Обложка для старта продаж',
        upload_to=complex_dir_path1, **nb
    )
    title_second = models.CharField(
        'Заголовок 1',
        help_text='Большая надпись в первой секции',
        default='ПОРТАЛ ЭЛИТНОЙ НЕДВИЖИМОСТИ',
        max_length=180,
    )
    wh_link = models.CharField(
        'Ссылка WhatsApp',
        max_length=580,
        default='https://wa.me/79818771062?text=Добрый день!%0AРасскажите, пожалуйста, подробнее о доступных ЖК'
    )
    meta_description = models.TextField(
        'Краткое описание',
        help_text='Описание сайта (для ссылко) CEO',
        max_length=500
    )
    scripts = models.TextField(
        'Скрипты аналитики',
        max_length=1500
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
    created_at = models.DateTimeField(
        'Создан',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Данные сайта'
        verbose_name_plural = 'Данные сайтов'

    def __str__(self) -> str:
        return f'{self.site}'

    @property
    def videos(self):
        return YouTubeLink.objects.filter(site=self)

    @property
    def slides(self):
        return MainSlider.objects.filter(site=self)

    @property
    def site_domain(self):
        return self.site.domain
    
    @property
    def site_name(self):
        return self.site.name
    
    def get_lan(self):
        dubai_en = 'statusprime.com'
        return 'en' if self.site.domain == dubai_en else 'ru'


class YouTubeLink(models.Model):
    site = models.ForeignKey(
        SiteData,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        'Название',
        max_length=100
    )
    link = models.CharField(
        'Ссылка',
        max_length=400
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = 'YouTube ссылка'
        verbose_name_plural = 'YouTube ссылки'

    def save(self, *args, **kwargs):
        self.name = self.name.upper()
        self.link = re.sub('watch?v=', 'embed/', self.link)
        self.link = re.sub('youtu.be/', 'youtube.com/embed/', self.link)
        super(YouTubeLink, self).save(*args, **kwargs)


class MainSlider(models.Model):
    site = models.ForeignKey(
        SiteData,
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        "Фото",
        upload_to=complex_dir_path11
    )
    logo = models.ImageField(
        "Лого",
        upload_to=complex_dir_path11
    )
    link = models.CharField(
        'Ссылка',
        max_length=400
    )
    def __str__(self) -> str:
        return f'Слайд {self.pk}'

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'



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
    
    @property
    def site_name(self):
        return self.site.site.name


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
    
    @property
    def site_name(self):
        return self.site.site.name


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
