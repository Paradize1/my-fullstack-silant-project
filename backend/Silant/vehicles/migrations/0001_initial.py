# Generated by Django 5.0.7 on 2024-07-16 22:10

import datetime
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
            name='ControlledBridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель управляемого моста',
                'verbose_name_plural': 'Модели управляемых мостов',
            },
        ),
        migrations.CreateModel(
            name='DrivingBridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель ведущего моста',
                'verbose_name_plural': 'Модели ведущих мостов',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель двигателя',
                'verbose_name_plural': 'Модели двигателей',
            },
        ),
        migrations.CreateModel(
            name='Failure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Характер отказа',
                'verbose_name_plural': 'Характеры отказа',
            },
        ),
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Способ восстановления',
                'verbose_name_plural': 'Способы восстановления',
            },
        ),
        migrations.CreateModel(
            name='ServiceCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Сервисная компания',
                'verbose_name_plural': 'Сервисные компании',
            },
        ),
        migrations.CreateModel(
            name='Technic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель техники',
                'verbose_name_plural': 'Модели техники',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Модель трансмиссии',
                'verbose_name_plural': 'Модели трансмиссий',
            },
        ),
        migrations.CreateModel(
            name='TypeMaintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Вид технического обслуживания',
                'verbose_name_plural': 'Виды технических обслуживаний',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=12, unique=True, verbose_name='Зав. № машины')),
                ('engine_number', models.CharField(max_length=12, verbose_name='Зав. № двигателя')),
                ('transmission_number', models.CharField(max_length=12, verbose_name='Зав. № трансмиссии')),
                ('driving_bridge_number', models.CharField(max_length=12, verbose_name='Зав. № ведущего моста')),
                ('controlled_bridge_number', models.CharField(max_length=12, verbose_name='Зав. № управляемого моста')),
                ('date_shipment', models.DateField(default=datetime.datetime.now, verbose_name='Дата отгрузки с завода')),
                ('consignee', models.CharField(max_length=200, verbose_name='Грузополучатель (конечный потребитель)')),
                ('delivery_address', models.CharField(max_length=200, verbose_name='Адрес поставки (эксплуатации)')),
                ('equipment', models.TextField(default='Стандарт', verbose_name='Комплектация (доп. опции)')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('controlled_bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.controlledbridge', verbose_name='Модель управляемого моста')),
                ('driving_bridge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.drivingbridge', verbose_name='Модель ведущего моста')),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.engine', verbose_name='Модель двигателя')),
                ('service_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.servicecompany', verbose_name='Сервисная компания')),
                ('technic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.technic', verbose_name='Модель техники')),
                ('transmission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.transmission', verbose_name='Модель трансмиссии')),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_failure', models.DateField(default=datetime.datetime.now, verbose_name='Дата отказа')),
                ('operating_time', models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')),
                ('description_failure', models.TextField(blank=True, null=True, verbose_name='Описание отказа')),
                ('repair_parts', models.TextField(blank=True, null=True, verbose_name='Используемые запасные части')),
                ('date_recovery', models.DateField(default=datetime.datetime.now, verbose_name='Дата восстановления')),
                ('time', models.PositiveIntegerField(default=0, verbose_name='Время')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.car', verbose_name='Машина')),
                ('node_failure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.failure', verbose_name='Узел отказа')),
                ('method_recovery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.recoverymethod', verbose_name='Способ восстановления')),
                ('service_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.servicecompany', verbose_name='Сервисная компания')),
            ],
            options={
                'verbose_name': 'Рекламация',
                'verbose_name_plural': 'Рекламации',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='Дата проведения ТО')),
                ('operating_time', models.PositiveIntegerField(default=0, verbose_name='Наработка, м/час')),
                ('order_number', models.CharField(max_length=20, verbose_name='№ заказ-наряда')),
                ('order_date', models.DateField(default=datetime.datetime.now, verbose_name='Дата заказ-наряда')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.car', verbose_name='Машина')),
                ('service_company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicles.servicecompany', verbose_name='Организация, проводившая ТО')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.typemaintenance', verbose_name='Вид ТО')),
            ],
            options={
                'verbose_name': 'Техническое обслуживание',
                'verbose_name_plural': 'Технические обслуживания',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username_display', models.CharField(blank=True, max_length=150, verbose_name='Отображаемое имя')),
                ('login', models.CharField(max_length=150, unique=True, verbose_name='Логин для входа')),
                ('password', models.CharField(max_length=150, verbose_name='Пароль для входа')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
    ]
