# Generated by Django 3.2.7 on 2022-09-20 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.TextField(blank=True, default='', help_text='Должность или группа', verbose_name='Должность/Группа'),
        ),
    ]