# Generated by Django 2.2 on 2021-04-12 02:28

import diary.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_auto_20201218_0204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='dt_modified',
        ),
        migrations.AlterField(
            model_name='page',
            name='content',
            field=models.TextField(validators=[diary.validators.validate_no_hash]),
        ),
        migrations.AlterField(
            model_name='page',
            name='feeling',
            field=models.CharField(max_length=80, validators=[diary.validators.validate_no_hash, diary.validators.validate_no_numbers]),
        ),
        migrations.AlterField(
            model_name='page',
            name='score',
            field=models.IntegerField(validators=[diary.validators.validate_score]),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=100, validators=[diary.validators.validate_no_hash]),
        ),
    ]