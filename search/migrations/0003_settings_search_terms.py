# Generated by Django 2.0.10 on 2019-02-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_searchterm_settings'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='search_terms',
            field=models.CharField(default='Band saw', max_length=5000),
        ),
    ]
