class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        if (self.capacity - v) < 0:
            return False
        else:
            return True

    def add(self, v):
        if self.can_add(v):
            self.coins += v
            self.capacity -= v
        else:
            print("Can't add")
