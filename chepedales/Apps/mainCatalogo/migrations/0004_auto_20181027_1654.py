# Generated by Django 2.0 on 2018-10-27 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCatalogo', '0003_auto_20181027_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacionpedal',
            name='imgPedal',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]