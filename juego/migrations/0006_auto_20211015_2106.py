# Generated by Django 3.2.6 on 2021-10-16 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0005_auto_20211015_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='premio',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Premio',
        ),
    ]