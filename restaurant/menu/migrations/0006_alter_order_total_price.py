# Generated by Django 4.2.5 on 2023-10-31 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_alter_order_table_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0),
        ),
    ]