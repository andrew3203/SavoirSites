from django.db import models
from aproperty.models import *
from django.urls import reverse

# Create your models here.

class DecorType(models.TextChoices):
    NO = 'NO', 'Без ремонта'
    SIMPLE = 'SIMPLE', 'Косметический'
    EURO = 'EURO', 'Евроремонт'
    DESIGN = 'DESIGN', 'Дизайнерский'
    


class ResaleProperty(PropertyBase):
    square = models.IntegerField(
        'Площадь',
        **nb
    )
    rooms_number = models.IntegerField(
        'Кол-во комнат',
        **nb
    )
    floor = models.IntegerField(
        'Этаж',
        **nb
    )
    floors_number= models.IntegerField(
        'Кол-во этажей в доме',
        **nb
    )
    decor = models.CharField(
        'Ремонт',
        max_length=80,
        choices=DecorType.choices,
        default=DecorType.NO,
        blank=True
    )
    construction_year = models.CharField(
        'Год постройки',
        max_length=20,
        **nb
    )
    bulding_material = models.CharField(
        'Тип (материал) дома',
        max_length=100,
        **nb
    )
    ceiling_height = models.FloatField(
        'Высота потолков',
        **nb
    )
    elevators = models.IntegerField(
        'Пассажирских лифтов',
        **nb
    )
    freight_elevators = models.IntegerField(
        'Грузовых лифтов',
        **nb
    )
    parking = models.CharField(
        'Парковка',
        max_length=100, **nb
    )
    ownership = models.CharField(
        'Форма собственности',
        max_length=100, **nb
    )
    entrances = models.IntegerField(
        'Кол во подъездов',
        **nb
    )
    rooms_on_floor = models.IntegerField(
        'Квартир на этаже',
        **nb
    )
    terrace = models.BooleanField(
        'Терраса',
        default=False
    )
    rooms_in_hous = models.IntegerField(
        'Квартир в доме',
        **nb
    )
    window_to = models.CharField(
        'Окна выходят',
        max_length=100,
        **nb
    )
    living_type = models.ManyToManyField(
        LivingType,
        blank=True, default=None,
        verbose_name='Тип жилья'
    )

    
    class Meta:
        verbose_name = 'Втричная недвижимость'
        verbose_name_plural = 'Втричная недвижимость'

    
    @property
    def images(self):
        return Image.objects.filter(property=self)
    
    def get_recomend(self):
        queryset = ResaleProperty.objects.filter(
            site=self.site,
            is_published=True,
        ).exclude(name=self.name).order_by('-click_amount')
        end = min(12, queryset.count())
        return queryset[:end]
    

class Image(ImageBase):
    property = models.ForeignKey(
        ResaleProperty,
        on_delete=models.CASCADE,
        verbose_name='Обьект недвижимости'
    )