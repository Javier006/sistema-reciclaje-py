# Generated by Django 4.1 on 2023-06-02 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='password',
            field=models.CharField(default=1, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='material',
            name='foto',
            field=models.ImageField(upload_to='static/img/'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cod_usuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
