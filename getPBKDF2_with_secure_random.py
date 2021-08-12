#!/usr/bin/python3

import hashlib
import sys
import os

value = " ".join( sys.argv[1:] )
salt = os.urandom(64)

dk =  hashlib.pbkdf2_hmac('sha512', value.encode(), salt, 200000 )

print (dk.hex() )

