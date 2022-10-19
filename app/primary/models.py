from django.db import models
from aproperty.models import *
import re
from django.urls import reverse


# Create your models here.
nb = dict(null=True, blank=True, default=None)

class PrimaryProperty(models.Model):
    site = models.ForeignKey(
        SiteData,
        on_delete=models.CASCADE,
        verbose_name='Сайт'
    )
    name = models.CharField(
        'Название лота',
        max_length=80
    )
    slug = models.SlugField(
        'Назваие в url'
    )
    price = models.CharField(
        'Цена лота',
        help_text='Минимальная цена лота в комплексе',
        max_length=80
    )
    addres = models.CharField(
        'Адрес',
        max_length=100
    )
    district = models.CharField(
        'Округ',
        max_length=50,
        default='',
        blank=True
    )
    subway = models.CharField(
        'Метро',
        max_length=100,
        default='',
        blank=True
    )
    lots_number = models.CharField(
        'Кол-во лотов',
        max_length=100,
        default='по запросу',
        blank=True
    )
    map_script = models.TextField(
        'Скрипт карты',
        max_length=500
    )
    min_square = models.BigIntegerField(
        'Минимальная площядь',
        default=10
    )
    max_square = models.BigIntegerField(
        'Максимальная площядь',
        default=500
    )
    short_phrase = models.TextField(
        'Короткая фраза',
        help_text='Яркая и короткая фраза, отображается на странице лота',
        max_length=250
    )
    description = models.TextField(
        'Полное описание лота',
        help_text='Можно использовать html, до 1500 символов',
        max_length=1500
    )
    title_image = models.ImageField(
        'Обложка',
        help_text='Фотография на странице лота',
        upload_to=complex_dir_path,
    )
    second_image = models.ImageField(
        'Доп. фото',
        help_text='Первая фото в фотографиях комплекса',
        upload_to=complex_dir_path,
         **nb
    )
    logo = models.ImageField(
        'Логотип',
        upload_to=complex_dir_path,
        null=True, blank=True
    )
    presentation = models.FileField(
        'Презентация лота',
        upload_to=complex_dir_path,
         **nb
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
    is_published = models.BooleanField(
        'Опубликован',
        help_text='Доступен ли обьект на сайте',
        default=True
    )

    class Meta:
        verbose_name = 'Новостройка'
        verbose_name_plural = 'Новостройки'
        ordering = ['-name']
    
    def __str__(self) -> str:
        return f'{self.name}'
    
    def get_absolute_url(self):       
        return reverse('primary', args=[str(self.slug)])
    
    @property
    def url(self):
        return self.get_absolute_url()
        
    @property
    def site_name(self):
        return self.site.site.name
    
    @property
    def site_domain(self):
        return self.site.site.domain
    
    @property
    def areas_data(self):
        return AreaPeculiarity.objects.filter(area=self.area)
    
    @property
    def images(self):
        return Image.objects.filter(property=self)
    
    @property
    def price_from(self):
        price = re.findall('\d+', self.price.replace(' ', ''))
        if price:
            price = int(price[0])
            if price != 0 and self.min_square != 0:
                return f'От  {price / self.min_square:,.0f}'.replace(',', ' ')
        return 'по запросу'
    
    @property
    def price_from_en(self):
        price = re.findall('\d+', self.price.replace(' ', ''))
        if price:
            price = int(price[0])
            if price != 0 and self.min_square != 0:
                return f'from  {price / self.min_square:,.0f}'.replace(',', ' ')
        return 'on request'
    
    @property
    def squares(self):
        if self.min_square == 0 and self.max_square == 0:
            return 'Метраж - по запросу'
        return f'Метраж от {self.min_square} до {self.max_square}'
    
    @property
    def squares_en(self):
        if self.min_square == 0 and self.max_square == 0:
            return 'Metters - on requests'
        return f'from {self.min_square} to {self.max_square}'
    
    @property
    def get_logo(self):
        if self.logo:
            return self.logo.url
        return ''
    
    def get_recomend(self):
        queryset = PrimaryProperty.objects.filter(
            site=self.site
        ).exclude(name=self.name).order_by('-click_amount')
        return queryset[:12]
    
    
class Image(models.Model):
    property = models.ForeignKey(
        PrimaryProperty,
        on_delete=models.CASCADE,
        verbose_name='Обьект недвижимости'
    )
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
        ordering = ['-name']

    def __str__(self) -> str:
        return f'{self.name}'
