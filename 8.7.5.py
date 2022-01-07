class Stapel():
    def __init__(self):
        self.__inhalt = []

    def add(self, element):
        print(self.__inhalt)
        self.__inhalt.append(element)
        print(self.__inhalt)

    def pop_last(self):
        print(self.get_last())
        self.__inhalt.pop()

    def is_empty(self):
        wahrheit = False
        if len(self.__inhalt) == 0:
            wahrheit = True
        return wahrheit

    def get_last(self):
        if self.is_empty() == False:
            return self.__inhalt[-1]

    def clear_stack(self):
        while self.is_empty() == False:
            self.pop_last()

stapel = Stapel()

print(stapel.get_last())

stapel.add(8)
stapel.add(9)
stapel.pop_last()

print(stapel.is_empty())

print(stapel.get_last())

stapel.add(1)
stapel.add(2)
stapel.add(3)
stapel.add(4)

stapel.clear_stack()

