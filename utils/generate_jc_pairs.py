from itertools import combinations
import numpy as np


def main():
    students = ["Daniel", "Nathan", "Taylor", "Lana", "Yunus",
                "Anthony", "Howard", "Brian", "Erik", "Sasha"]
    while students:
        combs = list(combinations(students, 2))
        pair_idx = np.random.choice(np.arange(len(combs)))
        pair = combs[pair_idx]
        students.remove(pair[0])
        students.remove(pair[1])
        print pair

if __name__ == '__main__':
    main()
