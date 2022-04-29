from django.db import models

# Create your models here.


class docs(models.Model):
    title = models.CharField(max_length=10)
    text = models.TextField()

    def __str__(self):
        return self.title


