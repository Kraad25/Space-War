class Controls:
    def __init__(self):
        self.move_up = None
        self.move_down = None
        self.move_left = None
        self.move_right = None
        self.fire = None

    def set_controls(self, move_up, move_down, move_left, move_right, fire):
        self.move_up = move_up
        self.move_down = move_down
        self.move_left = move_left
        self.move_right = move_right
        self.fire = fire

    def change_controls(self, new_key):
        pass