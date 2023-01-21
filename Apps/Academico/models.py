from django.db import models

# Create your models here.

class Curso(models.Model):
    """Model definition for Curso."""

    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    area        = models.CharField("Area:", max_length=50)
    creditos    = models.IntegerField()

    class Meta:
        """Meta definition for Curso."""

        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        texto = "{0} ({1})"
        """Unicode representation of Curso."""
        return texto.format(self.area, self.creditos)
