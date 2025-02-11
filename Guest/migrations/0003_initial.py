# Generated by Django 5.1.3 on 2024-12-06 05:58

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0005_tbl_subcategory'),
        ('Guest', '0002_delete_tbl_userreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_userreg',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=40)),
                ('user_address', models.CharField(max_length=40)),
                ('user_contact', models.CharField(max_length=40)),
                ('user_email', models.CharField(max_length=40)),
                ('user_photo', models.URLField()),
                ('user_gender', models.CharField(max_length=40)),
                ('user_dob', models.DateField()),
                ('user_password', models.CharField(max_length=40)),
                ('user_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
