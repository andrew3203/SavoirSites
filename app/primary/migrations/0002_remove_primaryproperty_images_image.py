# Generated by Django 4.0 on 2022-10-16 20:45

import aproperty.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aproperty', '0002_remove_image_site_alter_sitedata_options'),
        ('primary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primaryproperty',
            name='images',
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=180, verbose_name='Название')),
                ('photo', models.ImageField(blank=True, default=None, null=True, upload_to=aproperty.models.complex_dir_path, verbose_name='Фото')),
                ('description', models.TextField(blank=True, default='', max_length=500, verbose_name='Описание')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='primary.primaryproperty', verbose_name='Обьект недвижимости')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aproperty.sitedata', verbose_name='Сайт')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фотографии',
                'ordering': ['-name'],
            },
        ),
    ]