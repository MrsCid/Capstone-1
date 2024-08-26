from django.db import models
from django.contrib.auth.models import *
from django.core.exceptions import ValidationError

# Create your models here.

class Asignatura(models.Model):
    sigla=models.CharField(max_length=7)
    nombre=models.CharField(max_length=50)

    def __str__(self):
        return self.sigla
    
class Seccion(models.Model):
    JORNADA_OPCIONES = [
        ('D', 'Diurna'),
        ('V', 'Vespertina'),
    ]

    numero = models.IntegerField()
    jornada = models.CharField(max_length=1, choices=JORNADA_OPCIONES)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        
        email = self.normalize_email(email)
        
        if not email.endswith('@duocuc.cl') and not email.endswith('@profesor.duoc.cl'):
            raise ValidationError('El correo debe ser @duoc o @profesor.duoc')

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        
        if email.endswith('@duoc'):
            group = Group.objects.get(name='alumno')
        elif email.endswith('@profesor.duoc'):
            group = Group.objects.get(name='docente')
        
        user.groups.add(group)
        
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email