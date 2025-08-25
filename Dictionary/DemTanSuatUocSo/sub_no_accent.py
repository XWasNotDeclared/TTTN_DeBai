def solve(data):
    """
    data: danh sach so nguyen da doc tu input.
    Dinh dang data:
    - data[0] = T so luong bo test
    - voi moi bo test:
        + data[idx] = N
        + data[idx+1: idx+1+N] = day so A
    """
    t = data[0]
    idx = 1
    result = []
    
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx: idx + n]
        idx += n
        
        max_val = max(arr)
        freq = [0] * (max_val + 1)
        
        # Dem so lan moi so xuat hien trong arr
        count = [0] * (max_val + 1)
        for num in arr:
            count[num] += 1
        
        # Voi moi k tu 1 den max_val, dem tan suat k la uoc cua cac so trong arr
        for k in range(1, max_val + 1):
            s = 0
            for multiple in range(k, max_val + 1, k):
                s += count[multiple]
            freq[k] = s
        
        # Chuan bi chuoi ket qua theo dinh dang de bai
        # Chi in nhung k co freq[k] > 0
        pairs = []
        for k in range(1, max_val + 1):
            if freq[k] > 0:
                pairs.append(f"{k}: {freq[k]}")
        result.append("{" + ", ".join(pairs) + "}")
    
    return result

def main():
    data = []
    t = int(input().strip())
    data.append(t)
    for _ in range(t):
        n = int(input().strip())
        data.append(n)
        arr = list(map(int, input().split()))
        data.extend(arr)
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()
