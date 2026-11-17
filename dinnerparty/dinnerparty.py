
import random

number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")

    friends = {}

    for friend_number in range(number_of_friends):
        friend_name = input()
        friends[friend_name] = 0

    total_amount = float(input("Enter the total amount:\n"))

    amount_per_person = round(total_amount / number_of_friends, 2)

    for friend_name in friends:
        friends[friend_name] = amount_per_person

    lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky_feature == "Yes":
        lucky_friend = random.choice(list(friends.keys()))
        print(f"{lucky_friend} is the lucky one!")

        amount_per_person = round(total_amount / (number_of_friends - 1), 2)

        for friend_name in friends:
            friends[friend_name] = amount_per_person

        friends[lucky_friend] = 0
    else:
        print("No one is going to be lucky")

    print(friends)
