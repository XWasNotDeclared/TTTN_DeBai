def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        x = list(map(int, input().split()))
        
        min_x = x[0]
        max_x = x[-1]
        
        # Tinh buoc di neu di tu s den min_x roi di den max_x
        dist1 = abs(s - min_x) + (max_x - min_x)
        # Tinh buoc di neu di tu s den max_x roi di den min_x
        dist2 = abs(s - max_x) + (max_x - min_x)
        
        print(min(dist1, dist2))


def main():
    solve()


if __name__ == "__main__":
    main()
