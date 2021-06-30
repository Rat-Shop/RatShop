from .models import ServerConnection
from mctools import RCONClient
import logging


def execute_command(command):
    if ServerConnection.use_rcon:
        se = ServerConnection.objects.first()
        rcon = RCONClient(se.rcon_host, port=se.rcon_port)
        try:
            rcon.login(se.rcon_password)
        except Exception as e:
            logging.exception(e)
            return False
        if rcon.is_authenticated():
            rcon.command(command)
            rcon.stop()
            return True
    return False
