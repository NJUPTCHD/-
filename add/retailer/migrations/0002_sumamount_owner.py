# Generated by Django 3.0.3 on 2020-03-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sumamount',
            name='owner',
            field=models.CharField(max_length=16, null=True),
        ),
    ]
