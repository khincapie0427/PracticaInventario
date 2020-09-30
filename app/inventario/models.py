from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    fechaIngreso = models.DateField(auto_now_add=True)
    comentario = models.TextField()

#Charfield sólo admite como máximo 200 carateres
#Textfield adminte infinitos caracteres

#Es importante que los comentarios no tengan límite para que no se desborden


class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    nombreDeUsuario = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
