# Generated by Django 4.2.5 on 2023-10-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0010_me_requested_stipend'),
    ]

    operations = [
        migrations.CreateModel(
            name='work_experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان شغلی')),
                ('date_start_work', models.DateField(verbose_name='تاریخ شروع شغل')),
                ('date_end_work', models.DateField(verbose_name='تاریخ پایان شغل')),
                ('description', models.TextField(max_length=1700, verbose_name='توضیحات شغل')),
            ],
            options={
                'verbose_name': 'عنوان شغل',
                'verbose_name_plural': 'عناوین شغلی',
            },
        ),
        migrations.AddField(
            model_name='me',
            name='biography',
            field=models.CharField(default=1, max_length=600, verbose_name='بیوگرافی'),
            preserve_default=False,
        ),
    ]