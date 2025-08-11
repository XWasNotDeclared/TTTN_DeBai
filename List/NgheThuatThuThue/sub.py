import math

def is_prime(x):
    if x < 2:
        return False
    if x % 2 == 0:
        return x == 2
    r = int(math.isqrt(x))
    for i in range(3, r+1, 2):
        if x % i == 0:
            return False
    return True

def solve(data):
    """
    - data[0]: số test case T
    - data[1..]: các phần tử input của từng test case
    """
    t = data[0]
    idx = 1
    result = []

    for _ in range(t):
        # Đọc N, p, m
        n = data[idx]
        p = data[idx+1]
        m = data[idx+2]
        idx += 3

        # Đọc mảng a
        a = data[idx: idx + n]
        idx += n

        # Tính median
        sorted_a = sorted(a)
        if n % 2 == 1:
            median = sorted_a[n // 2]
        else:
            median = (sorted_a[n//2 - 1] + sorted_a[n//2]) // 2  # làm tròn xuống

        # Tính thuế
        tax = []
        for income in a:
            base = math.ceil(income * p / 100)
            if income > median:
                base += m
            tax.append(base)

        total_tax = sum(tax)

        # Nếu tổng là số nguyên tố → giảm 1 đô cho người nghèo nhất
        if is_prime(total_tax):
            total_tax -= 1

        result.append(str(total_tax))

    return result


def main():
    data = []
    t = int(input().strip())  # số test case
    data.append(t)
    for _ in range(t):
        # Đọc N, p, m
        n, p, m = map(int, input().split())
        data.extend([n, p, m])
        # Đọc mảng a
        a = list(map(int, input().split()))
        data.extend(a)
    res = solve(data)
    print("\n".join(res))


if __name__ == "__main__":
    main()
