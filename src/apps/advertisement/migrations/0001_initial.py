# Generated by Django 4.1.6 on 2023-03-10 13:05

import django.db.models.deletion
import multiselectfield.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                (
                    'type',
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ('EXCHANGE', 'Обмен'),
                            ('SELL', 'Продам'),
                            ('BUY', 'Куплю'),
                            ('GIVE', 'Отдам'),
                            ('TAKE', 'Возьму'),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    'urgency',
                    models.CharField(
                        choices=[('URGENT', 'Срочно'), ('NSU', 'Не очень срочно'), ('NAAU', 'Совсем не срочно')],
                        max_length=6,
                    ),
                ),
                (
                    'image',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name='images',
                        to='advertisement.image',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
    ]