if __name__ == '__main__':
    students = list()
    scores = list()
    names = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        if score not in scores:
            scores.append(score)
    scores.sort()
    nextMin = scores[1]
    for [name,score] in students:
        if score == nextMin:
            names.append(name)
    names.sort()
    #print(names)
    for name in names:
        print(name)
        
