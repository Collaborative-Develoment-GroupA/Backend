# Generated by Django 4.1.7 on 2023-03-30 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_officer_id_alter_officer_officer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='officer',
            name='officer_id',
        ),
        migrations.AlterField(
            model_name='officer',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
