# Generated by Django 3.0b1 on 2019-11-02 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('imgpath', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.CharField(max_length=100, verbose_name='Описание')),
                ('logo', models.CharField(max_length=100, verbose_name='Логотип')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='app.Category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'PHONE'), (2, 'FACEBOOK'), (3, 'EMAIL')], default=1)),
                ('value', models.CharField(max_length=150)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='app.Course')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=100, verbose_name='Широта')),
                ('longitude', models.CharField(max_length=100, verbose_name='Долгота')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branches', to='app.Course')),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
            },
        ),
    ]