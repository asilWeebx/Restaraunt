# Generated by Django 4.1.6 on 2023-02-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_rename_categoriya_menyu_categoriya'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menyu',
            old_name='Categoriya',
            new_name='Categoriyaa',
        ),
    ]
