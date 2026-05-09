from datetime import date, time
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError
# Create your models here.

class Socio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfilSocio')
    dni= models.CharField("DNI", max_length=10, unique=True, blank=False)
    fNac= models.DateField(blank=False, null=False)
    
    @property
    def esMenor(self):
        today= date.today()
        edad = today.year - self.fNac.year - ((today.month, today.day) < (self.fNac.month, self.fNac.day))
        return edad < 18
    def __str__(self):
        return f"{self.user.username} - DNI: {self.dni}"
    
class Empleado(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfilEmpleado")
    dni = models.CharField("DNI",max_length=10, unique= True, blank=False)
    
    def __str__(self):
        return f"{Empleado: {self.user.last_name}, {self.user.first_name}}"
    
class Turno(models.Model):
    DISCIPLINAS=[
        ('PADEL', 'Padel'),
        ('VOLEY', 'Vóley'),
        ('FUTBOL', 'Fútbol'),
        ('BASQUET', 'Básquet'),
    ]
    
    disciplina= models.CharField("Disciplina", max_length=10, choices=DISCIPLINAS)
    fecha= models.DateField("Fecha", blank= False)
    hora= models.TimeField("Hora", blank=False)
    cupo= models.PositiveIntegerField("Cupo Máximo", blank=False)
    
    class Meta:
        unique_together= ('disciplina', 'fecha', 'hora')
    
    def clean(self):
        apertura=time(8, 0)
        cierre= time(22, 0)
        
        if self.hora < apertura or self.hora > cierre:
            raise ValidationError("Los turnos deben ubicarse entre las 8:00 y las 22:00 hs.")
    
    def __str__(self):
        return f"{self.disciplina} - {self.fecha} {self.hora}"