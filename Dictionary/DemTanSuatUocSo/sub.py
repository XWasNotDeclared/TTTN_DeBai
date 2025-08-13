def solve(data):
    """
    data: danh sách số nguyên đã đọc từ input.
    Định dạng data:
    - data[0] = T số lượng bộ test
    - với mỗi bộ test:
        + data[idx] = N
        + data[idx+1: idx+1+N] = dãy số A
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
        
        # Đếm số lần mỗi số xuất hiện trong arr
        count = [0] * (max_val + 1)
        for num in arr:
            count[num] += 1
        
        # Với mỗi k từ 1 đến max_val, đếm tần suất k là ước của các số trong arr
        for k in range(1, max_val + 1):
            s = 0
            for multiple in range(k, max_val + 1, k):
                s += count[multiple]
            freq[k] = s
        
        # Chuẩn bị chuỗi kết quả theo định dạng đề bài
        # Chỉ in những k có freq[k] > 0
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
