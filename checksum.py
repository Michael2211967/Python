#! /usr/bin/python3

def checksum(n):
    checksum = 0
    while n > 0:
        checksum += n % 10
        n //= 10
    return checksum

if __name__ == "__main__":
    n = int(input("Von welcher Zahl wollen Sie die Quersumme wissen? "))
    check = checksum(n)
    print(f"\nDie Quersumme von {n} ist {check}.")
