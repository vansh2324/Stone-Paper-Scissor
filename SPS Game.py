import random

name = input("Please enter your good name here 👉🏻 : ")
print(f"\nWe welcome you {name} in this game 🙇🏻‍♂️.\nLet us enjoy this stone 🪨 paper 📜 scissor ✂ game.\n")

# Function to get user input
def user_input():
    user = input("Enter your choice (stone, paper, scissor): ").lower()
    while user not in ["stone", "paper", "scissor"]:
        print("❌ Invalid choice! Please choose from: stone, paper, scissor")
        user = input("Enter your choice again: ").lower()
    return user

# Function to get computer choice
def com_choice():
    return random.choice(["stone", "paper", "scissor"])

# Function to determine winner
def get_result(user_choice, comp_choice):
    print(f"🧠 Computer chose: {comp_choice} ", end='')
    emojis = {"stone": "🪨", "paper": "📜", "scissor": "✂"}
    print(emojis[comp_choice])  # Add emoji display
    
    if user_choice == comp_choice:
        print("😄 It's a draw! You have the same IQ as the computer.")
    elif (user_choice == "stone" and comp_choice == "scissor") or \
         (user_choice == "scissor" and comp_choice == "paper") or \
         (user_choice == "paper" and comp_choice == "stone"):
        print("🎉 You are the winner 🥂!")
    else:
        print("👾 Oops, Computer wins!")

# Main game loop
ch = "yes"
while ch.lower() == "yes":
    u = user_input()
    c = com_choice()
    get_result(u, c)
    ch = input("\nDo you want to play again (yes/no): ")

print("\n🙏 Thank you for playing with us 🫶🏻.")
