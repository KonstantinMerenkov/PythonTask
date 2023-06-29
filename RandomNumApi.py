import random


class RandomNumApi:

    def __init__(self, name):
        self.name = name

    def starting(self):
        print(f'Hello fellow {self.name}')

    @staticmethod
    def num_randomizer():
        return random.randint(1, 100)

    @staticmethod
    def verify_number(number):
        if not isinstance(number, int) and not 1 <= number <= 100:
            raise ValueError('Wrong type of number, try again')
        else:
            return number


def guess():
    nb = RandomNumApi(input('Whats your name\n'))
    nb.starting()
    while True:
        print('Put your number')
        n = int(input())
        if n < nb.num_randomizer():
            print('Too small')
        elif n > nb.num_randomizer():
            print('Too big')
        else:
            print('Bulls eye')
            break


guess()
