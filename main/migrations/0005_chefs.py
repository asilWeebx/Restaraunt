# Generated by Django 4.1.6 on 2023-02-09 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_tadbir'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fmi', models.CharField(max_length=250)),
                ('subject', models.CharField(max_length=26)),
            ],
        ),
    ]
