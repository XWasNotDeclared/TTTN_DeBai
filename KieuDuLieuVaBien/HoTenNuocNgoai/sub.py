#So xen ke chan
import sys

def read_nonempty_line():
    """Đọc dòng không rỗng từ stdin (strip); trả về None nếu EOF."""
    while True:
        line = sys.stdin.readline()
        if not line:
            return None
        line = line.strip()
        if line != '':
            return line

def main():
    first = read_nonempty_line()
    if first is None:
        return
    try:
        t = int(first)
    except ValueError:
        return

    for _ in range(t):
        line = read_nonempty_line()
        if line is None:
            # nếu thiếu dòng, dừng sớm
            break
        parts = line.split()
        # nếu có nhiều hơn 3 từ, lấy 3 đầu; nếu ít hơn, gán rỗng để không crash
        if len(parts) >= 3:
            ho, tendem, tenchinh = parts[0], parts[1], parts[2]
        else:
            # đệm phần thiếu bằng chuỗi rỗng (theo đề không xảy ra, nhưng an toàn)
            parts += [''] * (3 - len(parts))
            ho, tendem, tenchinh = parts[0], parts[1], parts[2]
        # in theo định dạng: <Tên_chính> <Họ> <Tên_đệm>
        print(f"{tenchinh} {ho} {tendem}")

if __name__ == '__main__':
    main()
