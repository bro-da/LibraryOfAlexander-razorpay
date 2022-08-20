# Generated by Django 4.0.6 on 2022-08-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Cancelled', 'Cancelled'), ('New', 'New'), ('Accepted', 'Accepted')], default='New', max_length=20),
        ),
    ]
