import random

class Hangman():
    # board format
        # {
        #     1:{'letter': 'q', 'show': False},
        #     2:{'letter': 'u', 'show': False},
        #     3:{'letter': 'i', 'show': False},
        #     4:{'letter': 'c', 'show': False},
        #     5:{'letter': 'h', 'show': False},
        #     6:{'letter': 'e', 'show': False},
        # }

    # put this before init because init calls upon this method
    def fill_board(self, astr, board):
        for i in range(len(astr)):
            board[i + 1] = {'letter': astr[i], 'show': False}
        
    def __init__(self):
        self.word_bank = ['tryptophan', 'fugacity', 'quell', 'nuance', 'challah', 'commensurate', 'masticate', 'defenestrate', 'quiche', 'equine']
        self.secret_word = random.choice(self.word_bank)
        self.secret_unique_chars = len(list(set(self.secret_word)))
        self.board = {}
        self.board_str = ''
        self.guessed = []
        self.guessed_correct = []
        self.mistakes_left = 7
        self.fill_board(self.secret_word, self.board)

    # runs a check between guessed and board to update 'show' values on board
    # also updates mistakes_left
    def update(self):
        for i in range(len(self.board)):
            if self.board[i+1]['letter'] in self.guessed:
                self.board[i+1]['show'] = True
                self.guessed_correct.append(self.board[i+1]['letter'])

        self.guessed_correct = list(set(self.guessed_correct))

        self.mistakes_left = 7 + len(self.guessed_correct) - len(self.guessed) 

    # runs update then prints out the board with guessed letters showing and unguessed letters hidden
    def show_board(self):
        self.update()
        self.board_str = ''
        for i in range(len(self.board)):
            if self.board[i+1]['show']:
                self.board_str += f"{self.board[i+1]['letter']} "
            else:
                self.board_str += '_ '
        print(f'\n{self.board_str}')
        print(f"\nGuessed letters:")
        print(self.guessed)
        print(f"\nYou've got {self.mistakes_left} guesses left.")
    
    # abbreviated version of the update method
    def show_board_short(self):
        self.update()
        self.board_str = ''
        for i in range(len(self.board)):
            if self.board[i+1]['show']:
                self.board_str += f"{self.board[i+1]['letter']} "
            else:
                self.board_str += '_ '
        print(f'\n{self.board_str}\n')

    # sequence of having user input a guess/guesses and then processing it for adding to guessed dict
    def guess(self):
        current_guess = input('\nWhat is your guess?\nLetter(s) only. No numbers, special characters, or spaces.\n').lower()
        for n in current_guess:
            if not n.isalpha():
                return print("\nYou've entered something invalid. Please try again.")

        current_guess = list(set(current_guess))

        for n in current_guess:
            if n in self.guessed:
                print(f'\nThe letter "{n}" was already guessed previously.')
            else:
                self.update()
                if self.mistakes_left > 0:
                    print(f'\nGuessing "{n}"...')
                    self.guessed.append(n)

                # will only happen if a guess with multiple incorrect letters is made with only 1 guess left
                # as soon as mistakes_left is 0, driver() will break its loop
                else:
                    print(f'\nOops! Looks like you have used up all your guesses.\nThe letter "{n}" was not guessed.')
                    break
            

def driver():
    hangman.show_board()
    while hangman.mistakes_left > 0:
        if len(hangman.guessed_correct) == hangman.secret_unique_chars:
            break
        
        else:
            hangman.guess()
            hangman.show_board()

    # when victory condition met or mistakes_left goes down to 0
    print('\n')
    print('=~'*40)
    print("\nLet's see how you did...")

    if len(hangman.guessed_correct) == hangman.secret_unique_chars:
            print('\n')
            print('=~'*40)
            hangman.show_board_short()
            print(f'You win! You got the word "{hangman.secret_word}" correctly with {hangman.mistakes_left} guess(es) left.')
            print('=~'*40)
    
    else:
        print('\n')
        print('=~'*40)
        hangman.show_board_short()
        print(f'\nThe secret word was: "{hangman.secret_word}"')
        print(f"\nYou got {len(hangman.guessed_correct)} letters out of {hangman.secret_unique_chars}. Better luck next time!")
        print('=~'*40)
        

hangman = Hangman()
# driver()