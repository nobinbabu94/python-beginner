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

    def __str__(self):
        return 'Dr.' + self.docs_name +', '+ self.docs_spec

class bookings(models.Model):
    patient_name = models.CharField(max_length=200,null=True, blank=True)
    patient_phone = models.CharField(max_length = 200,null=True, blank=True)
    patient_email = models.EmailField()
    docs_name = models.ForeignKey(doctors,on_delete=models.CASCADE,null=True, blank=True)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)