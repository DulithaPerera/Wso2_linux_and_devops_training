#!/usr/bin/python3

import hashlib
import sys

value = " ".join( sys.argv[1:] )

dk =  hashlib.pbkdf2_hmac('sha512', value.encode(), b'Km5d5ivMy8iexuHcZrsD', 200000 )

print (dk.hex() )

