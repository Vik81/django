# Generated by Django 2.1.7 on 2019-03-24 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_cateegory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cateegory',
            new_name='Category',
        ),
    ]
