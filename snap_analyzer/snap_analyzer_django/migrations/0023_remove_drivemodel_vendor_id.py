# Generated by Django 4.1 on 2022-09-12 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snap_analyzer_django', '0022_drivemodel_vendor_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drivemodel',
            name='vendor_id',
        ),
    ]
