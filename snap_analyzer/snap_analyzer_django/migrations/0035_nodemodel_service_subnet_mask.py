# Generated by Django 4.1 on 2022-09-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap_analyzer_django', '0034_nodemodel_service_gateway'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodemodel',
            name='service_subnet_mask',
            field=models.CharField(default='2.2.2.2', max_length=40),
            preserve_default=False,
        ),
    ]
