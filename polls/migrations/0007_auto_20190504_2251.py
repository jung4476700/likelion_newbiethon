# Generated by Django 2.1.8 on 2019-05-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_remove_polls_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polls',
            name='video_key',
            field=models.CharField(max_length=50),
        ),
    ]
