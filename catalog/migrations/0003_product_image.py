# Generated by Django 2.0.1 on 2018-07-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180719_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Imagem'),
        ),
    ]