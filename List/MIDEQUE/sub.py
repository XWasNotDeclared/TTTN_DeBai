def solve(data):
    """
    Hàm giải bài toán MIDEQUE.
    - data: danh sách chứa số thao tác và các thao tác.
    - Trả về: list chứa các kết quả của pop và size.
    """
    q = data[0]
    idx = 1
    result = []
    mideque = []  # Sử dụng list để mô phỏng mideque
    
    for _ in range(q):
        operation = data[idx]
        
        if operation == "push_front":
            x = data[idx + 1]
            mideque.insert(0, x)  # Thêm vào đầu
            idx += 2
        elif operation == "push_back":
            x = data[idx + 1]
            mideque.append(x)  # Thêm vào cuối
            idx += 2
        elif operation == "pop":
            if not mideque:
                result.append("EMPTY")
            else:
                n = len(mideque)
                # Tính vị trí phần tử giữa (chỉ số bắt đầu từ 1)
                if n % 2 == 0:  # Chẵn
                    mid_pos = n // 2 + 1  # Vị trí thứ n/2 + 1
                else:  # Lẻ
                    mid_pos = (n - 1) // 2 + 1  # Vị trí thứ (n-1)/2 + 1 = (n+1)/2
                
                # Chuyển về chỉ số 0-indexed
                mid_idx = mid_pos - 1
                popped_element = mideque.pop(mid_idx)
                result.append(popped_element)
            idx += 1
        elif operation == "size":
            result.append(len(mideque))
            idx += 1
    
    return result

def main():
    data = []
    q = int(input().strip())
    data.append(q)
    
    for _ in range(q):
        line = input().strip().split()
        if len(line) == 2:  # push_front hoặc push_back
            operation = line[0]
            x = int(line[1])
            data.extend([operation, x])
        else:  # pop hoặc size
            operation = line[0]
            data.append(operation)
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()