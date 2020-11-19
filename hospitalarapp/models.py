from django.db import models
from PIL import Image

# Create your models here.
class Hospital(models.Model):
    """Representa a entidade hospitais"""
    nome_hospital = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='img',null=True, blank=True)
    desc_hospital = models.TextField()
    tipo_hospital = models.CharField(max_length=200)
    conceito_hospital = models.CharField(max_length=200)


    def foto_url(self):
    	if self.foto and hasattr(self.foto, 'url'):
    		print("a url da foto é:", self.foto.url)
    		return self.foto.url
    	else:
    		return "/static/img/hosp04.jpg"

        
    def __str__(self):
        """retorna um representação de um string do modelo"""
        return self.nome_hospital
