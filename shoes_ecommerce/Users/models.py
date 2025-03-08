from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import get_object_or_404
import uuid


class CustomUser(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_set',  # Nombre único
        help_text='The groups this user belongs to.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_set',  # Nombre único
        help_text='Specific permissions for this user.',
    )
    def __str__(self):
        return self.email
    
    
    @classmethod
    def change_user_password(cls, user_uuid, new_password):
        user = cls.objects.get(uuid=user_uuid)
        user.set_password(new_password)
        user.save()
        return user #probar cuando termine de verificar que login y signup funcioonan