# Generated by Django 2.2.6 on 2019-10-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20191002_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alerts',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
