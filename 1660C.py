# https://codeforces.com/problemset/problem/1660/C


def solve(input):
    removed = 0

    if len(input) == 0:
        return (0, "")
    elif len(input) == 1:
        return (1, "")

    else:
        p = 0
        while p < len(input):

            if p+1 >= len(input):
                # Remove last (uneven) char
                input = input[:p]
                removed += 1
                break

            if input[p] == input[p+1]:
                #input = input[p+2:]
                p += 2
            else:

                next_p1 = -1
                next_p2 = -1

                try:
                    next_p1 = input.index(input[p], p+2)
                except (ValueError):
                    # Remoive charachter as we can't make the string even without another occurence
                    input = input[:p] + input[p+1:]
                    removed += 1
                    continue

                try:
                    next_p2 = input.index(input[p+1], p+2)
                except (ValueError):
                    # Remove charachter as we can't make the string even without another occurence
                    input = input[:p+1] + input[p+2:]
                    removed += 1
                    continue

                if next_p1 <= next_p2:
                    # Distance to next identicial charachter is shorter for the first charachter -> Remove the second char
                    input = input[:p+1] + input[p+2:]
                else:
                    # Distance to next identicial charachter is shorter for the second charachter -> Remove the first char
                    input = input[:p] + input[p+1:]

                removed += 1

    return (input, removed)


# if __name__ == '__main__':
#     n_cases = int(input())

#     while(n_cases > 0):
#         n_cases -= 1
#         print(solve(input())[0])


if __name__ == "__main__":
    tests = [("aabbdabdccc", 3),
             ("zyx", 3),
             ("aaababbb", 2),
             ("aabbcc", 0),
             ("oaoaaaoo", 2),
             ("bmefbmuyw", 7),
             ("aaaaa", 1),
             ("abba", 2)]

    for test in tests:
        r = solve(test[0])
        print(r)
        assert(r[1] == test[1])

    while(True):
        print(solve(input()))
