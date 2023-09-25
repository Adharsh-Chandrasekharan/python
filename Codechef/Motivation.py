# cook your dish here
T = int(input())

for tc in range(T):
    (n, x) = map(int, input().split(" "))

    max_r = 0

    for i in range(n):
        (s, r) = map(int, input().split(" "))

        if r > max_r and s <= x:
            max_r = r

    print(max_r)