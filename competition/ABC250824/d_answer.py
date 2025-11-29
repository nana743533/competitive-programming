from collections import defaultdict as dd, deque, Counter


def main():
    H, W = map(int, input().split())
    A = [input() for _ in range(H)]                            #! この入力内包表記
    Dist = [[[0] * 2 for _ in range(W)] for _ in range(H)]

    queue = deque()
    sy, sx = 0, 0
    gy, gx = 0, 0
    for y in range(H):
        for x in range(W):
            if A[y][x] == 'S':
                sy, sx = y, x
            if A[y][x] == 'G':
                gy, gx = y, x
    queue.append((sy, sx, 0))
    Dist[sy][sx][0] = 1

    dyx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        y, x, t = queue.popleft()
        if (y, x) == (gy, gx):
            print(Dist[y][x][t] - 1)
            return
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            nt = t
            if 0 <= ny < H and 0 <= nx < W:
                if A[ny][nx] == '?':
                    nt = (t + 1) % 2
                if A[ny][nx] != '#' and Dist[ny][nx][nt] == 0:
                    close_door = (A[ny][nx] == 'x' and t == 0) or (A[ny][nx] == 'o' and t == 1)
                    if not close_door:
                        Dist[ny][nx][nt] = Dist[y][x][t] + 1
                        queue.append((ny, nx, nt))
    print(-1)
    pass


if __name__ == '__main__':
    main()
