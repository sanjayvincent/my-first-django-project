# Generated by Django 2.0.8 on 2018-08-30 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('sex', models.CharField(blank=True, choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('UNSURE', 'Unsure')], max_length=10, null=True, verbose_name='Specify your sex')),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]