import json

def read_students_data(filePath):
    """Đọc dữ liệu học sinh từ file JSON"""
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Không tìm thấy file {filePath}")
        return []
    except json.JSONDecodeError:
        print(f"Lỗi định dạng JSON trong file {filePath}")
        return []

def filter_students(students, gender, class_name):
    """Lọc học sinh theo giới tính và lớp"""
    filtered = []
    for student in students:
        if student['gender'] == gender and student['class'] == class_name:
            filtered.append(student)
    return filtered

def calculate_math_statistics(students):
    """Tính thống kê điểm toán: sum, avg, max, min"""
    if not students:
        return 0.00, 0.00, 0.00, 0.00
    
    math_scores = [student['math'] for student in students]
    
    total = sum(math_scores)
    average = total / len(math_scores)
    maximum = max(math_scores)
    minimum = min(math_scores)
    
    return total, average, maximum, minimum

def main():
    # Đọc dữ liệu từ file students.json
    students = read_students_data("./data/students.json")
    
    # Nhận số lượng test cases
    T = int(input().strip())
    
    # Xử lý từng test case
    for _ in range(T):
        # Đọc gender và class
        line = input().strip().split()
        gender = line[0]
        class_name = line[1]
        
        # Lọc học sinh theo điều kiện
        filtered_students = filter_students(students, gender, class_name)
        
        # Tính thống kê điểm toán
        total, avg, maximum, minimum = calculate_math_statistics(filtered_students)
        
        # In kết quả với 2 chữ số thập phân
        print(f"{total:.2f} {avg:.2f} {maximum:.2f} {minimum:.2f}")

if __name__ == "__main__":
    main()