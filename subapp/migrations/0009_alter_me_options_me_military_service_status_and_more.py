# Generated by Django 4.2.5 on 2023-10-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0008_me_technical_expertise_alter_me_gender_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='me',
            options={'verbose_name': ' رزومه شما', 'verbose_name_plural': ' رزومه شما'},
        ),
        migrations.AddField(
            model_name='me',
            name='Military_service_status',
            field=models.CharField(choices=[('پایان خدمت', 'پایان خدمت '), ('معافیت دائم', 'معافیت دائم'), ('معافیت تحصیلی', 'معافیت تحصیلی'), ('در حال انجام ', 'در حال انجام '), ('مشمول', 'مشمول')], default=1, max_length=30, verbose_name='وضعیت خرمت سربازی '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='me',
            name='Nationality',
            field=models.CharField(default=1, max_length=30, verbose_name='ملیت شما'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='me',
            name='Your_current_location',
            field=models.CharField(default=1, max_length=30, verbose_name='موقیعت فعلی شما'),
            preserve_default=False,
        ),
    ]
