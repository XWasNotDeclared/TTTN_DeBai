from collections import Counter

def solve(data):
    """
    - data: danh sách số nguyên, input đã đọc
    - Trả về list kết quả "Yes"/"No"
    """
    t = data[0]
    idx = 1
    result = []
    for _ in range(t):
        a = data[idx]
        b = data[idx + 1]
        idx += 2
        # chuyển sang nhị phân, zfill 32 bit
        bin_a = bin(a)[2:].zfill(32)
        bin_b = bin(b)[2:].zfill(32)

        # đếm số lượng '0' và '1' bằng Counter (dictionary)
        count_a = Counter(bin_a)
        count_b = Counter(bin_b)

        # so sánh dictionary
        if count_a == count_b:
            result.append("Yes")
        else:
            result.append("No")
    return result


def main():
    data = []
    t = int(input().strip())
    data.append(t)
    for _ in range(t):
        a, b = map(int, input().split())
        data.extend([a, b])
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
