# Generated by Django 3.2.7 on 2022-09-25 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20220925_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='is_spec_equip',
            field=models.BooleanField(default=False, verbose_name='Является ли оборудование специальным'),
        ),
    ]
