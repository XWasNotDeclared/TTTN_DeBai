def solve(data):
    """
    Hàm giải bài toán quản lý danh sách sinh viên.
    - data: danh sách chứa thông tin đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
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
        
        # Tính tổng điểm và chuẩn bị dữ liệu cho việc sắp xếp
        student_list = []
        for student in students:
            parts = student.split()
            student_id = parts[0]
            
            # Tìm vị trí của điểm Toán (số thực đầu tiên từ cuối)
            # Lấy 5 phần tử cuối: Toán, Lý, Hóa, Khóa, Lớp
            toan = float(parts[-5])
            ly = float(parts[-4])
            hoa = float(parts[-3])
            course = int(parts[-2])
            class_name = parts[-1]
            
            # Tên là tất cả các phần từ vị trí 1 đến trước điểm Toán
            name = " ".join(parts[1:-5])
            
            total = toan + ly + hoa
            
            student_list.append({
                'id': student_id,
                'name': name,
                'total': total,
                'class': class_name,
                'course': course
            })
        
        # Sắp xếp: giảm dần theo tổng điểm, tăng dần theo mã sinh viên nếu bằng nhau
        student_list.sort(key=lambda x: (-x['total'], x['id']))
        
        # Tạo output cho test case này
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