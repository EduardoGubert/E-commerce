# Generated by Django 3.2.7 on 2021-09-14 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao_curta', models.TextField()),
                ('descricao_longa', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='produto_imagens/%Y/%m/')),
                ('slug', models.SlugField(unique=True)),
                ('preco_marketing', models.FloatField()),
                ('preco_marketing_promocional', models.FloatField(default=0)),
                ('tipo', models.CharField(choices=[('V', 'Variação'), ('S', 'Simples')], default='V', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Variacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.FloatField()),
                ('preco_promocional', models.FloatField(default=0)),
                ('estoque', models.PositiveBigIntegerField(default=1)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produto')),
            ],
        ),
    ]
