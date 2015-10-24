
def sample_students(inp, n):
    groups = []
    students = set(inp)
    while len(students) > 0:
        cc = random.sample(students, n)
        groups.append(cc)
        students -= set(cc)
    return groups
