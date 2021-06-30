from mctools import RCONClient

HOST = ""
PORT =

rcon = RCONClient(HOST, port=PORT)


def send_command(command):
    if rcon.login(""):
        resp = rcon.command(command)
        return True