# Generated by Django 3.0 on 2020-01-10 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'managed': False, 'ordering': ['album_id']},
        ),
    ]
