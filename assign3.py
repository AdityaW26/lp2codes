# Greedy algorithm - selection sort
n = int(input("Enter number of array elements - "))
l = []
for i in range(n):
    l.append(int(input("Enter element - ")))

print("List before sorting - ")
print(l)
print()

for j in range(n):
    min_index = j
    for k in range(j+1,n):
        if l[k]<l[min_index] :
            min_index = k

    l[j], l[min_index] = l[min_index], l[j]
    print("After iteration "+ str(j+1) + " list - ")
    print(l)


n = int(input("Enter number of jobs - "))
Jobs = []
Solution = []
Deadlines = []
Profits = []
totalProfit = 0
for i in range(0,n):
    print("JOB "+str(i+1))
    Jobs.append("J"+str(i+1))
    Deadlines.append(int(input("Enter deadline - ")))
    Profits.append(int(input("Enter profit - ")))

# sort profits in descending order
for j in range(0,n):
    for k in range(j+1, n):
        if Profits[k]>Profits[j] :
            # swap values
            Profits[k], Profits[j] = Profits[j], Profits[k]
            # swap other lists too to maintain original relation between indices
            Jobs[k], Jobs[j] = Jobs[j], Jobs[k]
            Deadlines[k], Deadlines[j] = Deadlines[j], Deadlines[k]

# traverse through deadline
status = [False]*n  # to check if slot is free or not
for i in range(0,n):
    deadline = Deadlines[i]
    if status[deadline] is False:   # free slot
        status[deadline] = True
        Solution.append(Jobs[i])
        totalProfit+=Profits[i]

print("Sequence of jobs - ")
print(Solution)
print("Total profit - " + str(totalProfit))

'''

OUTPUT OF SELECTION SORT

/usr/bin/python3 /home/tecomp/PycharmProjects/N2/assign3.py
Enter number of array elements - 7
Enter element - 22
Enter element - 12
Enter element - 9
Enter element - 36
Enter element - 11
Enter element - 28
Enter element - 15
List before sorting - 
[22, 12, 9, 36, 11, 28, 15]

After iteration 1 list - 
[9, 12, 22, 36, 11, 28, 15]
After iteration 2 list - 
[9, 11, 22, 36, 12, 28, 15]
After iteration 3 list - 
[9, 11, 12, 36, 22, 28, 15]
After iteration 4 list - 
[9, 11, 12, 15, 22, 28, 36]
After iteration 5 list - 
[9, 11, 12, 15, 22, 28, 36]
After iteration 6 list - 
[9, 11, 12, 15, 22, 28, 36]
After iteration 7 list - 
[9, 11, 12, 15, 22, 28, 36]

Process finished with exit code 0

__________________________________________________________________________________________________

OUTPUT OF JOB SCHEDULING ALGORITHM

/usr/bin/python3 /home/tecomp/PycharmProjects/N2/assign3.py
Enter number of jobs - 4
JOB 1
Enter deadline - 2
Enter profit - 100
JOB 2
Enter deadline - 1
Enter profit - 10
JOB 3
Enter deadline - 2
Enter profit - 15
JOB 4
Enter deadline - 1
Enter profit - 27
Sequence of jobs - 
['J1', 'J4']
Total profit - 127

Process finished with exit code 0


'''