# Generated by Django 2.0.8 on 2018-08-30 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
