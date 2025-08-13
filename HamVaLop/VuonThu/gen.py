import os

def solve(data):
    """
    Hàm giải bài toán Smart Zoo Manager.
    - data: danh sách các chuỗi đã được đọc từ input.
    - Trả về: list chứa các dòng kết quả (string).
    """
    idx = 0
    n = int(data[idx])
    idx += 1
    
    # Khởi tạo danh sách động vật
    animals = {}
    species_count = {"Dog": 0, "Cat": 0, "Bird": 0}
    
    # Đọc thông tin N con vật
    for _ in range(n):
        parts = data[idx].split()
        species, name, age, weight = parts[0], parts[1], int(parts[2]), float(parts[3])
        animals[name] = {
            'species': species,
            'age': age,
            'weight': weight
        }
        species_count[species] += 1
        idx += 1
    
    # Đọc số lệnh Q
    q = int(data[idx])
    idx += 1
    
    result = []
    
    # Xử lý Q lệnh
    for _ in range(q):
        command = data[idx].split()
        idx += 1
        
        if command[0] == "SOUND":
            name = command[1]
            species = animals[name]['species']
            if species == "Dog":
                result.append("Woof")
            elif species == "Cat":
                result.append("Meow")
            elif species == "Bird":
                result.append("Chirp")
                
        elif command[0] == "SPECIAL":
            name = command[1]
            species = animals[name]['species']
            if species == "Dog":
                result.append("Fetch")
            elif species == "Cat":
                result.append("Scratch")
            elif species == "Bird":
                result.append("Fly")
                
        elif command[0] == "FEED":
            name = command[1]
            weight_inc = float(command[2])
            animals[name]['weight'] += weight_inc
            # FEED không cần output
            
        elif command[0] == "STAT":
            species = command[1]
            result.append(str(species_count[species]))
    
    return result

def prepare_working_dir():
    """
    Chuyển thư mục làm việc về nơi chứa script hiện tại.
    Tìm và trả về danh sách tất cả các file .in trong thư mục đó.
    """
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)
    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files

def process_file(infile):
    """
    Xử lý một file .in và tạo file .out tương ứng.
    Giữ nguyên phần này cho các bài sau, trừ khi định dạng input/output thay đổi.
    """
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")
    with open(infile, "r") as fin, open(outfile, "w") as fout:
        # Đọc dữ liệu từ file input
        lines = fin.read().strip().split('\n')
        data = lines
        # Gọi hàm giải
        res = solve(data)
        # Ghi kết quả ra file output
        if res:
            fout.write("\n".join(map(str, res)) + "\n")
        else:
            fout.write("")

def main():
    """
    Hàm chính: tìm các file input, xử lý từng file, tạo file output.
    """
    in_files = prepare_working_dir()
    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return
    for infile in sorted(in_files):
        process_file(infile)

if __name__ == "__main__":
    main()