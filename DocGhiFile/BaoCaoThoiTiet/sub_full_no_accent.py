import json

def load_json(file_path):
    """
    Doc file JSON va tra ve du lieu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve_weather_report(data_json, wind_threshold):
    """
    Giai bai toan bao cao thoi tiet.
    
    Args:
        data_json: danh sach cac thanh pho voi thong tin thoi tiet
        wind_threshold: nguong toc do gio W
    
    Returns:
        list: ket qua gom [thanh pho nhiet do cao nhat, thanh pho do am thap nhat, danh sach thanh pho gio > W]
    """
    results = []
    
    # 1. Tim thanh pho co nhiet do cao nhat
    max_temp_city = max(data_json, key=lambda x: x['temperature_celsius'])
    results.append(max_temp_city['city'])
    
    # 2. Tim thanh pho co do am thap nhat  
    min_humidity_city = min(data_json, key=lambda x: x['humidity_percent'])
    results.append(min_humidity_city['city'])
    
    # 3. Tim cac thanh pho co toc do gio > W, sap xep giam dan theo toc do gio
    high_wind_cities = [city for city in data_json if city['wind_kmh'] > wind_threshold]
    
    if high_wind_cities:
        # Sap xep theo toc do gio giam dan
        high_wind_cities.sort(key=lambda x: x['wind_kmh'], reverse=True)
        for city in high_wind_cities:
            results.append(city['city'])
    else:
        results.append("None")
    
    return results

def main():
    """
    Ham chinh: doc du lieu JSON va input tu ban phim, sau do giai bai toan.
    """
    # Doc du lieu JSON
    data_json = load_json("./data/datas.json")
    
    # Doc nguong toc do gio tu ban phim
    wind_threshold = int(input())
    
    # Giai bai toan
    results = solve_weather_report(data_json, wind_threshold)
    
    # In ket qua
    for result in results:
        print(result)

if __name__ == "__main__":
    main()