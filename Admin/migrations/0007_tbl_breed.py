# Generated by Django 5.1.3 on 2024-12-07 06:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0006_tbl_pettype'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_name', models.CharField(max_length=30)),
                ('pettype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_pettype')),
            ],
        ),
    ]
