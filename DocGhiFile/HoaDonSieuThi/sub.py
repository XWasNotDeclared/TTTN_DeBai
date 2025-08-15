import json
import sys
from collections import Counter

def load_json(file_path):
    """Đọc file JSON và trả về dữ liệu."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_path}")
        return None

def solve_invoice():
    """Giải bài toán hóa đơn siêu thị từ input bàn phím."""
    
    # Đọc dữ liệu từ file JSON
    data = load_json("./data/datas.json")
    if not data:
        return
    
    # Tạo dictionary cho products và promotions để tra cứu nhanh
    products = {p["id"]: {"name": p["name"], "price": p["price"]} for p in data["products"]}
    promotions = {p["product_id"]: p["discount"] for p in data["promotions"]}
    
    # Đọc input từ bàn phím
    line1 = input().strip().split()
    n, t = int(line1[0]), int(line1[1])
    
    product_ids = input().strip().split()
    
    # Đếm số lượng từng sản phẩm
    product_count = Counter(product_ids)
    
    # Tính toán cho từng sản phẩm
    invoice_lines = []
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
            
            # Thêm vào hóa đơn
            invoice_lines.append(f"{name} x{quantity}: {int(subtotal_after_discount)} VND")
            total_after_discount += subtotal_after_discount
    
    # Tính thuế VAT
    tax_amount = total_after_discount * t / 100
    final_total = total_after_discount + tax_amount
    
    # In hóa đơn
    for line in invoice_lines:
        print(line)
    
    print(f"Tong tien: {int(total_after_discount)} VND")
    print(f"Thue VAT {t}%: {int(tax_amount)} VND")
    print(f"Tong thanh toan: {int(final_total)} VND")

if __name__ == "__main__":
    solve_invoice()