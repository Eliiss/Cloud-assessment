from django.db import models
import uuid

class Shoes (models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, unique=True)
  name = models.CharField(max_length=100)
  price = models.DecimalField 
