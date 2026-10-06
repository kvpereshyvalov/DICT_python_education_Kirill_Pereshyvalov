bot_name = "CodeBot"
birth_year = 2026

print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")
user_name = input("Please, remind me your name.\n")
print(f"What a great name you have, {user_name}!")

print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

remainder_three = int(input())
remainder_five = int(input())
remainder_seven = int(input())

user_age = (
    remainder_three * 70
    + remainder_five * 21
    + remainder_seven * 15
) % 105

print(f"Your age is {user_age}; that's a good time to start programming!")


print("Now I will prove to you that I can count to any number you want.")

count_limit = int(input())

for current_number in range(count_limit + 1):
    print(f"{current_number} !")

print("Completed, have a nice day!")

print("Let's test your programming knowledge.")

correct_answer = 2

while True:
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    user_answer = int(input())

    if user_answer == correct_answer:
        break

    print("Please, try again.")

print("Congratulations, have a nice day!")

