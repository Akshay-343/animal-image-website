from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
import uuid  # Required for unique book instances
from django.contrib.auth.models import User
from datetime import date


class Animal(models.Model):
    """Model representing an animal."""
    animal_name = models.CharField(max_length=100)
    animal_image = models.ImageField(upload_to='images/', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['animal_name']

    def get_absolute_url(self):
        """Returns the URL to access a particular animal instance."""
        return reverse('animal_detail',args=[str(self)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.animal_name}'
