from django.db import models

# Create your models here.

class Profesor(models.Model):
    """Model definition for Profesor."""

    CEDULA = '1'
    PASAPORTE = '2'
    CEDULA_EXTRANGERA = '3'

    DOCUMENTO_CHOICES = (
        (CEDULA, 'Cedula Ciudadana'),
        (PASAPORTE, 'Pasaporte'),
        (CEDULA_EXTRANGERA, 'Cedula Extrangera'),
    )

    # TODO: Define fields here
    id                    = models.AutoField(primary_key=True)
    tipoDocumento         = models.CharField("Tipo de documento", max_length=50, choices=DOCUMENTO_CHOICES, null=True, blank=True)
    documento             = models.CharField("Documento:", max_length=50, null=False, blank=False)
    nombreCompleto        = models.TextField(null=False, blank=False)


    class Meta:
        """Meta definition for Profesor."""

        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        db_table = "profesores"

    def __str__(self):
        """Unicode representation of Profesor."""
        return self.nombreCompleto


class Curso(models.Model):
    """Model definition for Curso."""

    # TODO: Define fields here
    id          = models.AutoField(primary_key=True)
    area        = models.CharField("Area:", max_length=50)
    creditos    = models.IntegerField()
    docente     = models.ForeignKey(Profesor, related_name="curso_docente" ,on_delete=models.PROTECT)

    class Meta:
        """Meta definition for Curso."""

        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        texto = "{0} ({1})"
        """Unicode representation of Curso."""
        return texto.format(self.area, self.creditos)
