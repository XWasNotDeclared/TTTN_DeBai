import json
import os

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve(data_json, input_data):
    """
    Hàm giải bài toán chính - tìm SIM theo 3 số cuối.
    
    Args:
        data_json: dữ liệu JSON đã load (chứa sim và price).
        input_data: dữ liệu input từ file .in (list các dòng).
    
    Returns:
        list: danh sách kết quả (string) tương ứng với từng SIM tìm được.
    """
    results = []
    
    # Lấy 3 số cuối từ input_data (dòng đầu tiên)
    last_three_digits = input_data[0].strip()
    
    # Tạo dictionary để tra cứu giá theo type nhanh hơn
    price_dict = {}
    for price_info in data_json["price"]:
        price_dict[price_info["type"]] = price_info["price"]
    
    # Duyệt qua tất cả SIM để tìm những SIM có 3 số cuối khớp
    for sim in data_json["sim"]:
        sim_number = sim["number"]
        if sim_number.endswith(last_three_digits):
            # Lấy thông tin SIM
            network = sim["network"]
            active = str(sim["active"]).lower()  # chuyển về lowercase string
            sim_type = sim["type"]
            price = price_dict.get(sim_type, 0)  # lấy giá theo type
            
            # Format kết quả: <số> <nhà mạng> <trạng thái> <giá>
            result_line = f"{sim_number} {network} {active} {price}"
            results.append(result_line)
    
    return results

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Trả về danh sách file .in trong thư mục.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile, data_json):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    
    Args:
        infile: tên file input
        data_json: dữ liệu từ JSON
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Processing {infile} -> {outfile} ...")
    
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu file .in (mỗi dòng là một string)
        input_data = [line.strip() for line in fin]
        
        # Gọi hàm solve
        results = solve(data_json, input_data)
        
        # Ghi kết quả ra file .out
        if results:
            fout.write("\n".join(results) + "\n")
        else:
            # Nếu không tìm thấy SIM nào, ghi file rỗng hoặc thông báo
            fout.write("")

def main():
    """
    Hàm chính: load JSON, tìm các file .in, xử lý từng file.
    """
    try:
        # 1. Load dữ liệu JSON
        data_json = load_json("./data/datas.json")  # đổi đường dẫn file JSON nếu cần
        
        # 2. Chuẩn bị danh sách file input
        in_files = prepare_working_dir()
        if not in_files:
            print("Không tìm thấy file .in nào trong", os.getcwd())
            return
        
        # 3. Xử lý từng file
        for infile in sorted(in_files):
            process_file(infile, data_json)
            
        print("Hoàn thành sinh test!")
        
    except FileNotFoundError:
        print("Không tìm thấy file datas.json")
    except KeyError as e:
        print(f"Lỗi cấu trúc dữ liệu JSON: {e}")
    except Exception as e:
        print(f"Lỗi: {e}")

if __name__ == "__main__":
    main()