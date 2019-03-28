class Move():

    def __init__(self, board_ids, piece_start_id):
        self.board_ids = board_ids
        self.piece_id = piece_start_id
        self.user_characters = ""
        self.degree_direction = 360
        self.previous_degree = self.degree_direction
        self.forward_character = "M"
        self.rotate_characters = {"R": 90, "L": -90}
        self.degree_properties = {"360": {"value": 10, "direction": "N"}, "90": {"value": 1, "direction": "E"},
                                  "180": {"value": -10, "direction": "S"}, "270": {"value": -1, "direction": "W"}}

    def set_user_characters(self, characters):
        self.user_characters = characters

    def check_correctness_of_the_id(self, piece_id):
        if isinstance(piece_id, int) and piece_id < 10:
            piece_id = "0{}".format(piece_id)

        status = False
        for row_ids in self.board_ids:
            if str(piece_id) in row_ids:
                status = True
                break
        return status

    def calculate_degree_direction(self, degree):
        degree_direction = self.degree_direction + degree
        if degree_direction > 360:
            return (degree_direction - 360)
        elif degree_direction < 0:
            return abs(degree_direction)
        elif degree_direction == 0:
            return 360
        else:
            return degree_direction

    def calculate_move_from_characters_to_id(self):
        place_id = 0

        for user_character in self.user_characters:

            if user_character != self.forward_character:
                character_degree = self.rotate_characters.get(user_character)
                self.degree_direction = self.calculate_degree_direction(character_degree)
            else:
                place_id = place_id + self.degree_properties.get(str(self.degree_direction)).get("value")

            if not self.check_correctness_of_the_id(place_id):
                break

            self.previous_degree = self.degree_direction
            self.piece_id = place_id
            if isinstance(self.piece_id, int) and self.piece_id < 10:
                self.piece_id = "0{}".format(self.piece_id)

    def get_piece_id(self):
        return str(self.piece_id)

    def get_piece_id_in_output_format(self, piece_id=None):
        if not piece_id:
            piece_id = self.get_piece_id()
        return "{} {} {}".format(piece_id[0], piece_id[1], self.degree_properties.get(str(self.previous_degree)).get("direction"))