# Generated by Django 4.0.4 on 2022-05-01 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_docs_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]