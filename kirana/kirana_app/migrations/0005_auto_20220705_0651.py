# Generated by Django 2.2 on 2022-07-05 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kirana_app', '0004_auto_20220705_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapping',
            name='stock_status',
            field=models.CharField(default='OUT', max_length=100),
        ),
    ]