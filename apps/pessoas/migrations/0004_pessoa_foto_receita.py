# Generated by Django 3.1.7 on 2021-03-02 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0003_auto_20210302_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y/'),
        ),
    ]