# Generated by Django 3.0.4 on 2020-03-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_auto_20200330_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='destination',
            name='price',
            field=models.IntegerField(),
        ),
    ]
