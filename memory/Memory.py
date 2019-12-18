class Memory:

    doMemory = None
    undoMemory = None

    def __init__(self):
        self.doMemory = []
        self.undoMemory = []