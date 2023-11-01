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

    def change_controls(self, control_type, new_key):
        if control_type == 'move_up':
            self.move_up = new_key
        elif control_type == 'move_down':
            self.move_down = new_key
        elif control_type == 'move_left':
            self.move_left = new_key
        elif control_type == 'move_right':
            self.move_right = new_key
        elif control_type == 'fire':
            self.fire = new_key