import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your choice (Rock, Paper, Scissor): ")
computer_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {computer_choice}")

if user_choice == computer_choice:
    print("Both user and computer have the same choice. It's a tie!")

elif (user_choice == "Rock" and computer_choice == "Scissor") or \
    (user_choice == "Paper" and computer_choice == "Rock") or \
    (user_choice == "Scissor" and computer_choice == "Paper"):
    print("You wins!")
else:    print("Computer wins!")
