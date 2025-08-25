#So xen ke chan
import sys

def read_nonempty_line():
    """Doc dong khong rong tu stdin (strip); tra ve None neu EOF."""
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
            # neu thieu dong, dung som
            break
        parts = line.split()
        # neu co nhieu hon 3 tu, lay 3 dau; neu it hon, gan rong de khong crash
        if len(parts) >= 3:
            ho, tendem, tenchinh = parts[0], parts[1], parts[2]
        else:
            # dem phan thieu bang chuoi rong (theo de khong xay ra, nhung an toan)
            parts += [''] * (3 - len(parts))
            ho, tendem, tenchinh = parts[0], parts[1], parts[2]
        # in theo dinh dang: <Ten_chinh> <Ho> <Ten_dem>
        print(f"{tenchinh} {ho} {tendem}")

if __name__ == '__main__':
    main()
