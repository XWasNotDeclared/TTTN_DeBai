def collide(rect1, rect2):
    """Kiem tra va cham hoac tiep xuc giua 2 hinh chu nhat."""
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    ax_min, ax_max = min(x1, x2), max(x1, x2)
    ay_min, ay_max = min(y1, y2), max(y1, y2)
    bx_min, bx_max = min(x3, x4), max(x3, x4)
    by_min, by_max = min(y3, y4), max(y3, y4)

    # Khong va cham khi mot hinh hoan toan nam ngoai hinh kia
    if ax_max < bx_min or bx_max < ax_min or ay_max < by_min or by_max < ay_min:
        return False
    return True


def solve():
    """Doc input tu ban phim va in ket qua."""
    T = int(input().strip())  # so bo test

    for _ in range(T):
        m = int(input().strip())  # so hinh chu nhat
        rects = []
        for _ in range(m):
            rects.append(tuple(map(int, input().split())))

        found = False
        for i in range(m):
            for j in range(i + 1, m):
                if collide(rects[i], rects[j]):
                    print(f"{i+1}-{j+1}")
                    found = True
        if not found:
            print("NO COLLISION")
        print("*****")


if __name__ == "__main__":
    solve()
