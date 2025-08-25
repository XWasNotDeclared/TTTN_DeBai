import json
import os

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_computer_recommendation(computers, cpu, ram, ssd):
    """
    Tim may tinh phu hop voi cau hinh yeu cau
    """
    matching_computers = []
    
    for computer in computers:
        if (computer["cpu"] == cpu and 
            computer["ram"] == ram and 
            computer["ssd"] == ssd):
            matching_computers.append(computer)
    
    if not matching_computers:
        return ["Khong co may nao phu hop"]
    
    # Sap xep theo gia tang dan
    matching_computers.sort(key=lambda x: x["gia"])
    
    results = []
    for computer in matching_computers:
        result_line = f"{computer['ten']} {computer['cpu']} {computer['ram']} {computer['ssd']} {computer['gia']}"
        results.append(result_line)
    
    return results

def main():
    """
    Ham chinh doc tu stdin va xu ly
    """
    # Load du lieu tu file JSON
    try:
        computers = load_json("./data/datas.json")
    except FileNotFoundError:
        print("Khong tim thay file datas.json")
        return
    
    # Doc so luong test case
    t = int(input().strip())
    
    for _ in range(t):
        # Doc cau hinh yeu cau
        line = input().strip()
        cpu, ram, ssd = line.split()
        
        # Tim va in ket qua
        results = solve_computer_recommendation(computers, cpu, ram, ssd)
        for result in results:
            print(result)

if __name__ == "__main__":
    main()