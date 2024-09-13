def square(start,end):
  return [n*n for n in range(start,end+1)]

print(square(2,10))
# output : [4, 9, 16, 25, 36, 49, 64, 81, 100]
a = int(input("Enter first number : "))
b = int(input("Enter second number: "))
print(square(a,b))
