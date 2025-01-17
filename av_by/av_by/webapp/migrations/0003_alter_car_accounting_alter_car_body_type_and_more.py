# Generated by Django 5.0 on 2024-01-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_car_phone_remove_car_phone2_remove_car_phone3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='accounting',
            field=models.CharField(max_length=100, verbose_name='Учёт'),
        ),
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(max_length=200, verbose_name='Кузов'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=100, verbose_name='Марка'),
        ),
        migrations.AlterField(
            model_name='car',
            name='city',
            field=models.CharField(max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(default='Белый', max_length=200, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='car',
            name='drive_unit',
            field=models.CharField(max_length=200, verbose_name='Привод'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_type',
            field=models.CharField(max_length=200, verbose_name='Тип двигателя'),
        ),
        migrations.AlterField(
            model_name='car',
            name='engine_volume',
            field=models.CharField(max_length=200, verbose_name='Объём двигателя'),
        ),
        migrations.AlterField(
            model_name='car',
            name='interior_color',
            field=models.CharField(default='комби', max_length=100, verbose_name='Цвет салона'),
        ),
        migrations.AlterField(
            model_name='car',
            name='interior_material',
            field=models.CharField(default='ткань', max_length=100, verbose_name='Материал салона'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=100, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='region',
            field=models.CharField(max_length=200, verbose_name='Область'),
        ),
        migrations.AlterField(
            model_name='car',
            name='registration_country',
            field=models.CharField(max_length=100, verbose_name='Страна регистрации'),
        ),
        migrations.AlterField(
            model_name='car',
            name='state',
            field=models.CharField(max_length=100, verbose_name='Состояние'),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(max_length=200, verbose_name='Коробка передач'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.CharField(max_length=200, verbose_name='Год'),
        ),
    ]
