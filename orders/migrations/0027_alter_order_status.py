# Generated by Django 4.0.6 on 2022-08-25 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0026_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Accepted', 'Accepted'), ('New', 'New'), ('Cancelled', 'Cancelled')], default='New', max_length=20),
        ),
    ]
