import random
import time
import itertools

def generate_pass(length=6):
    """Function to generate a password"""

    char_set = {'small': 'abcdefghijklmnopqrstuvwxyz',
                'nums': '0123456789',
                'big': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                'special': '^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
                }
    password = []

    while len(password) < length:
        key = random.choice(['small', 'nums', 'big', 'special'])
        a_char = random.choice(char_set[key])
        if check_prev_char(password, char_set[key]):
            continue
        else:
            password.append(a_char)
    return ''.join(password)


def check_prev_char(password, current_char_set):
    """Function to ensure that there are no consecutive 
    UPPERCASE/lowercase/numbers/special-characters."""

    index = len(password)
    if index == 0:
        return False
    else:
        prev_char = password[index - 1]
        if prev_char in current_char_set:
            return True
        else:
            return False

def decryptpassword(password):
    # Decrypt the password
    chars = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ^!\$%&/()=?{[]}+~#-_.:,;<>|\\"
    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                return 'password is {}. found in {} guesses.'.format(guess, attempts)

if __name__ == '__main__':
    password = generate_pass(6)
    print('Generated password: ' + password)
    start_time = time.time()
    decryptpassword(password)
    print((time.time() - start_time) / 60, "minutes")
