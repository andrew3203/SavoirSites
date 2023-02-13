from django.db import models
from aproperty.models import *
from django.urls import reverse

# Create your models here.
    


class ResaleProperty(PropertyBase):
    square = models.IntegerField(
        'Площадь',
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
    rooms = models.IntegerField(
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

    
    @property
    def images(self):
        return Image.objects.filter(property=self)
    
    @property
    def url(self):
        return reverse('resale-detail', args=[str(self.id)])
    
    @property
    def get_absolute_url(self):
        return reverse('my-resale', args=[str(self.slug)])
    
    @property
    def squares(self):
        return self.min_square

    
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