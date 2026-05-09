from django.shortcuts import render
from .models import Turno
from django.utils import timezone
from datetime import timedelta

# Create your views here.
def seccion_reservas(request):
    hoy = timezone.now().date()
    proximo_mes = (hoy.replace(day=28) + timedelta(days=4)).replace(day=1)
    fin_mes_siguiente = (proximo_mes + timedelta(days=32)).replace(day=1) - timedelta(days=1)
    
    disciplina_seleccionada = request.GET.get('disciplina')
    
    turnos= None
    mensaje_guia= "Por favor selecciona una disciplina para ver los turnos disponibles."
    
    if disciplina_seleccionada:
        turnos = Turno.objects.filter(
            disciplina=disciplina_seleccionada,
            fecha__range=[hoy, fin_mes_siguiente]
        ).order_by('fecha', 'hora')
        
        if not turnos.exists():
            mensaje_guia = f"No hay turnos disponibles para {disciplina_seleccionada} en este período."
        else:
            mensaje_guia = None
            
    opciones_disciplina = [d[0] for d in Turno.DISCIPLINAS]
    context = {
        'turnos': turnos,
        'disciplinas': opciones_disciplina,
        'seleccionada': disciplina_seleccionada,
        'mensaje_guia': mensaje_guia,
    }
    
    return render(request, 'reservas.html', context)