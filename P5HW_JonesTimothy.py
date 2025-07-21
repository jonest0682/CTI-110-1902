# Timothy Jones
# 7/18/2025
# P5HW 
# Math Battle Game - This is a turn-based math game where the player competes
# with a bot by answering math problems.

#start
import random

# Function to create player profile
def get_player():
    name = input("Enter your name to begin the battle: ")
    print(f"Welcome, {name}! Let the Math Battle begin!\n")
    return {"name": name, "score": 0}

# Function to generate a math question and return result
def ask_math_question():
    operators = ['+', '-', '*', '/']
    op = random.choice(operators)
    a = random.randint(1, 12)
    b = random.randint(1, 12)
    
    if op == '+':
        answer = a + b
    elif op == '-':
        answer = a - b
    elif op == '*':
        answer = a * b
    elif op == '/':
        # Ensure division is clean
        a = a * b
        answer = a / b
    
    return f"{a} {op} {b}", round(answer, 2)

# Function to simulate bot's answer (random accuracy)
def bot_answer(correct_answer):
    chance = random.randint(1, 100)
    if chance <= 70:
        return round(correct_answer, 2)  # bot answers correctly 70% of the time
    else:
        return round(correct_answer + random.randint(1, 5), 2)  # wrong answer

# Main gameplay logic
def play_game(player):
    bot_score = 0
    player_score = 0

    for round_num in range(1, 11):
        print(f"\n Round {round_num} ")

        # Player's turn
        q1, a1 = ask_math_question()
        try:
            user_input = float(input(f"{player['name']}, solve: {q1} = "))
        except ValueError:
            print("Invalid input. Counted as incorrect.")
            user_input = None

        if user_input == a1:
            player_score += 1
            print(" Correct!")
        else:
            print(f" Incorrect! The right answer was {a1}")

        # Bot's turn
        q2, a2 = ask_math_question()
        bot_response = bot_answer(a2)
        print(f" Bot solving: {q2} = {bot_response}")
        if bot_response == a2:
            bot_score += 1
            print(" Bot got it right!")
        else:
            print(f" Bot failed! Correct was {a2}")

        print(f"Score - {player['name']}: {player_score}, Bot: {bot_score}")

        if player_score == 5 or bot_score == 5:
            break

    print("\n Final Result ")
    if player_score > bot_score:
        print(f" {player['name']} wins! Brain power triumphs!")
    elif bot_score > player_score:
        print(" Bot wins! Better luck next time.")
    else:
        print(" It's a tie!")

# Main function to start the game
def main():
    player = get_player()
    play_game(player)

# Run the game
main()

#end
