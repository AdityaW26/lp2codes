'''n = int(input("Enter number of numbers - "))
nums = []
for i in range(n):
    t = int(input("value - "))
    nums.append(t)

print("Before sorting - ",nums)
for j in range(n):
    min_index = j
    for k in range(j+1,n):
        if nums[k]<nums[min_index]:
            min_index = k

    nums[j], nums[min_index] = nums[min_index], nums[j]

print("After sorting - ", nums)'''

Jobs = []
Solution = []
Profits = []
Deadlines = []
max_profit = 0

n = int(input("Enter number of jobs - "))
for i in range(n):
    Jobs.append("J"+str(i+1))
    Deadlines.append(int(input("Enter deadline for " + Jobs[i] + " - ")))
    Profits.append(int(input("Enter profit for " + Jobs[i] + " - ")))

# sort profits in desc order
for i in range(n):
    for j in range(i+1,n):
        if Profits[j]>Profits[i] :
            Profits[j], Profits[i] = Profits[i], Profits[j]
            Deadlines[j], Deadlines[i] = Deadlines[i], Deadlines[j]
            Jobs[j], Jobs[i] = Jobs[i], Jobs[j]


# traverse through deadline
status = [False]*n
for i in range(n):
    deadline = Deadlines[i]
    if status[deadline] is False:
        status[deadline] = True
        max_profit += Profits[i]
        Solution.append(Jobs[i])

print("Max profit - ", max_profit)
print('Schedule - ', Solution)

'''
Enter number of jobs - 4
Enter deadline for J1 - 1
Enter profit for J1 - 10
Enter deadline for J2 - 2
Enter profit for J2 - 100
Enter deadline for J3 - 1
Enter profit for J3 - 27
Enter deadline for J4 - 2
Enter profit for J4 - 11
Max profit -  127
Schedule -  ['J2', 'J3']

Process finished with exit code 0

'''