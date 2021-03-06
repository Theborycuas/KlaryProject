from django.db import models

class Province(models.Model):
    province_name = models.CharField(max_length=25, verbose_name="Nombre de la Provincia")
    province_state = models.BooleanField(default=False, verbose_name="Estado de la Provincia")
    created_at = models.DateTimeField(auto_now_add = True, verbose_name="Fecha de Creación")
    update_at = models.DateTimeField(auto_now = True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "provincia"
        verbose_name_plural = "provincias"

    def __str__(self):
        return self.province_name