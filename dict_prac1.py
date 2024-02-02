scl = dict()
i = 1
flag = 0
n = int(input('Enter number of entries:'))
while i <= n:
    adm = input('\nEnter admission no of stud:')
    nm = input('Enter name of student:')
    sec = input('Enter class and section:')
    per = float(input('Enter the percentage of student:'))
    b = (adm,nm,sec,per)
    scl[adm] = b

    i = i+1

l = scl.keys()

for i in l:
    print("\nAdmin- ", i,":")
    z = scl[i]
    print("admin\t1","name\t", "class\t", "per\t")
    for j in z:
        print(j, end='\t')
