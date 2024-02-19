def get_combinations(n, c):
    return []


if __name__ == "__main__":
    with open("case_3.txt", "r") as cases_file:
        cases = []
        solutions = []
        for line in cases_file:
            if line.strip():
                c, a = line.strip().split(",")
                cases.append([list(x) for x in c.split("|")])
                solutions.append(a.split("|"))

        for i in range(len(cases)):
            r = get_combinations(len(cases[i]), cases[i])
            a = set("".join(x) for x in r)
            b = set(solutions[i])
            for x in a:
                b.discard(x)
            print(f"Case {i + 1} : {'OK' if len(b) == 0 else 'FAIL'}")
