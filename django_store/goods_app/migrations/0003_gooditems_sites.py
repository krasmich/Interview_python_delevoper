# Generated by Django 4.0.4 on 2022-06-05 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('goods_app', '0002_category_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='gooditems',
            name='sites',
            field=models.ManyToManyField(to='sites.site'),
        ),
    ]
