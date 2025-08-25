def solve(data):
    """
    Ham giai bai toan MIDEQUE.
    - data: danh sach chua so thao tac va cac thao tac.
    - Tra ve: list chua cac ket qua cua pop va size.
    """
    q = data[0]
    idx = 1
    result = []
    mideque = []  # Su dung list de mo phong mideque
    
    for _ in range(q):
        operation = data[idx]
        
        if operation == "push_front":
            x = data[idx + 1]
            mideque.insert(0, x)  # Them vao dau
            idx += 2
        elif operation == "push_back":
            x = data[idx + 1]
            mideque.append(x)  # Them vao cuoi
            idx += 2
        elif operation == "pop":
            if not mideque:
                result.append("EMPTY")
            else:
                n = len(mideque)
                # Tinh vi tri phan tu giua (chi so bat dau tu 1)
                if n % 2 == 0:  # Chan
                    mid_pos = n // 2 + 1  # Vi tri thu n/2 + 1
                else:  # Le
                    mid_pos = (n - 1) // 2 + 1  # Vi tri thu (n-1)/2 + 1 = (n+1)/2
                
                # Chuyen ve chi so 0-indexed
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
        if len(line) == 2:  # push_front hoac push_back
            operation = line[0]
            x = int(line[1])
            data.extend([operation, x])
        else:  # pop hoac size
            operation = line[0]
            data.append(operation)
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()