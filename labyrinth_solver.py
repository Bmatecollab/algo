import random
import matplotlib.pyplot as plt
from typing import List, Optional


class Labyrinth:
    """
    Labirintus osztály, amely egy négyzetrács alapú táblázatot reprezentál.
    A cél a (m-1, m-1) pont, és a célhoz vezető lehetséges utak számát számítjuk ki.
    """

    def __init__(self, m: int):
        """
        Inicializálja a labirintust adott méretben.
        :param m: A labirintus mérete (m x m)
        """
        self.m: int = m  # A labirintus mérete
        self.table: List[List[Optional[int | str]]] = [[None for _ in range(m)] for _ in range(m)]  # Mezők tárolása
        self.table[self.m - 1][self.m - 1] = "CEL"  # A cél mező beállítása

    def add_forbidden(self, x: int, y: int):
        """
        Tiltott mező hozzáadása a labirintushoz.
        A kezdő (0,0) és cél (m-1, m-1) pontokat nem lehet tiltottá tenni.
        """
        if x == 0 and y == 0:
            return False
        if x == self.m - 1 and y == self.m - 1:
            return False
        self.table[x][y] = "x"  # A tiltott mezőt 'x' karakterrel jelöljük a táblában
        return True

    def add_random_forbidden_fields(self, num: int):
        """ Véletlenszerű tiltott mezők hozzáadása. """
        for _ in range(num):
            x = random.randint(0, self.m - 1)
            y = random.randint(0, self.m - 1)
            self.add_forbidden(x, y)

    def is_available(self, x, y):
        """ Ellenőrzi, hogy egy adott mező elérhető-e. """
        return 0 <= x < self.m and 0 <= y < self.m and self.table[x][y] != "x"

    def get_number_of_paths(self, x, y):
        """ Számolja az elérhető utak számát a célmezőig. """
        if x == self.m - 1 and y == self.m - 1:
            return 1
        if not self.is_available(x, y):
            return 0
        if self.table[x][y] is None:
            self.table[x][y] = self.get_number_of_paths(x + 1, y) + self.get_number_of_paths(x, y + 1)
        return self.table[x][y]

    def solve_with_loops(self):
        """ Ciklusok segítségével tölti fel az elérhető utak számát minden cellára. """
        for x in range(self.m - 1, -1, -1):
            for y in range(self.m - 1, -1, -1):
                if self.table[x][y] != "x":
                    self.get_number_of_paths(x, y)

    def __str__(self):
        """ A labirintus szöveges formátumú reprezentációja. """
        result = ""
        for row in self.table[::-1]:
            result += " ".join([f"{value: >5}" for value in row]) + "\n"
        return result

    def draw(self):
        """
        A labirintus grafikus megjelenítése.
        Ha a táblázat túl nagy, a matplotlib nem jeleníti meg, csak a konzolon lehet megnézni.
        """
        if self.m >= 16:
            print("Tul nagy a labirintus a grafikus megjeleniteshez, csak a konzolon jelenik meg az eredmeny.")
            return
        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')
        ax.table(cellText=self.table[::-1], loc='center')
        fig.tight_layout()
        plt.show()


if __name__ == '__main__':
    lab = Labyrinth(10)  # 10x10-es labirintus létrehozása
    lab.add_random_forbidden_fields(8)  # 8 tiltott mező hozzáadása
    lab.solve_with_loops()  # Útkeresés végrehajtása
    print(lab)  # Labirintus kiíratása konzolra
    lab.draw()  # Grafikus megjelenítés matplotlibbel
