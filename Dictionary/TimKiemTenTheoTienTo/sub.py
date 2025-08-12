def solve(data):
    """
    Hàm giải bài toán chính.
    - data: danh sách các dòng query đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    q = int(data[0])
    queries = data[1:q+1]
    
    # Lưu trữ thông tin người chơi
    id_to_name = {}  # id -> name hiện tại
    name_to_id = {}  # name -> id (để check trùng tên)
    
    result = []
    
    for query in queries:
        parts = query.strip().split()
        cmd = parts[0]
        
        if cmd == "REGISTER":
            player_id = int(parts[1])
            name = parts[2]
            
            # Kiểm tra ID đã tồn tại
            if player_id in id_to_name:
                result.append("ERROR_DUPLICATE_ID")
                continue
            
            # Kiểm tra tên đã tồn tại
            if name in name_to_id:
                result.append("ERROR_DUPLICATE_NAME")
                continue
            
            # Đăng ký thành công
            id_to_name[player_id] = name
            name_to_id[name] = player_id
            
        elif cmd == "RENAME":
            player_id = int(parts[1])
            new_name = parts[2]
            
            # Kiểm tra ID tồn tại
            if player_id not in id_to_name:
                result.append("ERROR_ID_NOT_FOUND")
                continue
            
            current_name = id_to_name[player_id]
            
            # Kiểm tra tên mới trùng với tên hiện tại
            if new_name == current_name:
                result.append("ERROR_SAME_NAME")
                continue
            
            # Kiểm tra tên mới đã được sử dụng
            if new_name in name_to_id:
                result.append("ERROR_DUPLICATE_NAME")
                continue
            
            # Đổi tên thành công
            # Xóa tên cũ khỏi name_to_id
            del name_to_id[current_name]
            # Cập nhật tên mới
            id_to_name[player_id] = new_name
            name_to_id[new_name] = player_id
            
        elif cmd == "FIND":
            prefix = parts[1]
            
            # Tìm tất cả tên bắt đầu với prefix
            matching_names = []
            for name in name_to_id.keys():
                if name.startswith(prefix):
                    matching_names.append(name)
            
            if not matching_names:
                result.append("ERROR_NOT_FOUND")
            else:
                # Sắp xếp theo thứ tự từ điển ASCII
                matching_names.sort()
                result.append(" ".join(matching_names))
    
    return result

def main():
    data = []
    q = int(input().strip())
    data.append(str(q))
    for _ in range(q):
        query = input().strip()
        data.append(query)
    
    res = solve(data)
    for line in res:
        print(line)

if __name__ == "__main__":
    main()