# Generated by Django 4.2.5 on 2023-10-30 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_sessions', '0005_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tables',
            name='is_full',
            field=models.BooleanField(default=False),
        ),
    ]
