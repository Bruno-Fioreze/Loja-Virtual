# Generated by Django 3.1.6 on 2021-02-04 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20210203_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao_slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]