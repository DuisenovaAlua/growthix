# Generated by Django 2.1.3 on 2018-12-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('things', '0008_auto_20181217_0943'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DataTime',
        ),
        migrations.RemoveField(
            model_name='user3',
            name='user',
        ),
        migrations.AddField(
            model_name='user2',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='User3',
        ),
    ]
