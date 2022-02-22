import random


def play():
    while True:
        user = input("choose wisely, 'r' for rock, 'p' for paper, 's' for scissors.\n")
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print("it's a tie")

        # r > s, s > p, p > r
        if is_win(user, computer):
            return 'You won !!!'
            break

        print('You lost :c ')


def is_win(player, opponent):
    # boolean
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
     or (player == 'p' and opponent == 'r'):
        return True


if __name__ == "__main__":
    play()
