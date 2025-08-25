def solve(num):
    for _ in range(num):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

        leftA, rightA = min(x1, x2), max(x1, x2)
        bottomA, topA = min(y1, y2), max(y1, y2)

        leftB, rightB = min(x3, x4), max(x3, x4)
        bottomB, topB = min(y3, y4), max(y3, y4)

        if rightA < leftB or rightB < leftA or topA < bottomB or topB < bottomA:
            print("NO")
        else:
            print("YES")


def main():
    n = int(input())
    solve(n)


if __name__ == "__main__":
    main()