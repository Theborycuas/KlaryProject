# Generated by Django 4.0.3 on 2022-03-17 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provinces', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='province',
            old_name='created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='province',
            old_name='update',
            new_name='update_at',
        ),
    ]
