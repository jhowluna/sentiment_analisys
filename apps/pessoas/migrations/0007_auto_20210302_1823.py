# Generated by Django 3.1.7 on 2021-03-02 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0006_auto_20210302_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='lista_sentimentos',
            field=models.CharField(max_length=20000000, null=True),
        ),
    ]