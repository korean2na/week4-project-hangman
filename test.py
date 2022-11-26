from hangman import Hangman
import unittest
from unittest.mock import patch

hangtest = Hangman()

class HangTest(unittest.TestCase):
    
    def test_fill_board(self):
        test_board = {}
        hangtest.fill_board('test', test_board)
        # print(test_board)
        self.assertIsNotNone(test_board)

    def test_init(self):
        hangtest.__init__()
        self.assertIsInstance(hangtest.secret_word, str)
        self.assertIsInstance(hangtest.mistakes_left, int)
        self.assertIs(hangtest.mistakes_left, 7)
        self.assertIsNotNone(hangtest.board)
        self.assertEqual(len(hangtest.board_str), 0)
        self.assertEqual(len(hangtest.guessed), 0)

    def test_update(self):
        hangtest.__init__()
        hangtest.board = {}
        hangtest.guessed = ['t', 'a']
        hangtest.fill_board('test', hangtest.board)
        self.assertEqual(len(hangtest.board), 4)
        self.assertEqual(len(hangtest.guessed), 2)
        hangtest.update()
        self.assertEqual(hangtest.mistakes_left, 6)
        self.assertTrue(hangtest.board[1]['show'])
        self.assertFalse(hangtest.board[2]['show'])
        self.assertFalse(hangtest.board[3]['show'])
        self.assertTrue(hangtest.board[4]['show'])

    def test_show(self):
        hangtest.__init__()
        hangtest.board = {}
        hangtest.guessed = ['t', 'a']
        hangtest.fill_board('test', hangtest.board)
        self.assertEqual(len(hangtest.board), 4)
        self.assertEqual(len(hangtest.guessed), 2)
        hangtest.show_board()
        self.assertEqual(hangtest.mistakes_left, 6)
        self.assertEqual(hangtest.board_str, 't _ _ t ')

    # working case
    @patch('builtins.input', return_value='ta')
    def test_guess_valid(self, input):
        hangtest.__init__()
        hangtest.board = {}
        hangtest.fill_board('test', hangtest.board)
        self.assertEqual(len(hangtest.board), 4)
        hangtest.guess()
        self.assertIn('t', hangtest.guessed)
        self.assertIn('a', hangtest.guessed)
        hangtest.show_board()
        self.assertEqual(hangtest.mistakes_left, 6)
        self.assertEqual(hangtest.board_str, 't _ _ t ')

    # semi-working case that tries 3 guesses at once when there is only 1 guess left
    @patch('builtins.input', return_value='dan')
    def test_guess_semi_valid(self, input):
        hangtest.__init__()
        hangtest.board = {}
        hangtest.guessed = ['x', 'y', 'z', 'q', 'w', 'v']
        hangtest.fill_board('test', hangtest.board)
        self.assertEqual(len(hangtest.board), 4)
        self.assertEqual(len(hangtest.guessed), 6)
        hangtest.guess()
        self.assertEqual(len(hangtest.guessed), 7)

    # invalid case with numbers
    @patch('builtins.input', return_value='80')
    def test_guess_invalid1(self, input):
        hangtest.__init__()
        self.assertEqual(hangtest.guess(), 'Invalid')
        self.assertEqual(len(hangtest.guessed), 0)

    # invalid case with special chars
    @patch('builtins.input', return_value='!@')
    def test_guess_invalid2(self, input):
        hangtest.__init__()
        self.assertEqual(hangtest.guess(), 'Invalid')
        self.assertEqual(len(hangtest.guessed), 0)

    # invalid case with letters, numbers, and special chars
    @patch('builtins.input', return_value='green80!@')
    def test_guess_invalid3(self, input):
        hangtest.__init__()
        self.assertEqual(hangtest.guess(), 'Invalid')
        self.assertEqual(len(hangtest.guessed), 0)

    
unittest.main()