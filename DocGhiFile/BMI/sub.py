import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def calculate_bmi_status(weight_kg, height_m):
    """
    Tính BMI và trả về trạng thái tương ứng.
    """
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        return 1
    elif 18.5 <= bmi < 25:
        return 2
    elif 25 <= bmi < 30:
        return 3
    else:  # bmi >= 30
        return 4

def solve():
    """
    Hàm giải bài toán chính - đọc từ bàn phím và file JSON.
    """
    # Đọc dữ liệu từ file JSON
    data_json = load_json("./data/datas.json")
    
    # Tạo dictionary để tra cứu nhanh theo id
    person_dict = {person["id"]: person for person in data_json}
    
    # Đọc input từ bàn phím
    n = int(input())
    ids = list(map(int, input().split()))
    
    results = []
    
    for person_id in ids:
        if person_id in person_dict:
            person = person_dict[person_id]
            status = calculate_bmi_status(person["weight_kg"], person["height_m"])
            results.append(f"{person_id} {status}")
        else:
            results.append(f"{person_id} NOT FOUND")
    
    return results

def main():
    """
    Hàm chính.
    """
    results = solve()
    for result in results:
        print(result)

if __name__ == "__main__":
    main()