# Generated by Django 3.2.6 on 2021-10-16 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0004_remove_categoria_premio_categoria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Premio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premio', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juego.categoria')),
            ],
        ),
        migrations.DeleteModel(
            name='Nivel',
        ),
    ]
