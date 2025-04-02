from django.db import models

class Members(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=15)


    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone}"
