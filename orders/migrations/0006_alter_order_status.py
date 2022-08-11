# Generated by Django 4.0.6 on 2022-08-06 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed')], default='New', max_length=20),
        ),
    ]
