# Generated by Django 3.2.7 on 2023-07-12 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city360', '0004_auto_20230712_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='image',
            field=models.ImageField(upload_to='cart_images'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='user_id',
            field=models.IntegerField(),
        ),
    ]
