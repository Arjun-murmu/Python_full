print("Hello World")
def Palindrom_no(n):
    s = str(n)
    rev = s[::-1]
    revn = int(rev)
    
    if n == revn:
        print(f"Your no {n} is Palindrom_no.")
    else:
        print(f"Your number {n} is not Palindrom_no.")

number = int(input("Enter a number for check : "))
Palindrom_no(number)
