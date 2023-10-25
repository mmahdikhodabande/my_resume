# Generated by Django 4.2.5 on 2023-10-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subapp', '0015_me_educational_records'),
    ]

    operations = [
        migrations.CreateModel(
            name='interests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='علافه ها ')),
            ],
            options={
                'verbose_name': 'علاقه ',
                'verbose_name_plural': 'علاقه ها',
            },
        ),
        migrations.CreateModel(
            name='languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='زبان')),
            ],
            options={
                'verbose_name': 'زبان ',
                'verbose_name_plural': 'زبان ها',
            },
        ),
    ]