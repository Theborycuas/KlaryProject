from django.db import models
from django.forms import BooleanField
from categories.models import Category
from tags.models import Tag
from cities.models import City

class Place(models.Model):
    place_name = models.CharField("Nombre", max_length=200, blank = False, null = False)
    place_description = models.CharField("Descripción", max_length=200, blank = True, null = True)
    place_lat = models.CharField("Latitud", max_length=200, blank = False, null = False)
    place_long = models.CharField("Longitud", max_length=200, blank = False, null = False)    
    city_id = models.ForeignKey(City, verbose_name="Citiudad", on_delete=models.CASCADE, null = False, blank = False)
    place_address = models.CharField("Dirección", max_length=200, blank = True, null = True)
    category_id = models.ManyToManyField(Category, verbose_name="Caregoría", null = True, blank = True)
    tags_id = models.ManyToManyField(Tag, verbose_name="Etiquetas", null = True, blank = True)
    place_approve = models.BooleanField("Aprovado o Denegado", default = True, blank = True, null = True)    
    place_state = models.BooleanField("Estado", default = True, blank = True, null = True)    
    place_count = models.IntegerField("Contador", blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Creación")
    update_at = models.DateTimeField(auto_now = True, verbose_name="Fecha de Edición")


    class Meta:
        verbose_name = "Lugar"
        verbose_name_plural = "Lugares"

    def __str__(self):
        return self.place_name