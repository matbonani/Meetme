from django.contrib import admin

from .models import Pessoa, Servico, Educacao, Experiencia, Portifolio, Projetos


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'idade', 'experiencia', 'telefone1', 'cidade', 'atualizacao')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'atualizacao')


@admin.register(Educacao)
class EducacaoAdmin(admin.ModelAdmin):
    list_display = ('ensino', 'instituicao', 'inicio', 'fim', 'atualizacao')


@admin.register(Experiencia)
class ExperienciaAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'empresa', 'fim', 'inicio', 'atualizacao')


@admin.register(Portifolio)
class PortifolioAdmin(admin.ModelAdmin):
    list_display = ('atualizacao', 'criacao')


@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('projetost', 'projetosend', 'premios', 'atualizacao')
