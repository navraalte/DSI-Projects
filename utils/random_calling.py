import numpy.random as rng
students = ["Brian", "Daniel", "Nathan", "Howard", "Erik", "Sasha",
            "Yunus", "Anthony", "Lana", "Taylor"]


def caller():
    return rng.choice(students)
