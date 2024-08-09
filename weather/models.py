from django.db import models


class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name
    
    class Meta: # Correct grammar for the word 'city'
        verbose_name_plural = 'cities'