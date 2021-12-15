from django.db import models


class Task(models.Model):
    titlu = models.CharField(max_length=250)
    completat = models.BooleanField(default=False)
    creat = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titlu
