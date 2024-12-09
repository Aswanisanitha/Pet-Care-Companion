# Generated by Django 5.1.3 on 2024-12-09 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_vetinaryhospital'),
        ('User', '0007_delete_tbl_foodplan'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_date', models.DateField()),
                ('appoinment_time', models.TimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userreg')),
                ('vetinaryhospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_vetinaryhospital')),
            ],
        ),
    ]
