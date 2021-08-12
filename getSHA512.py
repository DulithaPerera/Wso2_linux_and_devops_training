#!/usr/bin/python3

import hashlib
import sys
import os

value = " ".join( sys.argv[1:] )
salt = os.urandom(64)

hash = hashlib.sha512( value.encode() + salt)

print (hash.hexdigest() )

