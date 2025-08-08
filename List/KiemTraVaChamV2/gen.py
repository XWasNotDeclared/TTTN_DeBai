import os

def collide(rect1, rect2):
    """Kiểm tra va chạm giữa 2 hình chữ nhật."""
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    ax_min, ax_max = min(x1, x2), max(x1, x2)
    ay_min, ay_max = min(y1, y2), max(y1, y2)
    bx_min, bx_max = min(x3, x4), max(x3, x4)
    by_min, by_max = min(y3, y4), max(y3, y4)

    if ax_max < bx_min or bx_max < ax_min or ay_max < by_min or by_max < ay_min:
        return False
    return True


def solve(nums):
    """Giải bài toán từ list số nguyên."""
    idx = 0
    T = nums[idx]; idx += 1
    output = []

    for _ in range(T):
        m = nums[idx]; idx += 1
        rects = []
        for _ in range(m):
            rects.append(tuple(nums[idx:idx+4]))
            idx += 4

        found = False
        for i in range(m):
            for j in range(i + 1, m):
                if collide(rects[i], rects[j]):
                    output.append(f"{i+1}-{j+1}")
                    found = True
        if not found:
            output.append("NO COLLISION")
        output.append("*****")

    return output


def prepare_working_dir():
    """Chuyển thư mục làm việc về nơi chứa script và trả về danh sách file .in."""
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    in_files = [f for f in os.listdir(".") if f.lower().endswith(".in")]
    return in_files


def process_file(infile):
    """Xử lý một file .in và tạo file .out."""
    outfile = infile.rsplit(".", 1)[0] + ".out"
    print(f"Đang xử lý {infile} -> {outfile} ...")

    with open(infile, "r") as fin, open(outfile, "w") as fout:
        data = list(map(int, fin.read().strip().split()))
        res = solve(data)
        fout.write("\n".join(res) + "\n")


def main():
    in_files = prepare_working_dir()

    if not in_files:
        print("Không tìm thấy file .in nào trong", os.getcwd())
        return

    for infile in sorted(in_files):
        process_file(infile)


if __name__ == "__main__":
    main()
