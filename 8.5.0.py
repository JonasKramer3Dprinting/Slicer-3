class A():
    def __init__(self):
        self.__priv = "Ich bin privat"
        self._prot = "Ich bin protected"
        self.pub = "Ich bin öffentlich"

x = A()
print(x.pub)
x.pub = "Man kann meinen Wert ändern und das ist gut so"
print(x.pub)

print(x._prot)
x._prot = "Man Wert kann aber sollte nicht von außen geändert werden!"
print(x._prot)

# print(x.__priv)

print(x._A__priv)
x._A__priv = "Auch ich kann verändert werden"
print(x._A__priv)