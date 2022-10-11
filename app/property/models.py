from django.db import models
import cyrtranslit


# Create your models here.
nb = dict(null=True, blank=True, default=None)

def complex_dir_path(instance, filename):

    name = instance.name.replace(' ', '_')
    dir_name = cyrtranslit.to_latin(name, 'ru').lower()

    filename = filename.replace(' ', '_')
    filename = cyrtranslit.to_latin(filename, 'ru').lower()

    return f'primary/{dir_name}/{filename}'


class Client(models.Model):
    name = models.CharField(
        'ФИО',
        max_length=180
    )
    phone = models.CharField(
        "Телефон",
        max_length=80, **nb
    )
    email = models.CharField(
        'Email',
        max_length=80, **nb
    )
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Image(models.Model):

    name = models.CharField(
        'Название сета',
        max_length=180
    )
    photo = models.ImageField(
        "Фото",
        upload_to=complex_dir_path, **nb
    )
    description = models.TextField(
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

