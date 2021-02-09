import ping3
from errors import PingError
from ping3 import verbose_ping

ping3.EXCEPTIONS = True
try:
    verbose_ping("192.168.0.1")
except PingError as Ex:
    print("Error")
