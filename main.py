import random

def count_paths(m, forbidden):
    dp = [[0] * m for _ in range(m)]
    dp[0][0] = 1 if (0, 0) not in forbidden else 0

    for i in range(m):
        for j in range(m):
            if (i, j) in forbidden:
                dp[i][j] = 0
                continue
            if i > 0:
                dp[i][j] += dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i][j - 1]

    return dp[m - 1][m - 1], dp

def generate_forbidden_cells(m, num_forbidden):
    forbidden = set()
    while len(forbidden) < num_forbidden:
        x = random.randint(0, m - 1)
        y = random.randint(0, m - 1)
        if (x, y) != (0, 0) and (x, y) != (m - 1, m - 1):
            forbidden.add((x, y))
    return forbidden

def print_matrix(m, forbidden, dp):
    for i in range(m):
        for j in range(m):
            if (i, j) in forbidden:
                print('X', end=' ')
            elif dp[i][j] > 0:
                print('O', end=' ')
            else:
                print('.', end=' ')
        print()  # Új sor

def main():
    m = int(input("Kérem, adja meg a táblázat méretét (m): "))
    num_forbidden = int(input("Kérem, adja meg a tiltott mezők számát: "))

    forbidden = generate_forbidden_cells(m, num_forbidden)
    print(f"Tiltott mezők: {forbidden}")

    result, dp = count_paths(m, forbidden)
    print(f'A célba érkezés módjainak száma: {result}')
   
    print("A mátrix:")
    print_matrix(m, forbidden, dp)

if __name__ == "__main__":
    main()