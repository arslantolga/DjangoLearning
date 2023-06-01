from django.db import models

class tweet(models.Model):
    nickname = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    def __str__(self):
        return f"Nickname : {self.nickname}, Message : {self.message}"
