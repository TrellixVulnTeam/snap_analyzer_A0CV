# Generated by Django 4.1 on 2022-09-14 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap_analyzer_django', '0033_nodemodel_iscsi_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodemodel',
            name='service_gateway',
            field=models.CharField(default='1.1.1.1', max_length=40),
            preserve_default=False,
        ),
    ]
