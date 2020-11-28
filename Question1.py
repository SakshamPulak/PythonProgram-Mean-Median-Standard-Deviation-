import math
number=int(input("Enter Number of elements : "))
lst=[]
for loop in range(0,number):
    print ("Enter ",end = ' ')
    print (loop+1,end = ' ')
    element=int(input(" Element : "))
    lst.append(element)
length=len(lst)
ch='y'
while (ch=='y'):
    print ("\n1. Mean")
    print ("2. Mode")
    print ("3. Standard Deviation")
    option=int(input("Enter your choice : "))
    sumofterms=0
    if option==1:
        for value in lst:
            sumofterms+=value
        mean=(sumofterms/length)
        print ("\nMean of given data is : ",mean)
        break
    if option==2:
        maxValue = 0
        maxCount = 0
        for i in range (0,number):
            count = 0;
            for j in range (0,number):
                if (lst[j] == lst[i]):
                    count+=1
            if (count > maxCount):
                maxCount = count
                maxValue = lst[i]
        print ("\nMode of given data is : ",maxValue)
        break
    if option==3:
        sumofterms=0
        standarddeviation=0
        for value in lst:
            sumofterms+=value
        mean=(sumofterms/length)
        for i in range (0,number):
            standarddeviation+=pow(lst[i]-mean,2)
        print ("\nStandard deviation of given data is : ",(math.sqrt(standarddeviation/10)))
        break
    else:
        print ("Invalid choice")
        ch=input("want to continue (y/n) : ")
        if ch=='y':
            continue
        else:
            break

