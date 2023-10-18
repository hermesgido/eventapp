first_Number = int(input("Enter First Number: "))
second_Number = int(input("Enter Second Number: "))
action = int(input("Enter 1 to add or 2 to minus: "))
try:
    if action == 1:
        print(f"Thes sum is : {first_Number + second_Number}")
    else:
        print(f"Thes difference  is : {first_Number - second_Number}")
except:
    print("Please Enter COrrect Value")