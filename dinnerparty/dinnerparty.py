
number_of_friends = int(input("Enter the number of friends joining (including you):\n"))

if number_of_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")

    friends = {}

    for friend_number in range(number_of_friends):
        friend_name = input()
        friends[friend_name] = 0

    print(friends)
