import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_single_testcase(devices, target_temp, target_humidity, target_light):
    """
    Giải một test case đơn.
    
    Args:
        devices: danh sách thiết bị từ JSON
        target_temp: nhiệt độ chuẩn
        target_humidity: độ ẩm chuẩn  
        target_light: ánh sáng chuẩn
    
    Returns:
        list: danh sách kết quả cho test case này
    """
    results = []
    
    # Sắp xếp thiết bị theo ID tăng dần
    sorted_devices = sorted(devices, key=lambda x: x["id"])
    
    for device in sorted_devices:
        device_id = device["id"]
        current_temp = device["nhiet_do"]
        current_humidity = device["do_am"]
        current_light = device["anh_sang"]
        
        # Tính delta (cần tăng/giảm)
        delta_temp = target_temp - current_temp
        delta_humidity = target_humidity - current_humidity
        delta_light = target_light - current_light
        
        # Làm tròn đến 1 chữ số thập phân
        delta_temp = round(delta_temp, 1)
        delta_humidity = round(delta_humidity, 1)
        delta_light = round(delta_light, 1)
        
        # Format output: id delta_T delta_D delta_A
        result_line = f"{device_id} {delta_temp} {delta_humidity} {delta_light}"
        results.append(result_line)
    
    return results

def main():
    """
    Hàm chính: đọc từ stdin và xử lý
    """
    # Load dữ liệu JSON
    try:
        data_json = load_json("./data/datas.json")
        devices = data_json["devices"]
    except FileNotFoundError:
        print("Không tìm thấy file ./data/datas.json")
        return
    except KeyError:
        print("File JSON không có key 'devices'")
        return
    
    # Đọc số test case
    t = int(input().strip())
    
    all_results = []
    
    for i in range(t):
        # Đọc thông số chuẩn cho test case này
        line = input().strip()
        target_temp, target_humidity, target_light = map(float, line.split())
        
        # Giải test case
        testcase_results = solve_single_testcase(devices, target_temp, target_humidity, target_light)
        
        # Thêm vào kết quả tổng
        if i > 0:  # Thêm dòng trắng giữa các test case (trừ test case đầu)
            all_results.append("")
        
        all_results.extend(testcase_results)
    
    # In kết quả
    for result in all_results:
        print(result)

if __name__ == "__main__":
    main()