import hashlib
import os
import base64

class PasswordHelper:

    def get_hash(self, plain): 
        if isinstance(plain, str):
            plain = plain.encode('utf-8')
        hashed = hashlib.sha512(plain).hexdigest()        
        return hashed

    def get_salt(self):
        salt = base64.b64encode(os.urandom(20))
        return salt

    def validate_password(self, plain, salt, expected):
        if isinstance(plain, str):
            plain = plain.encode('utf-8')
        if isinstance(salt, str):
            salt = salt.encode('utf-8')
        return self.get_hash(plain + salt) == expected