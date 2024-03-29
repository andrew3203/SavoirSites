# Generated by Django 4.0 on 2023-02-08 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primary', '0006_alter_primaryproperty_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='primaryproperty',
            name='logo',
        ),
        migrations.AddField(
            model_name='primaryproperty',
            name='decor',
            field=models.CharField(blank=True, choices=[('NO', 'Без отделки'), ('SIMPLE', 'WhiteBox'), ('EURO', 'С отделкой'), ('DESIGN', 'Дизайнерский')], default='EURO', max_length=80, verbose_name='Ремонт'),
        ),
        migrations.AddField(
            model_name='primaryproperty',
            name='rooms_number',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Кол-во комнат'),
        ),
    ]
