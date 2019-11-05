# Generated by Django 2.1 on 2018-09-23 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180923_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('O', 'Open'), ('O', 'InProgress'), ('C', 'Closed')], default='O', max_length=1),
        ),
    ]
