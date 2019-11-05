# Generated by Django 2.1 on 2018-09-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180923_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('O', 'Open'), ('IP', 'InProgress'), ('C', 'Closed')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='issue',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
