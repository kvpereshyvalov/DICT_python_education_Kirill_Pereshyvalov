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
