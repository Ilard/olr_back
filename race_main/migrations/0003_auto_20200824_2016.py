# Generated by Django 3.1 on 2020-08-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_main', '0002_auto_20200824_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingame',
            name='player2_name',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='player3_name',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='player4_name',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]