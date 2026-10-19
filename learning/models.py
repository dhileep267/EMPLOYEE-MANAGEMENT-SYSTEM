from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.name} - {self.location} "


class Employee(models.Model)  :
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email =models.EmailField(unique=True)
    designation = models.CharField(max_length=50)
    salary = models.IntegerField()
    joinin_date=models.DateField()
    is_active =models.BooleanField(default=True)
    department=models.ForeignKey(Department,on_delete=models.SET_NULL,blank=True,null=True)
    manager =models.ForeignKey("self",null =True,blank=True,on_delete=models.SET_NULL)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def full_name(self):
        return f"{self.first_name} {self.last_name}"



    
    