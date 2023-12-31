# Generated by Django 3.2.16 on 2023-04-18 10:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('city360', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wrkregg',
            old_name='place',
            new_name='centre',
        ),
        migrations.AddField(
            model_name='wrkregg',
            name='district',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wrkregg',
            name='gender',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wrkregg',
            name='labour_category',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wrkregg',
            name='labour_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wrkregg',
            name='state',
            field=models.CharField(default=django.utils.timezone.now, max_length=150),
            preserve_default=False,
        ),
    ]
