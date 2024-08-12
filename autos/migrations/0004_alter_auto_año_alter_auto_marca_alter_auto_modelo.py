# Generated by Django 5.1 on 2024-08-12 01:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autos', '0003_alter_auto_año_alter_auto_marca_alter_auto_modelo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auto',
            name='año',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='auto',
            name='marca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.marca'),
        ),
        migrations.AlterField(
            model_name='auto',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autos.modeloauto'),
        ),
    ]
