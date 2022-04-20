from random import randint


class Game:

    def __init__(self):
        self.game_list()
        print('Your choice (rock paper scissors lizard spock)?')
        self.player_input = input('Input: ')
        self.__computer = self.game_list()[randint(0, 4)]
        print('Player:', self.player_validate())
        print('Computer:', self.__computer)
        print(self.__result())
        self.__continue()

    def __result(self):
        choices = {
            'rock': ["scissors", "lizard"],
            'paper': ["rock", "spock"],
            'scissors': ["paper", "lizard"],
            'lizard': ["spock ", "paper"],
            'spock': ["scissors", "rock"],
        }
        if self.player_validate() == self.__computer:
            print("It's a TIE!")
        elif self.__computer in choices[self.player_validate()]:
            print('Player WIN!')
        else:
            print('Computer WIN')

    def player_validate(self):
        while True:
            try:
                self.game_list().index(self.player_input.lower())
                return self.player_input
            except ValueError:
                print(f'Invalid input "{self.player_input}"')
                print('Your choice (rock paper scissors lizard spock)?')
                self.player_input = input('Input: ')

    def game_list(self) -> list[str]:
        with open('game_list.txt', 'r', encoding='utf8') as f:
            reader = f.read().split(', ')
            return reader

    def __continue(self):
        while True:
            print('Repeat (Y/N)?')
            self.continue_input = input('Input: ')
            if self.continue_input.upper() == 'Y':
                return self.__init__()
            elif self.continue_input.upper() == 'N':
                print('ty for game :)')
                break
            else:
                print(f'Invalid input "{self.continue_input}"')


if __name__ in '__main__':
    game = Game()