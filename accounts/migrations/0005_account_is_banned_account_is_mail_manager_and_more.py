# Generated by Django 4.0.6 on 2022-08-25 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_account_vendor_req_status_account_vendor_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_banned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_mail_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='vendor_req_rejection_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='vendor_req_status',
            field=models.BooleanField(default=False),
        ),
    ]