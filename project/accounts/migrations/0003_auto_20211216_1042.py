# Generated by Django 3.2.9 on 2021-12-16 10:42

import accounts.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_log_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='age',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='سن'),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='نوسینده می باشد؟'),
        ),
        migrations.AddField(
            model_name='profile',
            name='resume',
            field=models.FileField(null=True, upload_to=accounts.utils.get_file_path, verbose_name='رزومه'),
        ),
    ]
