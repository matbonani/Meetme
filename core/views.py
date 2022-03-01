from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Pessoa, Servico, Educacao, Experiencia, Portifolio, Projetos
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['pessoa'] = Pessoa.objects.all()
        context['servico'] = Servico.objects.all()
        context['educacao'] = Educacao.objects.all()
        context['experiencia'] = Experiencia.objects.all()
        context['portifolio'] = Portifolio.objects.all()
        context['projetos'] = Projetos.objects.all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Falha ao enviar o email')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


