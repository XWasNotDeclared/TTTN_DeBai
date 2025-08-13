import math

def solve(data):
    """
    Hàm giải bài toán GCD của dãy số.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa các kết quả GCD (mỗi test 1 dòng).
    """
    t = data[0]  # số test case
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
    t = int(input().strip())  # số test case
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
