# Generated by Django 4.2.6 on 2023-11-06 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roster_1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazv', models.CharField(max_length=200, verbose_name='название')),
                ('form', models.CharField(max_length=200, verbose_name='формат')),
                ('r', models.TextField(verbose_name='ростер')),
            ],
        ),
        migrations.DeleteModel(
            name='AAA',
        ),
    ]
