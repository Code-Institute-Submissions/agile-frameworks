# Generated by Django 3.0.6 on 2020-05-14 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0003_auto_20200513_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]