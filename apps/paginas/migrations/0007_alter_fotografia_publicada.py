# Generated by Django 5.1 on 2024-08-28 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0006_fotografia_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotografia',
            name='publicada',
            field=models.BooleanField(default=True),
        ),
    ]
