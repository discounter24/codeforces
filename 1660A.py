# https://codeforces.com/problemset/problem/1660/A


def solve(coin1, coin2):
    if coin1 == 0:
        return 1

    return coin1 + 2*coin2 + 1


if __name__ == '__main__':
    n_cases = int(input())

    while(n_cases > 0):
        n_cases -= 1
        burles = input().split(" ")
        assert len(burles) == 2, "Invalid input"
        burles = [int(x) for x in burles]
        print(solve(burles[0], burles[1]))
