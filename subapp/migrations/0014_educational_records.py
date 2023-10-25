# Generated by Django 4.2.5 on 2023-10-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0013_alter_me_biography'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educational_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان تحصیلی')),
                ('date_start_work', models.DateField(verbose_name='تاریخ شروع تحصیل')),
                ('date_end_work', models.DateField(verbose_name='تاریخ پایان تحصیل')),
                ('description', models.TextField(max_length=1700, verbose_name='توضیحات تحصیلات')),
            ],
            options={
                'verbose_name': 'سابقه تحصیل',
                'verbose_name_plural': 'سوابق تحصیلات',
            },
        ),
    ]
