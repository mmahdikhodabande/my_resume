# Generated by Django 4.2.5 on 2023-10-25 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0020_skills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cyberspace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.CharField(max_length=200, verbose_name='لینک اینستگرام')),
                ('X', models.CharField(max_length=200, verbose_name='لینک ایکس(توییتر)')),
                ('Linkedin', models.CharField(max_length=200, verbose_name='لینک لینکدین')),
                ('Github', models.CharField(max_length=200, verbose_name='لینک گیت هاب ')),
            ],
            options={
                'verbose_name': 'آدرس فضای مجازی',
                'verbose_name_plural': 'آدرس های فضاهای مجازی',
            },
        ),
    ]
