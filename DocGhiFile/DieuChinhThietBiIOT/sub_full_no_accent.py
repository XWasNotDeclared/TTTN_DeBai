import json
import os

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_single_testcase(devices, target_temp, target_humidity, target_light):
    """
    Giai mot test case don.
    
    Args:
        devices: danh sach thiet bi tu JSON
        target_temp: nhiet do chuan
        target_humidity: do am chuan  
        target_light: anh sang chuan
    
    Returns:
        list: danh sach ket qua cho test case nay
    """
    results = []
    
    # Sap xep thiet bi theo ID tang dan
    sorted_devices = sorted(devices, key=lambda x: x["id"])
    
    for device in sorted_devices:
        device_id = device["id"]
        current_temp = device["nhiet_do"]
        current_humidity = device["do_am"]
        current_light = device["anh_sang"]
        
        # Tinh delta (can tang/giam)
        delta_temp = target_temp - current_temp
        delta_humidity = target_humidity - current_humidity
        delta_light = target_light - current_light
        
        # Lam tron den 1 chu so thap phan
        delta_temp = round(delta_temp, 1)
        delta_humidity = round(delta_humidity, 1)
        delta_light = round(delta_light, 1)
        
        # Format output: id delta_T delta_D delta_A
        result_line = f"{device_id} {delta_temp} {delta_humidity} {delta_light}"
        results.append(result_line)
    
    return results

def main():
    """
    Ham chinh: doc tu stdin va xu ly
    """
    # Load du lieu JSON
    try:
        data_json = load_json("./data/datas.json")
        devices = data_json["devices"]
    except FileNotFoundError:
        print("Khong tim thay file ./data/datas.json")
        return
    except KeyError:
        print("File JSON khong co key 'devices'")
        return
    
    # Doc so test case
    t = int(input().strip())
    
    all_results = []
    
    for i in range(t):
        # Doc thong so chuan cho test case nay
        line = input().strip()
        target_temp, target_humidity, target_light = map(float, line.split())
        
        # Giai test case
        testcase_results = solve_single_testcase(devices, target_temp, target_humidity, target_light)
        
        # Them vao ket qua tong
        if i > 0:  # Them dong trang giua cac test case (tru test case dau)
            all_results.append("")
        
        all_results.extend(testcase_results)
    
    # In ket qua
    for result in all_results:
        print(result)

if __name__ == "__main__":
    main()