import math


class Graph():
    size = 0
    links = []
    tab = []

    def initialize_tab(self):
        self.tab = []
        for x in range(self.size):
            self.tab.append([])
            for y in range(self.size):
                if x != y:
                    self.tab[x].append(math.inf)
                else:
                    self.tab[x].append(0)

    def add_link(self, src, dst, distance):
        self.tab[src][dst] = distance
