# Generated by Django 2.1.2 on 2018-10-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0002_auto_20181020_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
