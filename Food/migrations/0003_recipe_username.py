# Generated by Django 5.0 on 2024-01-08 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Food', '0002_recipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='username',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
