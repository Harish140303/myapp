from django.db import models

class Employee(models.Model):
   
    photo = models.CharField(max_length=500, blank=True, null=True)

    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(blank=True)
    phone      = models.CharField(max_length=20, blank=True)

    role       = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    emp_type   = models.CharField(max_length=50, blank=True)
    join_date  = models.DateField(null=True, blank=True)

    dob        = models.DateField(null=True, blank=True)
    gender     = models.CharField(max_length=20, blank=True)
    blood_group= models.CharField(max_length=5, blank=True)
    address    = models.TextField(blank=True)

    education  = models.CharField(max_length=200, blank=True)
    skills     = models.TextField(blank=True)  
    hobbies    = models.TextField(blank=True)   
    biotag     = models.CharField(max_length=200, blank=True)

    ec_name    = models.CharField(max_length=100, blank=True)
    ec_relation= models.CharField(max_length=50, blank=True)
    ec_phone   = models.CharField(max_length=20, blank=True)
    ec_alt_phone=models.CharField(max_length=20, blank=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
