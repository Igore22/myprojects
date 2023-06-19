from logic import check_win, calculate_payout
from settings import get_starting_money

def play_game():
    starting_money = get_starting_money()
    current_money = starting_money
    slots = list(range(1, 31))
    continue_playing = True

    while continue_playing:
        print(f"Current money: ${current_money}")
        slot = int(input("Choose a slot to bet on (1-30): "))
        bet_amount = float(input("Place your bet amount: "))

        winning_slot = check_win(slots)
        if slot == winning_slot:
            payout = calculate_payout(bet_amount)
            current_money += payout
            print(f"You won ${payout}!")
        else:
            current_money -= bet_amount
            print("You lost!")

        print(f"Current money: ${current_money}")
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() != "yes":
            continue_playing = False

    print("Game Over")
    if current_money > starting_money:
        print("Congratulations! You are a winner!")
    elif current_money < starting_money:
        print("Better luck next time!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    play_game()