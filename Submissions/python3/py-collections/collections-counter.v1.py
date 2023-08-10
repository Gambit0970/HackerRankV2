total = 0
shoes = int(input())
sizes = [int(x) for x in input().split(" ")]
customers = int(input())
shoesWanted = []
for customer in range(customers):
    shoe,cost = input().split(" ")
    if int(shoe) in sizes:
        sizes.remove(int(shoe))
        total += int(cost)
print(total)
