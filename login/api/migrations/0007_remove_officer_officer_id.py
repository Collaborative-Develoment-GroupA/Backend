# Generated by Django 4.1.7 on 2023-04-04 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_accident_fault_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officer',
            name='officer_id',
        ),
    ]
