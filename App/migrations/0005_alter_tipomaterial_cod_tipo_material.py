# Generated by Django 4.1 on 2023-06-04 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_alter_usuario_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipomaterial',
            name='cod_tipo_material',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]