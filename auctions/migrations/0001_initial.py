# Generated by Django 5.1.5 on 2025-01-27 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва лоту')),
                ('description', models.TextField(max_length=10000, verbose_name='Опис лоту')),
                ('start_price', models.PositiveBigIntegerField(verbose_name='Стартова ціна лоту')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Очікує на підтвердження'), ('active', 'Активний'), ('expired', 'Час аукціону вийшов'), ('cancelled', 'Аукціон скасовано'), ('payment_pending', 'Очікує на оплату'), ('sold', 'Лот продано'), ('finished', 'Аукціон завершено')], default='pending', max_length=30, verbose_name='Статус лоту')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Користувач, що створив лот')),
            ],
        ),
    ]
