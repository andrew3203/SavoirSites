from django.db import models
from django.contrib.sites.models import Site
import cyrtranslit
import re
from django.core.validators import ValidationError
from ckeditor.fields import RichTextField
from django.utils.translation import gettext as _

nb = dict(null=True, blank=True, default=None)

class DecorType(models.TextChoices):
    NO = 'NO', _('Без отделки')
    SIMPLE = 'SIMPLE', _('WhiteBox')
    EURO = 'EURO', _('С отделкой')
    DESIGN = 'DESIGN', ('Дизайнерский')

def validate_logo(file, **kwargs):
    val = file.name.lower().rsplit('.', 1)[-1]
    if val not in ['jpeg', 'png', 'svg', 'jpg']:
        raise ValidationError("Не верный формат изображения")


def _get_name(name, filename):
    name = name.replace(' ', '_')
    dir_name = cyrtranslit.to_latin(name, 'ru').lower()
    filename = filename.replace(' ', '_')
    filename = cyrtranslit.to_latin(filename, 'ru').lower()
    return f'primary/{dir_name}/{filename}'


def complex_dir_path(instance, filename):
    name = instance.name
    return _get_name(name, filename)


def complex_dir_path1(instance, filename):
    name = instance.site.name
    return _get_name(name, filename)


def complex_dir_path11(instance, filename):
    name = instance.site.site.name
    return _get_name(name, filename)

class LivingPropertyType(models.TextChoices):
    PRIMARY = 'PRIMARY', 'Первичная недвижимость'
    RESALE = 'RESALE', 'Вторичная недвижимость'



class SiteData(models.Model):
    site = models.OneToOneField(
        Site,
        verbose_name='Сайт',
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
        return f'{self.site.name}'

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
    
    def get_lang(self):
        dubai_en = 'statusprime.com'
        return 'en' if self.site.domain == dubai_en else 'ru'
    
    def is_en(self):
        return self.get_lang() == 'en'


class LivingType(models.Model):
    site = models.ForeignKey(
        SiteData,
        verbose_name='Сайт',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Название',
        max_length=100
    )
    ltype = models.CharField(
        'Тип недвижимости',
        max_length=25,
        choices=LivingPropertyType.choices,
        default=LivingPropertyType.PRIMARY,
    )

    class Meta:
        verbose_name = 'Тип жилья'
        verbose_name_plural = 'Типы жилья'

    def __str__(self) -> str:
        return f'{self.site_name[:2].upper()}: - {self.name}, ({self.ltype})'

    @property
    def site_name(self):
        return self.site.site.name

class YouTubeLink(models.Model):
    site = models.ForeignKey(
        SiteData,
        verbose_name='Сайт',
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
        self.link = re.sub('watch?v=', 'emodels_baseed/', self.link)
        self.link = re.sub(
            'youtu.be/', 'youtube.com/emodels_baseed/', self.link)
        super(YouTubeLink, self).save(*args, **kwargs)


class MainSlider(models.Model):
    site = models.ForeignKey(
        SiteData,
        verbose_name='Сайт',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        "Фото",
        upload_to=complex_dir_path11
    )
    logo = models.FileField(
        "Лого",
        upload_to=complex_dir_path11,
        validators=[validate_logo]
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
    site = models.ForeignKey(
        SiteData,
        verbose_name='Сайт',
        on_delete=models.CASCADE,
    )
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
    def peculiarity(self):
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


class PropertyBase(models.Model):
    site = models.ForeignKey(
        SiteData,
        verbose_name='Сайт',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        'Название лота',
        max_length=80
    )
    slug = models.SlugField(
        'Назваие в url'
    )
    addres = models.CharField(
        'Адрес',
        max_length=100
    )
    price = models.CharField(
        'Цена лота',
        help_text='Минимальная цена лота в комплексе',
        max_length=80
    )
    map_script = models.TextField(
        'Скрипт карты',
        max_length=500
    )
    description = RichTextField(
        verbose_name='Полное описание лота',
        help_text=' До 2000 символов',
        max_length=2000
    )
    title_image = models.ImageField(
        'Обложка',
        help_text='Фотография на странице лота',
        upload_to=complex_dir_path,
    )
    click_amount = models.BigIntegerField(
        'Кол-во нажатий',
        default=0
    )
    main_order = models.IntegerField(
        'Порадок на главной странице',
        help_text='Показываются все обьекты с не нулевыми значениями.',
        default=0
    )
    area = models.ForeignKey(
        Area,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Район'
    )
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Специалист'
    )
    rooms_number = models.IntegerField(
        'Кол-во комнат',
        **nb
    )
    decor = models.CharField(
        'Ремонт',
        max_length=80,
        choices=DecorType.choices,
        default=DecorType.EURO,
        blank=True
    )
    living_type = models.ManyToManyField(
        LivingType,
        blank=True, default=None,
        verbose_name='Тип жилья'
    )
    is_published = models.BooleanField(
        'Опубликован',
        help_text='Доступен ли обьект на сайте',
        default=True
    )

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def site_name(self):
        return self.site.site.name


    @property
    def areas_data(self):
        return AreaPeculiarity.objects.filter(area=self.area)



class ImageBase(models.Model):
    name = models.CharField(
        'Название',
        max_length=180
    )
    photo = models.ImageField(
        "Фото",
        upload_to=complex_dir_path, **nb
    )
    description = models.CharField(
        'Описание',
        max_length=500,
        blank=True,
        default=''
    )

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
        abstract = True

    def __str__(self) -> str:
        return f'{self.name}'

