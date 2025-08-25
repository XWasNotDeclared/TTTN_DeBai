def solve(data):
    """
    Ham giai bai toan chinh.
    - data: danh sach cac dong truy van da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string).
    """
    company = {}  # Dictionary long nhau: {phong_ban: {ten_nv: sdt}}
    result = []
    
    q = int(data[0])
    
    for i in range(1, q + 1):
        query = data[i].strip().split()
        command = query[0]
        
        if command == "ADD":
            phong_ban = query[1]
            ten_nv = query[2]
            sdt = query[3]
            
            if phong_ban not in company:
                company[phong_ban] = {}
            company[phong_ban][ten_nv] = sdt
            
        elif command == "DEL":
            phong_ban = query[1]
            ten_nv = query[2]
            
            if phong_ban in company and ten_nv in company[phong_ban]:
                del company[phong_ban][ten_nv]
                
        elif command == "FIND":
            phong_ban = query[1]
            ten_nv = query[2]
            
            if phong_ban in company and ten_nv in company[phong_ban]:
                result.append(company[phong_ban][ten_nv])
            else:
                result.append("NOT FOUND")
                
        elif command == "LIST":
            phong_ban = query[1]
            
            if phong_ban in company and company[phong_ban]:
                # Sap xep theo thu tu tu dien cua ten nhan vien
                sorted_employees = sorted(company[phong_ban].items())
                employee_list = [f"{ten}:{sdt}" for ten, sdt in sorted_employees]
                result.append(" ".join(employee_list))
            else:
                result.append("EMPTY")
    
    return result

def main():
    data = []
    q = int(input().strip())
    data.append(str(q))
    
    for _ in range(q):
        line = input().strip()
        data.append(line)
    
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()