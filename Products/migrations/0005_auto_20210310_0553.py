# Generated by Django 2.2.14 on 2021-03-10 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0004_auto_20210309_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_height',
            field=models.PositiveIntegerField(default=100),
        ),
    ]