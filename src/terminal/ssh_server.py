import paramiko
import os

class SSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
        self.allowed_auths = ['password']

    def check_auth_password(self, username, password):
        if username == 'user' and password == 'password':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED