# Generated by Django 4.1 on 2022-09-03 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snap_analyzer_django', '0011_enclosuremodel_node_id_1_wwnn'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enclosuremodel',
            old_name='name_node_id_1',
            new_name='id_node_left',
        ),
        migrations.AddField(
            model_name='enclosuremodel',
            name='name_node_left',
            field=models.CharField(default='Null', max_length=40),
            preserve_default=False,
        ),
    ]
