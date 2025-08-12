def solve(data):
    """
    Hàm giải bài toán từ điển song ngữ.
    - data: danh sách các dòng lệnh đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả cho các lệnh find.
    """
    dictionary = {}
    result = []
    
    q = int(data[0])
    
    for i in range(1, q + 1):
        line = data[i].strip()
        parts = line.split(' ', 2)  # Tách tối đa thành 3 phần
        
        command = parts[0]
        
        if command == "add":
            eng = parts[1]
            viet = parts[2] if len(parts) > 2 else ""
            dictionary[eng] = viet
            
        elif command == "find":
            eng = parts[1]
            if eng in dictionary:
                result.append(dictionary[eng])
            else:
                result.append("Not found")
    
    return result

def main():
    data = []
    q = int(input().strip())
    data.append(str(q))
    
    for _ in range(q):
        line = input().strip()
        data.append(line)
    
    res = solve(data)
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()