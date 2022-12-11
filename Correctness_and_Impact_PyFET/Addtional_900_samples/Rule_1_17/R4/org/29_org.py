n=num
setData=set()		#set datastructure for checking a number is repeated or not.
while 1:
	if n==1:
		print("{} is a happy number after apply way 2".format(num))
        if n in setData:
            print("{} is Not a happy number after apply way 2".format(num))
            break

setData.add(n)	#adding into set if not inside set
n=int(''.join(str(sum([int(i)**2 for i in str(n)]))))       #Pythonic way
