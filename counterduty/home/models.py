from django.db import models

# Create your models here.

class stafflevel(models.Model):
    stafflevel_name = models.CharField(max_length=100)

    def __str__(self):
        return self.stafflevel_name

class stafftype(models.Model):
    stafftype_name = models.CharField(max_length=100)

    def __str__(self):
        return self.stafftype_name

class staff(models.Model):
    staff_name = models.CharField(max_length=100)
    staff_type = models.ForeignKey(stafftype, on_delete=models.CASCADE)
    staff_level = models.ForeignKey(stafflevel, on_delete=models.CASCADE)
    staff_active = models.BooleanField()

    def __str__(self):
        return self.staff


