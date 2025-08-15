import json

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_weather_report(data_json, wind_threshold):
    """
    Giải bài toán báo cáo thời tiết.
    
    Args:
        data_json: danh sách các thành phố với thông tin thời tiết
        wind_threshold: ngưỡng tốc độ gió W
    
    Returns:
        list: kết quả gồm [thành phố nhiệt độ cao nhất, thành phố độ ẩm thấp nhất, danh sách thành phố gió > W]
    """
    results = []
    
    # 1. Tìm thành phố có nhiệt độ cao nhất
    max_temp_city = max(data_json, key=lambda x: x['temperature_celsius'])
    results.append(max_temp_city['city'])
    
    # 2. Tìm thành phố có độ ẩm thấp nhất  
    min_humidity_city = min(data_json, key=lambda x: x['humidity_percent'])
    results.append(min_humidity_city['city'])
    
    # 3. Tìm các thành phố có tốc độ gió > W, sắp xếp giảm dần theo tốc độ gió
    high_wind_cities = [city for city in data_json if city['wind_kmh'] > wind_threshold]
    
    if high_wind_cities:
        # Sắp xếp theo tốc độ gió giảm dần
        high_wind_cities.sort(key=lambda x: x['wind_kmh'], reverse=True)
        for city in high_wind_cities:
            results.append(city['city'])
    else:
        results.append("None")
    
    return results

def main():
    """
    Hàm chính: đọc dữ liệu JSON và input từ bàn phím, sau đó giải bài toán.
    """
    # Đọc dữ liệu JSON
    data_json = load_json("./data/datas.json")
    
    # Đọc ngưỡng tốc độ gió từ bàn phím
    wind_threshold = int(input())
    
    # Giải bài toán
    results = solve_weather_report(data_json, wind_threshold)
    
    # In kết quả
    for result in results:
        print(result)

if __name__ == "__main__":
    main()