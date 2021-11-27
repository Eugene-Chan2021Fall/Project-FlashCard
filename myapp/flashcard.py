class FlashcardSet:
    def __init__(self, name):
        self.name = name
        self.set = []

    def add (self, front, back):
        self.set[front] = back

    def remove (self, front):
        del self.set[front]
