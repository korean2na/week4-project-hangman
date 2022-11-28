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
        self.query_on = False

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
        if self.mistakes_left == 0:
            print('\nOops! Looks like you have used up all your guesses.')
            return 'Out'

        else:
            current_guess = input('\nWhat is your guess?\nLetter(s) only. No numbers, special characters, or spaces.\n').lower()
            for n in current_guess:
                if not n.isalpha():
                    print("\nYou've entered something invalid. Please try again.")
                    return 'Invalid'

            current_guess = list(set(current_guess))

            for n in current_guess:
                if n in self.guessed:
                    print(f'\nThe letter "{n}" was already guessed previously.')
                else:
                    self.update()
                    if self.mistakes_left == 0:
                        print(f'\nOops! Looks like you have used up all your guesses.\nThe letter "{n}" was not guessed.')
                        break

                    else:
                        print(f'\nGuessing "{n}"...')
                        self.guessed.append(n)
                
            
           
def driver():
    options = {
        'yes': ['y', 'yes', 'ye', 'yeah', 'yea', 'yeh', 'ya', 'yah', '(y)es', '(y)', 'play', 'go', 'continue', 'cont', 'more'],
        'no': ['n', 'no', 'nah', 'na', 'nay', '(n)o', '(n)', 'quit', 'stop', 'exit']
    }
    wins = 0
    losses = 0
    two_words_ago = ''
    last_word_used = ''
    
    # overall loop for the game to go back to if the user wants to play another round
    game_running = True
    while game_running:
        # if the secret word is either of the last 2 words used, this loops through randomization until it finds a word that is not the last word used or was used two words ago
        while hangman.secret_word == two_words_ago or hangman.secret_word == last_word_used:
            hangman.secret_word = random.choice(hangman.word_bank)

        # loop shows board then checks to see if win condition is met which will break loop
        # if not met, runs guess method then loops again
        while hangman.mistakes_left > 0:
            hangman.show_board()
            if len(hangman.guessed_correct) == hangman.secret_unique_chars:
                break
            
            else:
                hangman.guess()

        # when victory condition met or mistakes_left goes down to 0
        print('\n')
        print('=~'*40)
        print("\nLet's see how you did...")

        # win
        if len(hangman.guessed_correct) == hangman.secret_unique_chars:
                wins += 1
                print('\n')
                print('=~'*40)
                hangman.show_board_short()
                print(f'\nYou win! You got the word "{hangman.secret_word}" correctly with {hangman.mistakes_left} guess(es) left.')
                print(f'\nYour overall score is: {wins}W - {losses}L\n')
                print('=~'*40)
        
        # loss
        else:
            losses += 1
            print('\n')
            print('=~'*40)
            hangman.show_board_short()
            print(f'\nThe secret word was: "{hangman.secret_word}"')
            print(f"\nYou got {len(hangman.guessed_correct)} letters out of {hangman.secret_unique_chars}. Better luck next time!")
            print(f'\nYour overall score is: {wins}W - {losses}L\n')
            print('=~'*40)

        # asking the user if they want to play another round or not
        hangman.query_on = True
        while hangman.query_on:
            reset_query = input('\nWould you like to play again?\n(Y)es | (N)o\n').lower()
            if reset_query in options['yes']:
                # update both previous words
                two_words_ago = ''+last_word_used
                last_word_used = ''+hangman.secret_word
                print('\n')
                print('=~'*40)
                hangman.__init__()

            elif reset_query in options['no']:
                print('\n')
                print('=~'*40)
                print(f'\nYour final overall score is: {wins}W - {losses}L\nThanks for playing!\n')
                print('=~'*40)
                game_running = False
                hangman.query_on = False

            else:
                print(f'\n"{reset_query}" is an invalid response. Please try again.')
        

hangman = Hangman()
# driver()