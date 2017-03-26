from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .models import TipoAtividade
from .models import Evento
from .models import Atividade


def inicio(request):
    html = """<h1>Opções</h1>
                <ul>
                    <li><a href='/eventos'>Eventos</a></li>
                    <li><a href='/atividades'>Atividades</a></li>
                    <li><a href='/tipoatividades'>Tipo de Atividade</a></li>
                    <li><a href='/detalhes'>Detalhes</a></li>
                </ul>
            """
    return HttpResponse(html)


def listaTipoAtividades(request):
    html = "<h1>Lista de Tipo de Atividades</h1>"
    lista = TipoAtividade.objects.all()
    for tipo in lista:
        html += '<li>{}</li>'.format(tipo.descricao)

    html += '<br/><h3>Para escolher um determinado Tipo de atividade, no navegador apague o "s/" de "tipoatividades/"e acrescente na frente da url "/id"<h3>'
    return HttpResponse(html)


def tipoAtividade(request, id):
    html = "<h1>Tipo de Atividades</h1>"
    atividade = TipoAtividade.objects.get(pk=id)
    html += '<li>{}</li>'.format(atividade.descricao)
    return HttpResponse(html)

def listaeventos(request):
    html = "<h1>Lista de Eventos</h1>"
    lista = Evento.objects.all()
    for evento in lista:
        html += '<li>{}</li>'.format(evento.nome)

    html += '<br/><h3>Para escolher um determinado evento, no navegador apague o "s/" de "eventos/" e acrescente na frente da url "/id"<h3>'
    return HttpResponse(html)

def evento(request, id):
    html = "<h1>Evento</h1>"
    evento = Evento.objects.get(pk=id)
    html += '<li>{}</li>'.format(evento.nome)
    return HttpResponse(html)

def listaAtivadades(request):
    html = "<h1>Lista de Atividades</h1>"
    lista = Atividade.objects.all()
    for atividade in lista:
        html += '<li>{}</li>'.format(atividade.tema)

    html += '<br/><h3>Para escolher uma determinada atividade, no navegador apague o "s/" de "atividades/" e acrescente na frente da url "/id"<h3>'
    return HttpResponse(html)

def atividade(request, id):
    html = "<h1>Atividade</h1>"
    atividade = Atividade.objects.get(pk=id)
    html += '<li>{}</li>'.format(atividade.tema)
    return HttpResponse(html)

@csrf_exempt
def addTipoAtividade(request):
    if request.method == 'POST':
        tipo = TipoAtividade()
        tipo.descricao = request.POST['descricao']
        tipo.save()
        return HttpResponse('Tipo Inserido com sucesso')
    else:
        return HttpResponse('Falha na inserção de tipo')


