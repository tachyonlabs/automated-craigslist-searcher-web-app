# Generated by Django 2.0.10 on 2019-02-22 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0005_auto_20190220_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='search_site',
            field=models.CharField(default='sfbay', max_length=30),
        ),
    ]
