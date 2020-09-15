from django.db import models

# Create your models here.
class employee(models.Model):

    gender_choices = {
        ('m', 'Male'),
        ('f','Female'),
    }
    
    first_name = models.CharField(max_length = 100, blank=False)
    last_name = models.CharField(max_length=100, blank=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=13)
    email = models.EmailField(max_length=255)
    job = models.ManyToManyField('AvailableJobs',blank=True)
    date_of_birth = models.DateField()
    gender = models.CharField(choices=gender_choices, max_length=1)

class AvailableJobs(models.Model):

    job_name = models.CharField(max_length=100)
    def __str__(self):
        return self.job_name