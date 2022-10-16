from django.db import models
from aproperty.models import *
from primary.models import *

# Create your models here.

class ResaleProperty(PrimaryProperty):

    min_square = None
    max_square = None

    rooms_number = models.IntegerField(
        'Кол-во комнат',
        **nb
    )
    floor = models.IntegerField(
        'Этаж',
        **nb
    )
    floor_number = models.IntegerField(
        'Кол-во этажей в доме',
        **nb
    )
    decor = models.CharField(
        'Ремонт',
        max_length=80,
        **nb
    )
    construction_year = models.DateField(
        'Год постройки',
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
    parking = models.BooleanField(
        'Парковка',
        default=False
    )
    ownership = models.IntegerField(
        'Форма собственности',
        **nb
    )
    entrances = models.IntegerField(
        'Кол во подъездов',
        **nb
    )
    rooms_on_floor = models.IntegerField(
        'Квартир на этаже',
        **nb
    )
    penthouse = models.BooleanField(
        'Пентхаус',
        default=False
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
    

    class Meta:
        verbose_name = 'Втричная недвижимость'
        verbose_name_plural = 'Втричная недвижимость'
        ordering = ['-name']
    


