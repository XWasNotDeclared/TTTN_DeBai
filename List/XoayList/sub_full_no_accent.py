def solve(data):
    """
    Ham giai bai toan xoay list sang phai k buoc.
    - data: danh sach so nguyen da duoc doc tu input.
    - Tra ve: list chua cac phan tu sau khi xoay.
    """
    n = data[0]
    k = data[1]
    arr = data[2:2+n]
    
    # Toi uu k de tranh xoay thua
    k = k % n if n > 0 else 0
    
    # Xoay list sang phai k buoc
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