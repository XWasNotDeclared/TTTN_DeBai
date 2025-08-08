def decimal_to_ternary(n: int) -> str:
    """Chuyển số nguyên dương n sang hệ tam phân (chuỗi)."""
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 3))
        n //= 3
    return "".join(digits[::-1])

def main():
    # Nhập số nguyên dương từ bàn phím
    n = int(input().strip())
    # Chuyển sang hệ tam phân
    res = decimal_to_ternary(n)
    # In kết quả ra màn hình
    print(f"{res}")

if __name__ == "__main__":
    main()
