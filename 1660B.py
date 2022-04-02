
# https://codeforces.com/problemset/problem/1660/B

def solve(candies):
    if len(candies) == 1:
        return sum(candies) <= 1
    candies = sorted(candies, reverse=True)
    return candies[0] - candies[1] <= 1


if __name__ == '__main__':
    n_cases = int(input())

    while(n_cases > 0):
        n_cases -= 1
        n_candyTypes = int(input())
        candiesInput = input().split(" ")
        assert len(candiesInput) == n_candyTypes, "Invalid input"
        candies = [int(x) for x in candiesInput]
        if solve(candies):
            print("YES")
        else:
            print("NO")
