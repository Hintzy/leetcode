def reverseBits(n: int) -> int:
    trimmed = bin(n)[2:]
    return int(trimmed[::-1])

print(reverseBits(32))