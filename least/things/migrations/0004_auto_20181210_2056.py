# Generated by Django 2.1.3 on 2018-12-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0003_user2_checking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user2',
            name='speciality',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='user2',
            name='university',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
