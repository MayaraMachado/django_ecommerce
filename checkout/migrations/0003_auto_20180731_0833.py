# Generated by Django 2.0.1 on 2018-07-31 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20180726_1134'),
        ('checkout', '0002_auto_20180730_1107'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarItem',
            new_name='CartItem',
        ),
    ]