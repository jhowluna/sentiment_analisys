# Generated by Django 3.1.7 on 2021-03-02 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pessoas', '0004_pessoa_foto_receita'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='foto_receita',
            new_name='foto_pessoa',
        ),
    ]
