import math

def solve(data):
    """
    Ham giai bai toan GCD cua day so.
    - data: danh sach so nguyen da duoc doc tu input.
    - Tra ve: list chua cac ket qua GCD (moi test 1 dong).
    """
    t = data[0]  # so test case
    idx = 1
    result = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx: idx + n]
        idx += n
        gcd_val = arr[0]
        for num in arr[1:]:
            gcd_val = math.gcd(gcd_val, num)
        result.append(gcd_val)
    return result

def main():
    data = []
    t = int(input().strip())  # so test case
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
