from django.db import models
import uuid

class Shoes (models.Model):
  uuid = models.UUIDField(default=uuid.uuid4, unique=True)
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  size = models.IntegerField()
  description = models.TextField()
  stock = models.IntegerField()
  image = models.ImageField(upload_to='shoe_images/')

  def __str__(self):
    return self.name

