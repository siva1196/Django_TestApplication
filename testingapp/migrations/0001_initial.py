# Generated by Django 3.2.9 on 2021-12-14 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('Gender', models.TextField()),
                ('City', models.TextField()),
                ('Mobile', models.IntegerField()),
                ('Email', models.TextField()),
                ('Username', models.CharField(max_length=6)),
            ],
        ),
    ]
