from django.db import models
import re
from django.urls import reverse
from aproperty.models import *
from django.utils.translation import gettext as _


class PrimaryProperty(PropertyBase):
    lots_number = models.IntegerField(
        'Кол-во лотов',
        default=0,
    )
    district = models.CharField(
        'Округ',
        max_length=100,
        default='',
        blank=True
    )
    subway = models.CharField(
        'Метро',
        max_length=100,
        default='',
        blank=True
    )
    lots_numodels_baseer = models.CharField(
        'Кол-во лотов',
        max_length=100,
        default='по запросу',
        blank=True
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
    second_image = models.ImageField(
        'Доп. фото',
        help_text='Первая фото в фотографиях комплекса',
        upload_to=complex_dir_path,
        **nb
    )
    logo = models.FileField(
        'Логотип',
        upload_to=complex_dir_path,
        null=True, blank=True,
        validators=[validate_logo]
    )
    presentation = models.FileField(
        'Презентация лота',
        upload_to=complex_dir_path,
        **nb
    )

    class Meta:
        verbose_name = 'Новостройка'
        verbose_name_plural = 'Новостройки'

    def __str__(self) -> str:
        return f'{self.name}'

    @property
    def images(self):
        return Image.objects.filter(property=self)
    
    @property
    def url(self):
        return reverse('primary-detail', args=[str(self.id)])

    @property
    def get_absolute_url(self):
        return reverse('my-primary', args=[str(self.slug)])
    
    @property
    def price_from(self) -> str:
        price = re.findall('\d+', self.price.replace(' ', ''))
        if price:
            price = int(price[0])
            if price != 0 and self.min_square != 0:
                return f"{int(price / self.min_square)}"
        return _('по запросу')
        
    @property
    def squares(self):
        return self.min_square

    @property
    def get_logo(self) -> str:
        if self.logo:
            return self.logo.url
        else:
            return ''

    def get_recomend(self):
        queryset = PrimaryProperty.objects.filter(
            site=self.site,
            is_published=True,
        ).exclude(name=self.name).order_by('-click_amount')
        end = min(12, queryset.count())
        return queryset[:end]


class Image(ImageBase):
    property = models.ForeignKey(
        PrimaryProperty,
        on_delete=models.CASCADE,
        verbose_name='Обьект недвижимости'
    )
