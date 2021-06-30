from .models import ServerConnection
from mctools import RCONClient


def execute_command(command):
    if ServerConnection.use_rcon:
        se = ServerConnection.objects.first()
        rcon = RCONClient(se.rcon_host, port=se.rcon_port)
        if rcon.login(se.rcon_password):
            rcon.command(command)
            return True
    return False
