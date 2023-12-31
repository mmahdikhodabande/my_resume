# Generated by Django 4.2.5 on 2023-10-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0007_me_scientific_position_alter_me_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='me',
            name='Technical_expertise',
            field=models.CharField(default=1, max_length=30, verbose_name='تخصص فنی شما'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='me',
            name='gender',
            field=models.CharField(choices=[('مرد', 'مرد'), ('زن', 'زن '), ('ترجیح می دهم نگویم', 'ترجیح می دهم نگویم ')], max_length=30, verbose_name='جنسیت'),
        ),
        migrations.AlterField(
            model_name='me',
            name='marital_status',
            field=models.CharField(choices=[('مجرد', 'مجرد'), ('متاهل', 'متاهل ')], max_length=30, verbose_name='وضعیت تاهل '),
        ),
    ]
