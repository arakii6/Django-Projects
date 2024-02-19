# Generated by Django 5.0.1 on 2024-01-12 17:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_department_options_alter_student_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_Name', models.CharField(max_length=100)),
                ('Customer_Age', models.SmallIntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Amount', models.IntegerField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CP', to='Accounts.customer')),
            ],
        ),
    ]
