from board import Board
from move import Move


def get_user_characters():
    user_input = input("Provide movement characters: ")
    return user_input


def main():
    board = Board()
    move = Move(board.board_ids, board.piece_start_id)

    print("\nWelcome in MovingPiece game!")
    print("Move your piece along the board by providing movement characters:")
    print("M - move forward, R - rotate right by 90 degrees, L - rotate left by 90 degrees")
    print("")

    board.pretty_print_board()
    print("")
    print("Current position: {}".format(move.get_piece_id_in_output_format()))

    user_characters = get_user_characters()
    move.set_user_characters(user_characters)

    move.calculate_move_from_characters_to_id()
    move_id = move.get_piece_id()

    board.set_piece_id(move_id)
    board.set_piece_on_board()

    print("")
    board.pretty_print_board()
    print("")
    print("Current position: {}".format(move.get_piece_id_in_output_format(move_id)))


if __name__ == "__main__":
    main()