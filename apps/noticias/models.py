from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    
    def __str__(self):  # Corregido aquí
        return self.nombre

class Noticias(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.TextField()
    imagenes=models.ImageField(upload_to='noticias')
    fecha_publicacion=models.DateTimeField(auto_now_add=True)
    categoria_noticia=models.ForeignKey(Categoria, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.titulo

