from django.db import models

# Create your models here.
class Design(models.Model):
    title = models.CharField(max_length=100)
    path = models.ImageField(
        default="../media/designs/default.jpeg", upload_to="../media/designs/"
    )
    description = models.CharField(max_length=1000, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
