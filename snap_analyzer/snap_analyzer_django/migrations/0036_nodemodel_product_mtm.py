# Generated by Django 4.1 on 2022-09-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap_analyzer_django', '0035_nodemodel_service_subnet_mask'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodemodel',
            name='product_mtm',
            field=models.CharField(default='Машина', max_length=40),
            preserve_default=False,
        ),
    ]
