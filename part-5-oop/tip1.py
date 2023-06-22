class Top:
    def __init__(self, names=[]) -> None:
        names.append("TOP")
        self.names = names
        self.size = len(names)


class Left(Top):
    def __init__(self, names=[]) -> None:
        names.append("LEFT")
        super().__init__(names)

class Right(Top):
    def __init__(self, names=[]) -> None:
        names.append("RIGHT")
        super().__init__(names)

class Bottom(Left, Right):
    def __init__(self, names=[]) -> None:
        names.append("BOTTOM")
        super().__init__(names)

bottom = Bottom([])

print(bottom.super().size)

