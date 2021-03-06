# Generated by Django 3.2.9 on 2021-12-16 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20211216_1042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name': 'لاگ', 'verbose_name_plural': 'لاگ ها'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'کاربری', 'verbose_name_plural': 'کاربری ها'},
        ),
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال'),
        ),
    ]
