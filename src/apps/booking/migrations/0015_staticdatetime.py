# Generated by Django 3.2.7 on 2022-09-26 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_equipment_is_spec_equip'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticDateTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField(null=True, verbose_name='Дата начала бронирования')),
                ('date_end', models.DateField(null=True, verbose_name='Дата конца бронирования')),
                ('start_time', models.TimeField(verbose_name='Время начала брони')),
                ('end_time', models.TimeField(verbose_name='Время конца брони')),
                ('comment', models.TextField(verbose_name='Для кого данная бронь')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='static_date_time', to='booking.room')),
            ],
            options={
                'verbose_name': 'Даты и время для запрета бронирования',
                'verbose_name_plural': 'Даты и время запрета бронирования',
            },
        ),
    ]
