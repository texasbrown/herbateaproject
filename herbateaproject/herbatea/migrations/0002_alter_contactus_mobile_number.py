# Generated by Django 4.1.3 on 2022-11-28 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herbatea', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]