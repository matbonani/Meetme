import stdimage
from django.db import models
import uuid
from stdimage import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criacao = models.DateField('Criação', auto_now_add=True)
    atualizacao = models.DateTimeField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo', default=False)

    class Meta:
        abstract = True


class Pessoa(Base):

    AVAILABILITY_CHOICE = (
        ('Disponivel', 'disp'),
        ('Indisponivel no momento', 'indisp')
    )

    nome = models.CharField('Primeiro nome', max_length=20)
    sobrenome = models.CharField('Ultimo nome', max_length=20)
    idade = models.IntegerField('Idade')
    descricao = models.TextField('Comte um pouco sobre voce', max_length=400)
    descricao2 = models.CharField('Pequena descrição', max_length=150)
    perfil = StdImageField('Imagem de perfil', upload_to=get_file_path,
                           variations={'thumb': {'width': 508, 'height': 550, 'crop': True}})
    experiencia = models.IntegerField('Anos de experiencia')
    pais = models.CharField('Pais', max_length=50)
    cidade = models.CharField('Cidade/bairro', max_length=50)
    email = models.EmailField('E-mail')
    telefone1 = models.CharField('Telefone 1', max_length=50)
    telefone2 = models.CharField('Telefone 2', max_length=50, default='')
    freelance = models.CharField('Disponibilidade', max_length=30, choices=AVAILABILITY_CHOICE)
    facebook = models.CharField('Facebook', max_length=300, default='#')
    twitter = models.CharField('twitter', max_length=300, default='#')
    instagram = models.CharField('instagram', max_length=300, default='#')
    linkedin = models.CharField('Linkedin', max_length=300, default='#')

    def __str__(self):
        return self.nome


class Servico(Base):

    ICONE_CHOICE = (
        ('icon-grid', 'grid 2x2'),
        ('icon-layers', 'folhas'),
        ('icon-briefcase', 'maleta'),
        ('icon-bubbles', 'conversa')
    )

    servico = models.CharField('Serviço', max_length=100)
    descricao = models.CharField('Descrição do serviço', max_length=200)
    icone = models.CharField('Icone', max_length=15, choices=ICONE_CHOICE)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Educacao(Base):
    ensino = models.CharField('Estudou oque', max_length=100)
    instituicao = models.CharField('Nome da Instituição', max_length=100)
    inicio = models.CharField('mes/ano de inicio', max_length=100)
    fim = models.CharField('mes/ano do termino', max_length=100)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Educação'
        verbose_name_plural = 'Educações'

    def __str__(self):
        return self.instituicao


class Experiencia(Base):
    cargo = models.CharField('Cargo', max_length=100)
    empresa = models.CharField('Nome da empresa', max_length=100)
    inicio = models.CharField('mes/ano de inicio', max_length=50)
    fim = models.CharField('mes/ano do termino', max_length=50)
    descricao = models.TextField('Descrição')

    class Meta:
        verbose_name = 'Experiencia'
        verbose_name_plural = 'Experiencias'

    def __str__(self):
        return self.cargo


class Portifolio(Base):
    portifolio = StdImageField('Imagem do portifolio', upload_to=get_file_path,
                               variations={'thumb': {'width': 500, 'height': 324, 'crop': True}})

    class Meta:
        verbose_name = 'Portifolio'
        verbose_name_plural = 'Portifolios'


class Projetos(Base):
    projetost = models.IntegerField('Projetos em andamento')
    projetosend = models.IntegerField('Projetos finalizados')
    premios = models.IntegerField('Premios recebidos')
    clientes = models.IntegerField('Clientes satisfeitos')

    class Meta:
        verbose_name = 'Contagem'
        verbose_name_plural = 'Contagens'





