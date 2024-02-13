# Generated by Django 4.2.7 on 2024-02-13 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vol1', '0004_instrumentosmusicais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artistas',
            name='insArt',
            field=models.ForeignKey(help_text='Instrumento musical do artista', max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instrumentos', to='vol1.instrumentosmusicais'),
        ),
    ]