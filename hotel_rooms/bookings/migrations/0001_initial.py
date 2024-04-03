# Generated by Django 5.0.3 on 2024-04-02 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateTimeField(verbose_name='From')),
                ('until_date', models.DateTimeField(verbose_name='Until')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Price')),
                ('payment_id', models.PositiveBigIntegerField(verbose_name='Payment ID')),
                ('user_id', models.PositiveBigIntegerField(verbose_name='User ID')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bookings', to='rooms.room', verbose_name='Room')),
            ],
            options={
                'verbose_name': 'Booking',
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]