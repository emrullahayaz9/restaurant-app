# Generated by Django 4.2.5 on 2023-10-29 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='table_number',
            field=models.IntegerField(default=1),
        ),
    ]
