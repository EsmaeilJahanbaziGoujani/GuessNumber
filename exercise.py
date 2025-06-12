# Positive, Negative, or Zero
num = int(input("Enter a number: "))
if num < 0:
    print("This number is negative:", num)
elif num > 0:
    print("This number is positive:", num)
else:
    print("This number is zero")

# Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("This number is Even:", num)
else:
    print("This number is Odd:", num)

# Password Check
password = input("Enter the password: ")
if password == "python123":
    print("Access granted.")
else:
    print("Incorrect password.")

# Password Check with while
password = input("Enter the password: ")
count = 3
while count < 3:
    if password == "python123":
        print("Access granted.")
        break
else:
    print("Enter the correct password!!!")

# Password Check with while
correct_password = "python123"
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    password = input("Enter the password: ")
    if password == correct_password:
        print("The password is correct...")
        break
    else:
        attempts += 1
        print("Chances to enter the correct password", max_attempts - attempts)

if attempts == max_attempts:
    print("🚫 Too many failed attempts. Access denied.")

# Count with for loop
for i in range(1, 6):
    print("Number:", i)

# Count with while loop
count = 1
while count <= 5:
    print("Step", count)
    count += 1

# Combines Condition
age = int(input("Enter your age: "))
if age >= 18 and age <= 60:
    print("You are eligible to register.")
else:
    print("Your age is not in the allowed range.")





