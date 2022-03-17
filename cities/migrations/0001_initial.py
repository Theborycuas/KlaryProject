# Generated by Django 4.0.3 on 2022-03-17 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('provinces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=25, verbose_name='Nombre de la Ciudad')),
                ('city_state', models.BooleanField(default=False, verbose_name='Estado de la Ciudad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
                ('province_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='provinces.province', verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'ciudad',
                'verbose_name_plural': 'ciudades',
            },
        ),
    ]