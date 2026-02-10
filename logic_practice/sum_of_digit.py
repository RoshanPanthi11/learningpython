num=int(input("enter a number"))
total=0
temp=num

while temp > 0:
     digit = temp % 10
     total += digit 
     temp//=10

print(f"sum of digit of {num} is {total}")


#alternative
num = input("Enter a number: ")
print("Sum of digits:", sum(int(digit) for digit in num))
     