#!/usr/bin/python3

import secrets
import string

chars = string.digits + string.ascii_letters + string.punctuation

print(len(chars))
print(''.join(secrets.choice(chars)  for _ in range(40)))
