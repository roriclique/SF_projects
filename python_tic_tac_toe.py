from random import randint

vertical_coordinats = ('0', '1', '2')
empty_space = '_'


def get_user_char():
    user_char = input("Choose a warrior |x, 0|: ").lower().strip(' ')
    while user_char not in ('x', '0'):
        print("Not available. Let's try again.")
        user_char = input("Yeah. Select one of these symbols --> |x, 0|: ").lower().strip(' ')
    return user_char


def show_field(field):
    print(' ', '0', '1', '2')
    for y, value in enumerate(vertical_coordinats):
        print(value, ' '.join(field[y]))


def draw_(field):
    count = 0
    for y in range(3):
        count += 1 if empty_space in field[y] else 0
    return count == 0


def user_turn(field):
    true_x, true_y = 0, 0
    while True:
        coordinats = input("And input coordinats...?:").lower().strip(' ')
        y, x = tuple(coordinats)

        if int(x) not in (0, 1 , 2) or y not in vertical_coordinats:
            print("Cmon, are you sure?")
            continue

        true_x, true_y = int(x), vertical_coordinats.index(y)
        if field[true_y][true_x] == empty_space:
            break
        else:
            print("These coordinates are already taken!")

    return true_x, true_y


def get_ai_char(char):
    return '0' if char == 'x' else 'x'


def win_(char, field):
    ai_char = get_ai_char(char)
    for y in range(3):
        if ai_char not in field[y] and empty_space not in field[y]:
            return True

    for x in range(3):
        col = [field[0][x], field[1][x], field[2][x]]
        if ai_char not in col and empty_space not in col:
            return True

    first_diagonal = [field[0][0], field[1][1], field[2][2]]
    if ai_char not in first_diagonal and empty_space not in first_diagonal:
        return True
    second_diagonal = [field[0][2], field[1][1], field[2][0]]
    if ai_char not in second_diagonal and empty_space not in second_diagonal:
        return True

    return False


def ai_turn(field):
    y, x = randint(0, 2), randint(0, 2)
    while field[y][x] != empty_space:
        y, x = randint(0, 2), randint(0, 2)
    return y, x


field = [
    [empty_space for x in range(3)] for y in range(3)
]

user_char = get_user_char()
ai_char = get_ai_char(user_char)


while True:
    show_field(field)
    if draw_(field):
        print("Not a looser, but not a winner. So next time.")
        break

    x, y = user_turn(field)
    field[y][x] = user_char
    if win_(user_char, field):
        print("Damn, you've just won...Congrats!")
        break

    x, y = ai_turn(field)
    field[y][x] = ai_char
    if win_(ai_char, field):
        print("You're lost. Try again?")
        break

show_field(field)