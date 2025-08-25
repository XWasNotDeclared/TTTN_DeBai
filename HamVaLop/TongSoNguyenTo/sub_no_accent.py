def sieve(max_n):
    """Tra ve mang is_prime danh dau so nguyen to tu 0..max_n"""
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(max_n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False
    return is_prime

def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach so nguyen da duoc doc tu input.
    - Tra ve: list chua ket qua cua moi test case.
    """
    t = data[0]
    idx = 1
    result = []
    max_val = 0
    # Lay max_val de sieve
    tmp_idx = 1
    for _ in range(t):
        n = data[tmp_idx]
        tmp_idx += 1
        arr = data[tmp_idx: tmp_idx + n]
        tmp_idx += n
        max_val = max(max_val, max(arr))
    # Tao bang nguyen to
    prime_table = sieve(max_val)
    # Giai tung test case
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx: idx + n]
        idx += n
        total = sum(x for x in arr if prime_table[x])
        result.append(total)
    return result

def main():
    data = []
    t = int(input().strip())
    data.append(t)
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        data.append(n)
        data.extend(arr)
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()
