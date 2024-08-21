#Loop pratice 1
for i in range(5):
    print(i)
#loop Pratice 2
friends = ["RAJU","JITU","SONU","MAMA"]
for friend in friends:
    print("Hello " + friend)

#Loop pratice 3
num = [3,2,5,4]
sum = 0
length = 0
for value in num:
    sum += value
    length += 1
print("Sum = ",sum)
print("Total Sum : " + str(sum) + "\nAvarage : " + str(sum/length)) 
#Loop pratice 4
product = 1
for n in range(1,10):
    product = product * n
print(product)

#Loop pratice 5
def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,5):
    print(x,to_celsius(x))
 #loop pratice 6
for n in range(4+1):
    print(n)
#loop partice 7
for n in range(2,10):
    print(n)
#loop pratice 8
for n in range(2,10+2):
    print(n)
#loop pratice 9
for n in range(2,10,2):
    print(n)
#loop pratice 10
for n in range(4,15+1,2):
    print(n)
#loop pratice 11
for m in range(2*2,25,3+2):
    print(m)
#loop pratice 12
for o in range(10,0,-2):
    print(o)
#loop pratice 13
for t in range(1,10+1):
    print("3 * ",t," = ", t*3)
#OUTPUT
# 3 *  1  =  3
# 3 *  2  =  6
# 3 *  3  =  9
# 3 *  4  =  12
# 3 *  5  =  15
# 3 *  6  =  18
# 3 *  7  =  21
# 3 *  8  =  24
# 3 *  9  =  27
#3 *  10  =  30
#loop pratice 14
for nu in range(2,-2,-1):
    print(nu)
