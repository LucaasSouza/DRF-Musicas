from django.db import models

# Tabela dos instrumentos musicais
class InstrumentosMusicais(models.Model):
    codIns = models.CharField(primary_key=True, max_length=3, blank=False, null=False)
    nomIns = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        db_table = 'T000INS'

    def __str__(self):
        return self.codIns

# Tabela dos artistas
class Artistas(models.Model):
    insArt = models.ForeignKey(InstrumentosMusicais, related_name='instrumentos', max_length=200, blank=False, null=True, help_text='Instrumento musical do artista', on_delete=models.SET_NULL)
    nomArt = models.CharField(primary_key=True, max_length=200, blank=False, null=False, help_text='Nome da artístico da pessoa')
    nomPes = models.CharField(max_length=200, blank=True, null=False, help_text='Nome da pessoa')

    class Meta:
        db_table = 'T000ART'

    def __str__(self):
        return self.nomArt


# Tabela dos gêneros musicais
class GenerosMusicais(models.Model):
    codGen = models.CharField(primary_key=True, max_length=3, blank=False, null=False)
    nomGen = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        db_table = 'T000GEN'

    def __str__(self):
        return self.codGen


# Tabela das bandas
class Bandas(models.Model):
    artBnd = models.ManyToManyField(Artistas, related_name='elenco', blank=False, help_text='Artistas da banda')
    genBnd = models.ForeignKey(GenerosMusicais, related_name='generos_musicais', blank=True, null=True, help_text='Gênero musical da banda', on_delete=models.SET_NULL)
    nomBnd = models.CharField(max_length=200, primary_key=True, blank=False, null=False, help_text='Nome da banda')

    class Meta:
        db_table = 'T000BND'

    def __str__(self):
        return self.nomBnd


# Tabela das músicas
class Musicas(models.Model):
    nomBnd = models.ForeignKey(Bandas, to_field='nomBnd', related_name='nome_banda', blank=False, null=False, help_text='Nome da banda', on_delete=models.CASCADE)
    nomMsc = models.CharField(max_length=200, blank=True, null=False, help_text='Nome da música')
    tmpMsc = models.IntegerField(blank=True, null=False, default='0', help_text='Tempo da música (em segundos)')

    class Meta:
        db_table = 'T000MSC'

    def __str__(self):
        return self.nomMsc