# Generated by Django 5.0.1 on 2024-02-07 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_Accounts', '0002_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='example@example.com', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]