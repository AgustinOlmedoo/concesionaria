# Generated by Django 5.1 on 2024-08-12 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0004_alter_auto_año_alter_auto_marca_alter_auto_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='marca',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='auto',
            name='modelo',
            field=models.CharField(max_length=100),
        ),
    ]
