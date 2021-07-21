#from the book effective python 90 specyfic ways tp write better python

class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

r1 = Resistor(10e3)

class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)
        self.voltage = 0

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms

r2 = VoltageResistance(1e3)
print(f"before: {r2.current:.2f} amps")
r2.voltage = 20
print(f"after: {r2.current:.2f} amps")


class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError(f'ohms bust be > ; got {ohms}')
        self._omhs = ohms

r3 = BoundedResistance(1e3)
r3.ohms = 2e1

class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError(f'The omhs is immutable')
        self._omhs = ohms

r4 = FixedResistance(3e10)

r4.ohms = 2e3
