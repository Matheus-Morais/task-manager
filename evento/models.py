from django.db import models
from django.utils import timezone


class Atividade(models.Model):
    evento = models.ForeignKey('Evento')
    tipo_atividade = models.ForeignKey('TipoAtividade')
    tema = models.CharField('tema', max_length=200)
    descricao = models.TextField('descrição')
    abertura_atividade = models.DateTimeField('abertura')
    encerramento_atividade = models.DateTimeField('encerramento')
    local = models.CharField('local de realização', max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.tema = self.tema.upper()

        if self.local:
            self.local = self.local.upper()

        return super(Atividade, self).save(*args, **kwargs)

    def __str__(self):
        return self.tema


class Evento(models.Model):
    nome = models.CharField('nome', max_length=200)
    local = models.CharField('local', max_length=200)
    abertura_evento = models.DateField('abertura do evento')
    encerramento_evento = models.DateField('encerramento do evento')
    abertura_inscricoes = models.DateField('abertura das inscrições')
    encerramento_inscricoes = models.DateField('encerramento das inscrições')
    limite_inscricoes = models.IntegerField('limite de inscrições')
    apresentacao = models.TextField('apresentação', blank=True, null=True)
    publico_alvo = models.TextField('público alvo', blank=True, null=True)
    programacao = models.TextField('programação', blank=True, null=True)
    data_cadastro = models.DateTimeField('data de cadastro', default=timezone.now)

    def save(self, *args, **kwargs):
        self.nome = self.nome.upper()
        self.local = self.local.upper()

        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.nome)


class TipoAtividade(models.Model):
    descricao = models.CharField('descrição', max_length=200, unique=True)
    data_cadastro = models.DateTimeField('data de cadastro', default=timezone.now)

    class Meta:
        verbose_name = 'tipo de atividade'
        verbose_name_plural = 'tipos de atividades'

    def save(self, *args, **kwargs):
        self.descricao = self.descricao.upper()
        return super(TipoAtividade, self).save(*args, **kwargs)

    def __str__(self):
        return '{}'.format(self.descricao)