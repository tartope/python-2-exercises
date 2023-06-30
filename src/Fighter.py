from Character import Character

class Fighter(Character):
    def __repr__(self):
        return f"{self.__class__.__name__}: {self.hit_points} hit points."