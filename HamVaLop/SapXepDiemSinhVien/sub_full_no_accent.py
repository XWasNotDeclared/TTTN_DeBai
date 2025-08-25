def solve(data):
    """
    Ham giai bai toan quan ly danh sach sinh vien.
    - data: danh sach chua thong tin da duoc doc tu input.
    - Tra ve: list chua cac dong ket qua (string).
    """
    result = []
    idx = 0
    t = data[idx]
    idx += 1
    
    for case in range(1, t + 1):
        n = data[idx]
        idx += 1
        
        students = []
        for _ in range(n):
            student_data = data[idx]
            idx += 1
            students.append(student_data)
        
        # Tinh tong diem va chuan bi du lieu cho viec sap xep
        student_list = []
        for student in students:
            parts = student.split()
            student_id = parts[0]
            
            # Tim vi tri cua diem Toan (so thuc dau tien tu cuoi)
            # Lay 5 phan tu cuoi: Toan, Ly, Hoa, Khoa, Lop
            toan = float(parts[-5])
            ly = float(parts[-4])
            hoa = float(parts[-3])
            course = int(parts[-2])
            class_name = parts[-1]
            
            # Ten la tat ca cac phan tu vi tri 1 den truoc diem Toan
            name = " ".join(parts[1:-5])
            
            total = toan + ly + hoa
            
            student_list.append({
                'id': student_id,
                'name': name,
                'total': total,
                'class': class_name,
                'course': course
            })
        
        # Sap xep: giam dan theo tong diem, tang dan theo ma sinh vien neu bang nhau
        student_list.sort(key=lambda x: (-x['total'], x['id']))
        
        # Tao output cho test case nay
        result.append(f"Case #{case}:")
        for student in student_list:
            result.append(f"{student['id']} {student['name']} {student['total']:.2f} {student['class']} {student['course']}")
    
    return result

def main():
    data = []
    t = int(input().strip())
    data.append(t)
    
    for _ in range(t):
        n = int(input().strip())
        data.append(n)
        for _ in range(n):
            student_info = input().strip()
            data.append(student_info)
    
    res = solve(data)
    print("\n".join(res))

if __name__ == "__main__":
    main()