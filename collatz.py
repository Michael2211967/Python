def collatz_seq(n):
    seq = [n]
    while n != 1:
        n = n * 3 + 1 if n % 2 else n // 2
        seq.append(n)
    return seq

if __name__ == "__main__":
    number = int(input("Geben Sie bitte Ihre Zahl ein: "))
    seq = collatz_seq(number)
    print(seq)
