def get_combinations(n: int, c: list[list[str]]) -> list[str]:
    # with FSM - (Finite-State Machine)
    combinations = [] # will be returned
    termination_indexes = [len(group) for group in c] # termination indexes for each group
    initial_indexes = [0] * n # initial indexes for each group

    while True:
        combination = [c[i][initial_indexes[i]] for i in range(n)] # create a combination with current state
        combinations.append(combination)
        
        i = 0
        while i < n:
            initial_indexes[i] += 1
            if initial_indexes[i] == termination_indexes[i]:
                initial_indexes[i] = 0
                i += 1
            else:
                break
        else:
            break
    
    return combinations

def get_combinations_alternatife(n,c):
    # Alternative solution shorthly
    from itertools import product
    
    return [list(x) for x in product(*c)]


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
