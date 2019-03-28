import unittest
from move import Move
from board import Board


class TestMove(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.move = Move(self.board.board_ids, self.board.piece_start_id)

    def test_calculate_move_from_characters_to_id(self):
        user_characters = {"MRMLMRM": "22", "RMMM": "03", "LMMM": "00", "MMLMMM": "20", "MMRMMMLMLMLMLMLM":"33",
                           "MMRMMMRMRMRMRMRM":"13", "MMRMMMMMMMMMMMMMM":"24", "RRMMMM":"00", "RMMMMMMMM":"04", "RRRRRRRRRRLLLLLLLLLLLLL":"00"}

        for characters, result in user_characters.items():
            self.move.set_user_characters(characters)
            self.move.calculate_move_from_characters_to_id()
            self.assertEqual(result, self.move.get_piece_id())
            self.move.__init__(self.board.board_ids, self.board.piece_start_id)

    def test_output_format(self):
        user_characters = {"MRMLMRM": "2 2 E", "RMMM": "0 3 E", "LMMM": "0 0 W", "MMLMMM": "2 0 W", "MMRMMMLMLMLMLMLM": "3 3 N",
                           "MMRMMMRMRMRMRMRM": "1 3 S", "MMRMMMMMMMMMMMMMM": "2 4 E", "RRMMMM": "0 0 S", "RMMMMMMMM": "0 4 E"}

        for characters, result in user_characters.items():
            self.move.set_user_characters(characters)
            self.move.calculate_move_from_characters_to_id()
            self.assertEqual(result, self.move.get_piece_id_in_output_format())
            self.move.__init__(self.board.board_ids, self.board.piece_start_id)


if __name__ == "__main__":
    unittest.main()