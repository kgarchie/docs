from django.db import models

# Create your models here.


class docs(models.Model):
    title = models.CharField(max_length=10)
    text = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


