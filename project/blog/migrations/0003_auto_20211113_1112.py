# Generated by Django 3.2.9 on 2021-11-13 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211113_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '  دسته بندی', 'verbose_name_plural': '  دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': '    کامنت', 'verbose_name_plural': '    کامنت ها'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': ' پست', 'verbose_name_plural': ' پست ها'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '   تگ', 'verbose_name_plural': '   تگ ها'},
        ),
    ]
