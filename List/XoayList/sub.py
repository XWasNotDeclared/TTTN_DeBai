def solve(data):
    """
    Hàm giải bài toán xoay list sang phải k bước.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa các phần tử sau khi xoay.
    """
    n = data[0]
    k = data[1]
    arr = data[2:2+n]
    
    # Tối ưu k để tránh xoay thừa
    k = k % n if n > 0 else 0
    
    # Xoay list sang phải k bước
    if k == 0:
        result = arr
    else:
        result = arr[-k:] + arr[:-k]
    
    return [' '.join(map(str, result))]

def main():
    data = []
    n, k = map(int, input().split())
    data.extend([n, k])
    
    if n > 0:
        arr = list(map(int, input().split()))
        data.extend(arr)
    
    res = solve(data)
    print(res[0])

if __name__ == "__main__":
    main()