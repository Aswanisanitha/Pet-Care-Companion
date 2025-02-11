# Generated by Django 5.1.3 on 2024-12-13 09:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_alter_tbl_appoinment_appoinment_token_tbl_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_vaccinedetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_name', models.CharField(max_length=30)),
                ('vaccine_details', models.CharField(max_length=30)),
                ('vaccine_date', models.DateField()),
                ('vaccine_fordate', models.DateField()),
                ('pet_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.tbl_pet')),
            ],
        ),
    ]
