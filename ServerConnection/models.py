from django.db import models


# Create your models here.

class ServerConnection(models.Model):
    use_rcon = models.BooleanField(default=False)
    rcon_host = models.CharField(max_length=255, blank=True, null=True)
    rcon_port = models.IntegerField(blank=True, null=True)
    rcon_password = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "ServerConnection"
