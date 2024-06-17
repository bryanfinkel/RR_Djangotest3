# Generated by Django 5.0.6 on 2024-06-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('Level', models.CharField(max_length=25)),
                ('Status', models.CharField(max_length=25)),
                ('Sponsor', models.CharField(max_length=25)),
                ('Classrooms', models.IntegerField()),
            ],
        ),
    ]
