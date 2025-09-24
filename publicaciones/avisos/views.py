from django.views.generic import ListView
from django.utils.timezone import localdate
from .models import Aviso

class AvisosVigentesListView(ListView):
    model = Aviso
    template_name = "avisos/lista.html"
    context_object_name = "avisos"

    def get_queryset(self):
        hoy = localdate()
        return (
            Aviso.objects
            .filter(fecha_inicio__lte=hoy, fecha_fin__gte=hoy)
            .order_by("-fecha_inicio")
        )
