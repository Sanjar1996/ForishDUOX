# Generated by Django 3.2.6 on 2021-08-16 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0018_alter_xodimmodel_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xodimmodel',
            old_name='full_name',
            new_name='ism',
        ),
    ]
