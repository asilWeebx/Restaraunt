# Generated by Django 4.1.6 on 2023-02-10 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_rename_categoriyaa_menyu_categoriya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menyu',
            name='categoriya.py',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='main.categoriya.py'),
        ),
    ]
