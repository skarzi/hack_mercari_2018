# Generated by Django 2.1.2 on 2018-10-20 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('preferences', '0001_initial'),
        ('deliveries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='recipient_preference',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='preferences.MeetingPreference'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='sender_preference',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='preferences.MeetingPreference'),
        ),
    ]