from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
#
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otros'),
    )

    username    = models.CharField(max_length=10, unique=True)
    email       = models.EmailField(unique = True)
    nombres     = models.CharField(max_length=30, blank=True)
    apellidos   = models.CharField(max_length=30, blank=True)
    genero      = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    avatar_url  = models.CharField(max_length=250, blank=True)
    empresa     = models.ForeignKey("configuracion.Empresa", on_delete=models.PROTECT, related_name="empresa_usuario", null=True, blank=True)
    #
    is_staff  = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'

    REQUIRED_FIELDS = ['username',]

    objects = UserManager()

    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return self.nombres + ' ' + self.apellidos
