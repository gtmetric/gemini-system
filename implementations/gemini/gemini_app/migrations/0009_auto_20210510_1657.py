# Generated by Django 3.2 on 2021-05-10 09:57

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gemini_app', '0008_auto_20210510_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='scienceplan',
            name='plan_no',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='end_date',
            field=models.DateTimeField(default='10/05/2021 09:57:27', validators=[django.core.validators.MinValueValidator(datetime.datetime(2021, 5, 10, 9, 57, 27, 18739, tzinfo=utc), message='The end date is invalid.')]),
        ),
        migrations.AlterField(
            model_name='scienceplan',
            name='start_date',
            field=models.DateTimeField(default='10/05/2021 09:57:27', validators=[django.core.validators.MinValueValidator(datetime.datetime(2021, 5, 10, 9, 57, 27, 18739, tzinfo=utc), message='The start date is invalid.')]),
        ),
    ]