#account proof 1212488-20201206-47944ac0

# stars

with open("C:/Users/Cooper/Downloads/input.txt",'r') as file:
    expenses = file.readlines()
    cleandata = []
    for line in expenses:
        cleandata.append(line.strip('\n'))
    for expense in cleandata:
        for expense2 in cleandata:
            test = int(expense2) + int(expense)
            if test == 2020:
                solution1 = (f"{expense} + {expense2} = 2020\nAnswer:"+ str(int(expense2) * int(expense)))
            for expense3 in cleandata:
                test = int(expense2) + int(expense) + int(expense3)
                if test == 2020:
                    solution2 = (f"{expense} + {expense2} + {expense3} = 2020\nAnswer:"+ str(int(expense2) * int(expense) * int(expense3)))



print('Problem 1:', solution1)
print('Problem 2:', solution2)