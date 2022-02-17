import random


def play():

    while True:
        user = get_user_input()
        computer = random.choice(['r', 'p', 's'])

        if user == computer:
            print("it's a tie")

        # r > s, s > p, p > r
        if is_win(user, computer):
            print('You won !!!')
            break

        print('You lost :c ')


def get_user_input():
    # gets user inputs and check if it's appropriate
    # recalls itself until an appropriate input is entered
    user_input = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    if user_input != 'r' and user_input != 'p' and user_input != 's':
        print("please choose either r, p or s! ")
        user_input = get_user_input()
    return user_input


def is_win(player, opponent):
    # boolean
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
     or (player == 'p' and opponent == 'r'):
        return True


if __name__ == "__main__":
    play()
