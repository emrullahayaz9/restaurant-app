from django.db import models

# Create your models here.
class Tables(models.Model):
    table_number = models.CharField(max_length=10)
    table_password = models.CharField(max_length=10)
    is_full = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.table_password} {self.table_number}"