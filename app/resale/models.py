from django.db import models
from aproperty.models import *
from django.urls import reverse

# Create your models here.

class ResaleProperty(models.Model):
    site = models.ForeignKey(
        SiteData,
        on_delete=models.CASCADE,
        verbose_name='Сайт'
    )
    name = models.CharField(
        'Название лота',
        max_length=120
    )
    slug = models.SlugField(
        'Назваие в url'
    )
    square = models.IntegerField(
        'Площядть',
        **nb
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
    map_script = models.TextField(
        'Скрипт карты',
        max_length=500
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
    click_amount = models.BigIntegerField(
        'Кол-во нажатий',
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
        default=True,
    )

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
        return ReImage.objects.filter(property=self)
    


class ReImage(models.Model):
    property = models.ForeignKey(
        ResaleProperty,
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