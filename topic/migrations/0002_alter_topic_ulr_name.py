# Generated by Django 3.2.6 on 2022-01-12 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='ulr_name',
            field=models.SlugField(),
        ),
    ]
