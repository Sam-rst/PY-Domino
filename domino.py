class Domino:
    
    def __init__(self, left=0, right=0) -> None:
        self.left = left
        self.right = right
        
    def __str__(self):
        left_str = " "
        right_str = " "
        if self.left != 0:
            left_str = self.left
        if self.right != 0:
            right_str = self.right

        if self.isDouble():
            return f"[{left_str}|{right_str}] => DOUBLE !"
        else:
            return f"[{left_str}|{right_str}]"
        
    def __eq__(self, domino):
        return self.left == domino.left and self.right == domino.left
    
    def __gt__(self, domino):
        return self.value() > domino.value()
    
    def __lt__(self, domino):
        return self.value() < domino.value()
    
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, value):
        try:
            if value < 0 or value > 6:
                raise ValueError("This domino is not valid : must be between 0 and 6 include")
            self.__left = value
        except ValueError as e:
            print(e)
            
    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, value):
        try:
            if value < 0 or value > 6:
                raise ValueError("This domino is not valid : must be between 0 and 6 include")
            self.__right = value
        except ValueError as e:
            print(e)
    
    def isDouble(self):
        return self.left == self.right
    
    def set(self, left, right):
        self.left = left
        self.right = right

    def value(self):
        return self.left + self.right
    
    def reverse(self):
        self.right, self.left = self.left, self.right
        
    def isEqual(self, domino):
        return self == domino