# Generated by Django 4.1 on 2023-05-30 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('cod_cuenta', models.IntegerField(primary_key=True, serialize=False)),
                ('saldo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoMaterial',
            fields=[
                ('cod_tipo_material', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('valor', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoTransaccion',
            fields=[
                ('cod_tipo_tra', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cod_usuario', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('contrasena', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('cod_tra', models.IntegerField(primary_key=True, serialize=False)),
                ('monto', models.IntegerField()),
                ('fecha', models.DateTimeField()),
                ('cod_cuenta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.cuenta')),
                ('cod_tipo_tra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.tipotransaccion')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('cod_material', models.IntegerField(primary_key=True, serialize=False)),
                ('foto', models.ImageField(upload_to='')),
                ('cod_tipo_material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.tipomaterial')),
                ('cod_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='cuenta',
            name='cod_usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.usuario'),
        ),
    ]
