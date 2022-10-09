example_code = ("""\
# imports
from requests import get
import socket

""
Thanks to: communication.with.users@gmail.com for this great free weather API!
Github   : https://github.com/cookie0o
dev      : cookie0_o
""

def get_ip():
        ""
        Get the IP4 address of the user.
        ""
        try:
            hostname=socket.gethostname()   
            ip_address=socket.gethostbyname(hostname)

            # return the IP address
            return ip_address

        # if the IP address is not found, return the error message
        except Exception as error:
            # return the error message
            print ("GET IP ERROR:")
            return error
...
""")