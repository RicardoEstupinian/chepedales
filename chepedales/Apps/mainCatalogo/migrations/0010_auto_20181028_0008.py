# Generated by Django 2.0 on 2018-10-28 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainCatalogo', '0009_auto_20181027_2355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacionpedal',
            old_name='imagen',
            new_name='imgPedal',
        ),
    ]