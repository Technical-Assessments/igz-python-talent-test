# Generated by Django 4.0.1 on 2022-02-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mathapi', '0002_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='string',
            name='output_data',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
