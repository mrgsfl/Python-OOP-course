class Buffer:
    def __init__(self):
        self.current = []

    def add(self, *a):
        self.current += a
        while len(self.current) >= 5:
            summa = sum(self.current[:5])
            print(summa)
            del self.current[:5]
            
    def get_current_part(self):
        return self.current
