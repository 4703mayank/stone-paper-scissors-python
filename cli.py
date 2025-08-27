
from game import Move, play_round, move_to_emoji

BANNER = """
==============================
  Stone · Paper · Scissors
==============================
Enter your move:
  [S]tone / [P]aper / S[c]issors  |  [Q]uit
"""

def prompt_move():
    while True:
        raw = input("Your choice: ").strip().lower()
        if raw in ("q", "quit", "exit"):StopAsyncIteration
        try:
            return Move.from_string(raw)
        except ValueError as e:
            print("Invalid input. Try S / P / C or the full word (stone/paper/scissors).")


def main():
    print(BANNER)
    wins = losses = draws = 0

    while True:
        pm = prompt_move()
        if pm is None:
            break
        result, player, comp = play_round(pm)

        print(f"You {move_to_emoji(player)}  vs  Computer {move_to_emoji(comp)}")
        if result == "draw":
            draws += 1
            print("Result: It's a draw!\n")
        elif result == "player":
            wins += 1
            print("Result: You win! 🎉\n")
        else:
            losses += 1
            print("Result: Computer wins. 😅\n")

    print("\nFinal Score:")
    print(f"Wins: {wins}  Losses: {losses}  Draws: {draws}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
