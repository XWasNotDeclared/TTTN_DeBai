import json

def read_students_data(filePath):
    """Doc du lieu hoc sinh tu file JSON"""
    try:
        with open(filePath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Khong tim thay file {filePath}")
        return []
    except json.JSONDecodeError:
        print(f"Loi dinh dang JSON trong file {filePath}")
        return []

def filter_students(students, gender, class_name):
    """Loc hoc sinh theo gioi tinh va lop"""
    filtered = []
    for student in students:
        if student['gender'] == gender and student['class'] == class_name:
            filtered.append(student)
    return filtered

def calculate_math_statistics(students):
    """Tinh thong ke diem toan: sum, avg, max, min"""
    if not students:
        return 0.00, 0.00, 0.00, 0.00
    
    math_scores = [student['math'] for student in students]
    
    total = sum(math_scores)
    average = total / len(math_scores)
    maximum = max(math_scores)
    minimum = min(math_scores)
    
    return total, average, maximum, minimum

def main():
    # Doc du lieu tu file students.json
    students = read_students_data("./data/students.json")
    
    # Nhan so luong test cases
    T = int(input().strip())
    
    # Xu ly tung test case
    for _ in range(T):
        # Doc gender va class
        line = input().strip().split()
        gender = line[0]
        class_name = line[1]
        
        # Loc hoc sinh theo dieu kien
        filtered_students = filter_students(students, gender, class_name)
        
        # Tinh thong ke diem toan
        total, avg, maximum, minimum = calculate_math_statistics(filtered_students)
        
        # In ket qua voi 2 chu so thap phan
        print(f"{total:.2f} {avg:.2f} {maximum:.2f} {minimum:.2f}")

if __name__ == "__main__":
    main()