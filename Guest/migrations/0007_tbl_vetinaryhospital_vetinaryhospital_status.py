# Generated by Django 5.1.3 on 2024-12-12 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0006_tbl_vetinaryhospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_vetinaryhospital',
            name='vetinaryhospital_status',
            field=models.IntegerField(default=0),
        ),
    ]
