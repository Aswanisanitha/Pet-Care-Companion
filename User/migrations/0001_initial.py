# Generated by Django 5.1.3 on 2024-12-07 17:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0012_tbl_traning'),
        ('Guest', '0005_alter_tbl_userreg_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=30)),
                ('pet_weight', models.CharField(max_length=30)),
                ('pet_photo', models.URLField()),
                ('pet_age', models.CharField(max_length=30)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_breed')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_userreg')),
            ],
        ),
    ]
