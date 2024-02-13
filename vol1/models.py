from django.db import models

# Tabela das bandas
class Bandas(models.Model):
    GENEROS_CHOICE=(
        ('RCK', 'ROCK'),
        ('RTB', 'RHYTHM \'N BLUES'),
    )

    nomBnd = models.CharField(max_length=200, primary_key=True, blank=False, null=False, help_text='Nome da banda')
    genBnd = models.CharField(choices=GENEROS_CHOICE, max_length=200, blank=True, null=True, help_text='Gênero musical da banda')

    class Meta:
        db_table = 'T000BND'

    def __str__(self):
        return self.nomBnd


# Tabela dos artistas
class Artistas(models.Model):
    INSTRUMENTOS_CHOICE=(
        ('BAT', 'BATERIA'),
        ('GUI', 'GUITARRA'),
        ('MIC', 'MICROFONE'),
        ('TEC', 'TECLADO'),
        ('VIO', 'VIOLÃO'),
        ('SAX', 'SAXOFONE'),
    )

    nomBnd = models.ForeignKey(Bandas, related_name='nome_banda_pessoa', blank=False, null=True, help_text='Nome da banda', on_delete=models.SET_NULL)
    nomArt = models.CharField(primary_key=True, max_length=200, blank=False, null=False, help_text='Nome da artístico da pessoa')
    nomPes = models.CharField(max_length=200, blank=True, null=False, help_text='Nome da pessoa')
    insArt = models.CharField(choices=INSTRUMENTOS_CHOICE, default='MIC', max_length=200, blank=False, null=False, help_text='Instrumento musical do artista')

    class Meta:
        db_table = 'T000ART'

    def __str__(self):
        return self.nomArt


# Tabela das músicas
class Musicas(models.Model):
    nomBnd = models.ForeignKey(Bandas, related_name='nome_banda', blank=False, null=False, help_text='Nome da banda', on_delete=models.CASCADE)
    nomMsc = models.CharField(max_length=200, blank=True, null=False, help_text='Nome da música')
    tmpMsc = models.IntegerField(blank=True, null=False, default='0', help_text='Tempo da música (em segundos)')

    class Meta:
        db_table = 'T000MSC'

    def __str__(self):
        return self.nomMsc