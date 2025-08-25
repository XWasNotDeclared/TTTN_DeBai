def decimal_to_ternary(n: int) -> str:
    """Chuyen so nguyen duong n sang he tam phan (chuoi)."""
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return "".join(digits[::-1])

def main():
    # Nhap so nguyen duong tu ban phim
    n = int(input().strip())
    # Chuyen sang he tam phan
    res = decimal_to_ternary(n)
    # In ket qua ra man hinh
    print(f"{res}")

if __name__ == "__main__":
    main()
