from django.db import models

# Create your models here.
class URLS(models.Model):
    slug=models.CharField(max_length=6, primary_key=True)
    url=models.TextField()

    def __str__(self):
        return self.slug
    
URLS.objects.model._meta.db_table='urlslug'