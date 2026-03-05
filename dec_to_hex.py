#!/usr/bin/env python3
ALPHABET = \
  "0123456789abcdefghijklmnopqrstuvwxyz"

def encode (n):
  try:
    return ALPHABET [n]
  except IndexError:
    raise Exception ("cannot encode: %s" % n)

def dec_to_base (dec = 0, base = 16):
  if dec < base:
    return encode (dec)
  else:
    return dec_to_base (dec // base, base) + encode (dec % base)

dec = int(input("Dezimalzahl eingeben: "))
print(f"\n hex: {dec_to_base(dec)}")
print(f" oct: {dec_to_base(dec, 8)}")
print(f" bin: {dec_to_base(dec, 2)}")


