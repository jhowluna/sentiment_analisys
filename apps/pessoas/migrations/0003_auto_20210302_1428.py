# Generated by Django 3.1.7 on 2021-03-02 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0002_auto_20210302_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.CharField(max_length=2),
        ),
    ]
