class labyrinth:
    labmap = []
    def __init__(filename):
        with open(filename) as f:
            content = f.readlines()

