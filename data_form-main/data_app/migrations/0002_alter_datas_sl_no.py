# Generated by Django 4.2.2 on 2023-06-07 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datas',
            name='SL_NO',
            field=models.IntegerField(),
        ),
    ]