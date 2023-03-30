# Generated by Django 4.1.6 on 2023-03-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_admin',
            new_name='is_staff',
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='Фамилия'),
        ),
    ]