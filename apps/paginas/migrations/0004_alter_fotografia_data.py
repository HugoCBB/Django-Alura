# Generated by Django 5.0.7 on 2024-07-17 00:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_alter_fotografia_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='data',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]