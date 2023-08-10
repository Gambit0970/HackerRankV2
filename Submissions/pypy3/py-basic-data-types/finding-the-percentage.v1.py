if __name__ == '__main__':
    total = 0
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = student_marks[query_name]
    for i in l:
        total += i
    print("{:.2f}".format(total/len(l)))
