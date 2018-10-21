# Generated by Django 2.1.2 on 2018-10-20 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0004_auto_20181020_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='status',
            field=models.CharField(choices=[('assigning', 'Assigning to courier'), ('waiting_for_courier', 'Waiting for courier to pick up'), ('in_transit', "Package is on it's way"), ('delivered', 'Package delivered')], default='assigning', max_length=32),
        ),
    ]