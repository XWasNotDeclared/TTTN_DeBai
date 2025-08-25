def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach cac dong query da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string).
    """
    q = int(data[0])
    queries = data[1:q+1]
    
    # Luu tru thong tin nguoi choi
    id_to_name = {}  # id -> name hien tai
    name_to_id = {}  # name -> id (de check trung ten)
    
    result = []
    
    for query in queries:
        parts = query.strip().split()
        cmd = parts[0]
        
        if cmd == "REGISTER":
            player_id = int(parts[1])
            name = parts[2]
            
            # Kiem tra ID da ton tai
            if player_id in id_to_name:
                result.append("ERROR_DUPLICATE_ID")
                continue
            
            # Kiem tra ten da ton tai
            if name in name_to_id:
                result.append("ERROR_DUPLICATE_NAME")
                continue
            
            # Dang ky thanh cong
            id_to_name[player_id] = name
            name_to_id[name] = player_id
            
        elif cmd == "RENAME":
            player_id = int(parts[1])
            new_name = parts[2]
            
            # Kiem tra ID ton tai
            if player_id not in id_to_name:
                result.append("ERROR_ID_NOT_FOUND")
                continue
            
            current_name = id_to_name[player_id]
            
            # Kiem tra ten moi trung voi ten hien tai
            if new_name == current_name:
                result.append("ERROR_SAME_NAME")
                continue
            
            # Kiem tra ten moi da duoc su dung
            if new_name in name_to_id:
                result.append("ERROR_DUPLICATE_NAME")
                continue
            
            # Doi ten thanh cong
            # Xoa ten cu khoi name_to_id
            del name_to_id[current_name]
            # Cap nhat ten moi
            id_to_name[player_id] = new_name
            name_to_id[new_name] = player_id
            
        elif cmd == "FIND":
            prefix = parts[1]
            
            # Tim tat ca ten bat dau voi prefix
            matching_names = []
            for name in name_to_id.keys():
                if name.startswith(prefix):
                    matching_names.append(name)
            
            if not matching_names:
                result.append("ERROR_NOT_FOUND")
            else:
                # Sap xep theo thu tu tu dien ASCII
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