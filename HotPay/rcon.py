from mctools import RCONClient

HOST = "mc.szczurowsky.pl"
PORT = 25575

rcon = RCONClient(HOST, port=PORT)


def send_command(command):
    if rcon.login("123"):
        resp = rcon.command(command)
        return True