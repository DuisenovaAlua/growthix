# Generated by Django 2.1.3 on 2018-12-10 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0002_auto_20181203_0935'),
    ]

    operations = [
        migrations.AddField(
            model_name='user2',
            name='checking',
            field=models.BooleanField(default=False),
        ),
    ]