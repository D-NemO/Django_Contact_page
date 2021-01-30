from django.db import models

# Create your models here.
class contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name