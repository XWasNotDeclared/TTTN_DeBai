def solve(data):
    """
    Ham giai bai toan tim day con ly tuong.
    - data: danh sach so nguyen da duoc doc tu input.
    - Tra ve: list chua ket qua (string).
    """
    n = data[0]
    arr = data[1:n+1]
    
    if n == 1:
        return [str(arr[0])]
    
    # Tim tat ca cac day con lien tiep tang dan
    best_sum = float('-inf')
    best_subsequence = []
    
    i = 0
    while i < n:
        # Bat dau mot day con moi tu vi tri i
        current_subsequence = [arr[i]]
        current_sum = arr[i]
        j = i + 1
        
        # Mo rong day con tang dan
        while j < n and arr[j] > arr[j-1]:
            current_subsequence.append(arr[j])
            current_sum += arr[j]
            j += 1
        
        # Kiem tra xem day con hien tai co tot hon khong
        if len(current_subsequence) > 1:  # Chi xet day con co it nhat 2 phan tu
            if current_sum > best_sum:
                best_sum = current_sum
                best_subsequence = current_subsequence[:]
        
        # Di chuyen den phan tu tiep theo
        if j == i + 1:  # Khong co day tang nao tu vi tri i
            i += 1
        else:
            i = j
    
    # Neu khong tim thay day con tang nao, tra ve so lon nhat
    if not best_subsequence:
        max_value = max(arr)
        return [str(max_value)]
    
    # Tra ve day con ly tuong
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