# Generated by Django 2.1.8 on 2019-05-04 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_auto_20190504_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='apply',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]
