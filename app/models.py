from django.db import models


class UserProfile(models.Model):
    infopage = models.CharField(max_length=50)
    genero = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    hora_nacimiento = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=50)
    situacion_sentimental = models.CharField(max_length=20)
    pensamientos = models.CharField(max_length=20)
    elemento = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=50, blank=True, null=True)
    email_usuario = models.EmailField(blank=True, null=True)
    longitud = models.FloatField(default=-74.0721)  # Valor por defecto
    latitud = models.FloatField(default=4.711)  # Valor por defecto

    def __str__(self):
        return f"{self.infopage} - {self.nombre_usuario}"
