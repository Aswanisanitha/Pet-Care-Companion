# Generated by Django 5.1.3 on 2024-12-12 09:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_vetinaryhospital'),
        ('User', '0010_delete_tbl_appoinment'),
        ('Vetinaryhospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_appoinment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appoinment_date', models.DateField(auto_now_add=True)),
                ('appoinment_Fordate', models.DateField()),
                ('appoinment_status', models.IntegerField(default=0)),
                ('slot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vetinaryhospital.tbl_slot')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userreg')),
            ],
        ),
    ]
