# Generated by Django 4.2 on 2023-12-22 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_rename_flight_ticket_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='teacher',
        ),
    ]
