# Generated by Django 4.0.4 on 2022-06-05 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('goods_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site'),
        ),
    ]
