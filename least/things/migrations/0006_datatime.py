# Generated by Django 2.1.3 on 2018-12-10 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0005_auto_20181210_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
            ],
        ),
    ]
