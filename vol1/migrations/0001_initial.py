# Generated by Django 4.2.7 on 2024-02-13 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bandas',
            fields=[
                ('nomBnd', models.CharField(help_text='Nome da banda', max_length=200, primary_key=True, serialize=False)),
                ('genBnd', models.CharField(blank=True, choices=[('RCK', 'ROCK'), ('RTB', "RHYTHM 'N BLUES")], help_text='Gênero musical da banda', max_length=200, null=True)),
            ],
            options={
                'db_table': 'T000BND',
            },
        ),
        migrations.CreateModel(
            name='Musicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMsc', models.CharField(blank=True, help_text='Nome da música', max_length=200)),
                ('tmpMsc', models.IntegerField(blank=True, default='0', help_text='Tempo da música (em segundos)')),
                ('nomBnd', models.ForeignKey(help_text='Nome da banda', on_delete=django.db.models.deletion.CASCADE, related_name='nome_banda', to='vol1.bandas')),
            ],
            options={
                'db_table': 'T000MSC',
            },
        ),
        migrations.CreateModel(
            name='Artistas',
            fields=[
                ('nomArt', models.CharField(help_text='Nome da artístico da pessoa', max_length=200, primary_key=True, serialize=False)),
                ('nomPes', models.CharField(blank=True, help_text='Nome da pessoa', max_length=200)),
                ('insArt', models.CharField(choices=[('BAT', 'BATERIA'), ('GUI', 'GUITARRA'), ('MIC', 'MICROFONE'), ('TEC', 'TECLADO'), ('VIO', 'VIOLÃO'), ('SAX', 'SAXOFONE')], default='MIC', help_text='Instrumento musical do artista', max_length=200)),
                ('nomBnd', models.ForeignKey(help_text='Nome da banda', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nome_banda_pessoa', to='vol1.bandas')),
            ],
            options={
                'db_table': 'T000ART',
            },
        ),
    ]
