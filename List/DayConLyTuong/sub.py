def solve(data):
    """
    Hàm giải bài toán tìm dãy con lý tưởng.
    - data: danh sách số nguyên đã được đọc từ input.
    - Trả về: list chứa kết quả (string).
    """
    n = data[0]
    arr = data[1:n+1]
    
    if n == 1:
        return [str(arr[0])]
    
    # Tìm tất cả các dãy con liên tiếp tăng dần
    best_sum = float('-inf')
    best_subsequence = []
    
    i = 0
    while i < n:
        # Bắt đầu một dãy con mới từ vị trí i
        current_subsequence = [arr[i]]
        current_sum = arr[i]
        j = i + 1
        
        # Mở rộng dãy con tăng dần
        while j < n and arr[j] > arr[j-1]:
            current_subsequence.append(arr[j])
            current_sum += arr[j]
            j += 1
        
        # Kiểm tra xem dãy con hiện tại có tốt hơn không
        if len(current_subsequence) > 1:  # Chỉ xét dãy con có ít nhất 2 phần tử
            if current_sum > best_sum:
                best_sum = current_sum
                best_subsequence = current_subsequence[:]
        
        # Di chuyển đến phần tử tiếp theo
        if j == i + 1:  # Không có dãy tăng nào từ vị trí i
            i += 1
        else:
            i = j
    
    # Nếu không tìm thấy dãy con tăng nào, trả về số lớn nhất
    if not best_subsequence:
        max_value = max(arr)
        return [str(max_value)]
    
    # Trả về dãy con lý tưởng
    return [' '.join(map(str, best_subsequence))]

def main():
    data = []
    n = int(input().strip())
    data.append(n)
    arr = list(map(int, input().split()))
    data.extend(arr)
    
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()