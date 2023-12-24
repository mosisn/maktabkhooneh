# Generated by Django 4.2 on 2023-12-21 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_course_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='number',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(help_text='price in toman'),
        ),
    ]
