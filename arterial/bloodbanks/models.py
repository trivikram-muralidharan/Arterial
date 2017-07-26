from django.db import models

# Create your models here.
class Donor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    user_id = models.CharField(max_length=20)
    pswd = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    numdon = models.CharField(max_length=10)
    age = models.CharField(max_length=5)
    btype = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name





class BloodReq(models.Model):
    donor = models.ForeignKey(Donor, on_delete = models.CASCADE)
    btype = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    hospname = models.CharField(max_length=50)
    Area = models.CharField(max_length=50)
    units = models.CharField(max_length=50)
    

    def __str__(self):
        return self.hospname



class Hospital(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bloodbank(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    apunit = models.CharField(max_length=50)
    anunit = models.CharField(max_length=50)
    bpunit = models.CharField(max_length=50)
    bnunit = models.CharField(max_length=50)
    abpunit = models.CharField(max_length=50)
    abnunit = models.CharField(max_length=50)
    opunit = models.CharField(max_length=50)
    onunit = models.CharField(max_length=50)
    
    

    def __str__(self):
        return self.name


