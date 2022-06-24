class animation:
    # Need comments
    def __init__(self):
        # define variables to be used throughout the program

        self.parachute_line = ""
        self.parachute = []

    def create_parachute_line(self):
        # create the parachute line
        
        self.parachute = [
            "  ___  ",
            " /___\ ",
            " \   / ",
            "  \ /  ",
            "   O   ",
            "  /|\  ",
            "  / \  ",
            "       ",
            "^^^^^^^"
        ]
        print()

        return self.parachute

    def print_parachute_line(self, parachute):
        # print the parachute line
        
        for i in range(0, len(parachute)):
            print(parachute[i], flush=True)

        return parachute
