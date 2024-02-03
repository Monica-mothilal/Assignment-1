def star_pattern2(n):
    for i in range(n, 0, -1 ):
        for j in range(1, i + 1):
            print("* ", end="")
        print()
n=6
star_pattern2(n)

