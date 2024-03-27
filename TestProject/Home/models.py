from django.db import models

# Create your models here.

class departments(models.Model):
    dep_name = models.CharField(max_length=100,null=True, blank=True)
    dep_descriptions = models.TextField()

    def __str__(self):
        return self.dep_name

class doctors(models.Model):
    docs_name = models.CharField(max_length=100,null=True, blank=True)
    docs_spec = models.CharField(max_length=100,null=True, blank=True)
    dep_name = models.ForeignKey(departments, on_delete=models.CASCADE,null=True, blank=True)
    docs_image = models.ImageField(upload_to='doctors')