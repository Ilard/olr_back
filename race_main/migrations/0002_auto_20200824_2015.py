# Generated by Django 3.1 on 2020-08-24 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('race_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingame',
            name='player2_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='player3_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ingame',
            name='player4_name',
            field=models.CharField(default='', max_length=20, null=True),
        ),
    ]
