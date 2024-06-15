from . import constant as c


class Tile:
    """
       y j

    3*DY   ┌────────┬───────┬───────┐
           │        │       │       │
         2 │        │       │       │
           │        │       │       │
    3*DY   ├────────NW──────NE──────┤
           │        │       │       │
         1 │        │   M   │       │
           │        │       │       │
      DY   ├────────SW──────SE──────┤
           │        │       │       │
         0 │        │       │       │
           │        │       │       │
       0   └────────┴───────┴───────┘
                0       1       2         i
           0        DX      2*DX    3*DX  x
    """

    i: int
    j: int

    w: int
    e: int
    x: int

    s: int
    n: int
    y: int

    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        self.compute_x()
        self.compute_y()

    @classmethod
    def from_pixel(cls, x: int, y: int) -> "Tile":
        i = x // c.DX
        j = y // c.DY
        return cls(i, j)

    def compute_x(self):
        self.w = self.i * c.DX
        self.e = (self.i + 1) * c.DX
        self.x = (self.w + self.e) // 2

    def compute_y(self):
        self.s = self.j * c.DY
        self.n = (self.j + 1) * c.DY
        self.y = (self.s + self.n) // 2

    def __str__(self):
        return f"Tile({self.i},{self.j})"

    def __eq__(self, other) -> bool:
        return self.i == other.i and self.j == other.j
