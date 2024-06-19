from django.db import models

class HarryWinstonPiece(models.Model):
    model_name = models.CharField(max_length=255)
    serial_number = models.CharField(max_length=255, blank=True)
    style = models.TextField()
    materials = models.TextField()
    features = models.TextField()
    documentation = models.TextField()
    condition = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.model_name} ({self.serial_number})"