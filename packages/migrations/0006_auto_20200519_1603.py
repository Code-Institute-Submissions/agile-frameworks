# Generated by Django 3.0.6 on 2020-05-19 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0005_auto_20200519_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
