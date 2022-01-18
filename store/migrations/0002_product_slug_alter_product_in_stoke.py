# Generated by Django 4.0.1 on 2022-01-17 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='test', unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='In_stoke',
            field=models.BooleanField(default=True),
        ),
    ]
