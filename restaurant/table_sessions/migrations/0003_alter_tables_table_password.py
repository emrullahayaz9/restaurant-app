# Generated by Django 4.2.5 on 2023-10-30 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_sessions', '0002_tables_table_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tables',
            name='table_password',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
