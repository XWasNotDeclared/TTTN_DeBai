import json
import os
from collections import Counter

def load_json(file_path):
    """
    Đọc file JSON và trả về dữ liệu.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def solve(data_json, input_data):
    """
    Hàm giải bài toán chính.
    
    Args:
        data_json: dữ liệu JSON đã load.
        input_data: dữ liệu input từ file .in, dạng list các dòng.
    
    Returns:
        list: danh sách kết quả (string) tương ứng với hóa đơn.
    """
    # Tạo dictionary cho products và promotions
    products = {p["id"]: {"name": p["name"], "price": p["price"]} for p in data_json["products"]}
    promotions = {p["product_id"]: p["discount"] for p in data_json["promotions"]}
    
    # Parse input
    line1 = input_data[0].split()
    n, t = int(line1[0]), int(line1[1])
    product_ids = input_data[1].split()
    
    # Đếm số lượng từng sản phẩm
    product_count = Counter(product_ids)
    
    # Tính toán cho từng sản phẩm
    results = []
    total_after_discount = 0
    
    for product_id, quantity in product_count.items():
        if product_id in products:
            product_info = products[product_id]
            name = product_info["name"]
            price = product_info["price"]
            
            # Tính tổng tiền trước giảm giá
            subtotal = price * quantity
            
            # Áp dụng giảm giá nếu có
            discount_percent = promotions.get(product_id, 0)
            discount_amount = subtotal * discount_percent / 100
            subtotal_after_discount = subtotal - discount_amount
            
            # Thêm vào kết quả
            results.append(f"{name} x{quantity}: {int(subtotal_after_discount)} VND")
            total_after_discount += subtotal_after_discount
    
    # Tính thuế VAT
    tax_amount = total_after_discount * t / 100
    final_total = total_after_discount + tax_amount
    
    # Thêm tổng kết
    results.append(f"Tong tien: {int(total_after_discount)} VND")
    results.append(f"Thue VAT {t}%: {int(tax_amount)} VND")
    results.append(f"Tong thanh toan: {int(final_total)} VND")
    
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
    
    with open(infile, "r", encoding="utf-8") as fin, open(outfile, "w", encoding="utf-8") as fout:
        # Đọc dữ liệu file .in
        input_data = [line.strip() for line in fin]
        
        # Gọi hàm solve
        res = solve(data_json, input_data)
        
        # Ghi kết quả ra file .out
        fout.write("\n".join(res) + "\n")

def main():
    """
    Hàm chính: load JSON, tìm các file .in, xử lý từng file.
    """
    # 1. Load dữ liệu JSON
    data_json = load_json("./data/datas.json")
    
    # 2. Chuẩn bị danh sách file input
    in_files = prepare_working_dir()
    
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    
    # 3. Xử lý từng file
    for infile in sorted(in_files):
        process_file(infile, data_json)

if __name__ == "__main__":
    main()