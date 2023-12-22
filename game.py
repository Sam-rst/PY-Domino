from domino import Domino

class Game:
    
    def __init__(self) -> None:
        self.dominos = []
    
    def start(self):
        for i in range(0,7):
            for j in range(0,7):
                d = Domino(i, j)
                self.dominos.append(d)
                print(d)
        return self.dominos