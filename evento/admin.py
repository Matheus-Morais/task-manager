from django.contrib import admin
from evento.models import TipoAtividade, Atividade, Evento


admin.site.register(TipoAtividade)
admin.site.register(Atividade)
admin.site.register(Evento)
