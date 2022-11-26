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
        self.assertIsInstance(hangtest.secret_word, str)
        self.assertIsInstance(hangtest.mistakes_left, int)
        self.assertIs(hangtest.mistakes_left, 7)
        self.assertIsNotNone(hangtest.board)
        self.assertEqual(len(hangtest.board_str), 0)
        self.assertEqual(len(hangtest.guessed), 0)

    def test_update(self):
        hangtest.board = {}
        hangtest.fill_board('test', hangtest.board)
        self.assertEqual(len(hangtest.board), 4)
        hangtest.guessed = ['t', 'a']
        self.assertEqual(len(hangtest.guessed), 2)
        hangtest.update()
        self.assertEqual(hangtest.mistakes_left, 6)
        self.assertTrue(hangtest.board[1]['show'])
        self.assertFalse(hangtest.board[2]['show'])
        self.assertFalse(hangtest.board[3]['show'])
        self.assertTrue(hangtest.board[4]['show'])

    def test_show(self):
        hangtest.board = {}
        hangtest.fill_board('test', hangtest.board)
        self.assertEqual(len(hangtest.board), 4)
        hangtest.guessed = ['t', 'a']
        self.assertEqual(len(hangtest.guessed), 2)
        hangtest.show_board()
        self.assertEqual(hangtest.mistakes_left, 6)
        self.assertEqual(hangtest.board_str, 't _ _ t ')

    # last test to get working, need to figure out how patch works
    # @patch('builtins.input', return_value='green80')
    # def test_guess_invalid1(self, mock_input):
    #     result = hangtest.guess()
    #     self.assertEqual(result, "\nYou've entered something invalid. Please try again.")

    
unittest.main()