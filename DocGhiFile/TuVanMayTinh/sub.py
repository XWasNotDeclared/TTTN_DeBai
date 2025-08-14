import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_computer_recommendation(computers, cpu, ram, ssd):
    """
    Tìm máy tính phù hợp với cấu hình yêu cầu
    """
    matching_computers = []
    
    for computer in computers:
        if (computer["cpu"] == cpu and 
            computer["ram"] == ram and 
            computer["ssd"] == ssd):
            matching_computers.append(computer)
    
    if not matching_computers:
        return ["Khong co may nao phu hop"]
    
    # Sắp xếp theo giá tăng dần
    matching_computers.sort(key=lambda x: x["gia"])
    
    results = []
    for computer in matching_computers:
        result_line = f"{computer['ten']} {computer['cpu']} {computer['ram']} {computer['ssd']} {computer['gia']}"
        results.append(result_line)
    
    return results

def main():
    """
    Hàm chính đọc từ stdin và xử lý
    """
    # Load dữ liệu từ file JSON
    try:
        computers = load_json("./data/datas.json")
    except FileNotFoundError:
        print("Khong tim thay file datas.json")
        return
    
    # Đọc số lượng test case
    t = int(input().strip())
    
    for _ in range(t):
        # Đọc cấu hình yêu cầu
        line = input().strip()
        cpu, ram, ssd = line.split()
        
        # Tìm và in kết quả
        results = solve_computer_recommendation(computers, cpu, ram, ssd)
        for result in results:
            print(result)

if __name__ == "__main__":
    main()