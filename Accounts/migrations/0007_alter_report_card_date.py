# Generated by Django 5.0.1 on 2024-01-31 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_report_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report_card',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
