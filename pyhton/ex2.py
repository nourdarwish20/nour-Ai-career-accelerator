num = int(input("Enter a number: "))
check=int(input("Enter other number:"))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
    
if num % check == 0:
    print(f"{check} divides evenly into {num}")
else:
    print(f"{check} does NOT divide evenly into {num}")