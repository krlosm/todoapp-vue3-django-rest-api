from django.db import models

class Todo(models.Model):
    texto = models.CharField(max_length=140)
    estado = models.BooleanField()

    def __str__(self):
        return self.texto

    class Meta:
        ordering = ['texto']