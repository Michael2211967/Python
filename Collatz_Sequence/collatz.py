def collatz_seq(n):
    seq = [n]
    while n != 1:
        n = n * 3 + 1 if n % 2 else n // 2
        seq.append(n)
    return seq

if __name__ == "__main__":
    for number in range(99):
        seq = collatz_seq(number + 1)
        print(seq)
