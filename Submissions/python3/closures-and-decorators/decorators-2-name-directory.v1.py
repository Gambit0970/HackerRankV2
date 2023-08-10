

def person_lister(f):
    def inner(people):
        people = sorted(people, key=lambda x: int(x[2]))
        #people.sort(key=operator.itemgetter(2))
        #temp = []
        #for i in range(len(people)-1):
        #    
        #    for j in range(i+1,len(people)):
        #        if people[i][2] > people[j][2]:
        #            temp = people[j]
        #            people[j] = people[i]
        #            people[i] = temp
        #        else:
        #            i+=1
        #    #print(people[i])
        #    #print(people[j])
        #    #print("*****")
        return (f(p) for p in people)
    return inner

