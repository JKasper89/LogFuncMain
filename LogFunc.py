# -*- coding: utf8 -*-
__version__ = '2.1'  # Versionsinformationen
__author__ = 'Jan Kasper(jan.kasper@students.tbs1.de)'

from abc import ABC, abstractmethod


class LogFunc(ABC):  # Beginn der Klassendefinition
    """
    This is the parent class for logic gate classes.
    """

    def __init__(self, numberofinputs, numberofoutputs):  # Definition der Attribute
        """
        Create a logic Gate with given numberofinputs and numberofoutputs.
        Inputs and Outputs get the boolean value False.
        :param numberofinputs:False
        :param numberofoutputs:False
        """
        self.__Inputs = [False] * numberofinputs
        self.__Outputs = [False] * numberofoutputs
        self.__Name = type(self).__name__
        self.execute()

    # Definition der Getter und Setter
    def __getinputs(self):
        return self.__Inputs

    def __setinputs(self, value):
        self.__Inputs = value

    def __getoutputs(self):
        return self.__Outputs

    def _setoutputs(self, value):
        self.__Outputs = value

    def __getname(self):
        return self.__Name

    def __setname(self, value):
        self.__Name = value

    # Definition der Properties
    Inputs = property(__getinputs, __setinputs)
    Outputs = property(__getoutputs, None)
    Name = property(__getname, __setname)

    @abstractmethod
    def execute(self):  # Berechnung der logischen Verknüpfung
        pass

    def __str__(self):  # Ausformlierung der Stringumwandlung
        """
        Conerts the status of the logical gate to a string.
        :return: string of the gate status
        """
        cwidth = 60
        line = ''.ljust(cwidth, '#')
        format_str = "## {{0:10}}: {{1:{0}}} ##".format(cwidth - 18)
        temp = line
        temp += "\n" + format_str.format("Name", self.Name)
        temp += "\n" + format_str.format("Type", type(self).__name__)
        temp += "\n" + format_str.format("Inputs", str(self.Inputs))
        temp += "\n" + format_str.format("Outputs", str(self.Outputs))
        temp += "\n" + line
        return temp

    def show(self):  # Bildschirmausgabe der Stringumwandlung
        """
        Shows the value of each property of the class and the class name
        :return: None
        """
        print(self.__str__())


class ANDGate(LogFunc):  # Definition des AND Gates
    def __init__(self, numberofinputs=2):
        """
        Set the numberofinputs, by default 2, and 1 Output
        :param numberofinputs:
        """
        super().__init__(numberofinputs, 1)

    def execute(self):  # Berechnung der logischen Verknüpfung
        """
        Set the Output to True when all Inputs are True
        :return: None
        """
        if self.Inputs.count(False) == 0:
            self._setoutputs(True)
        else:
            self._setoutputs(False)


class ORGate(LogFunc):  # Definition des OR Gates
    def __init__(self, numberofinputs=2):
        """
        Set the numberofinputs, by default 2, and 1 Output
        :param numberofinputs:
        """
        super().__init__(numberofinputs, 1)

    def execute(self):  # Berechnung der logischen Verknüpfung
        """
        Set the Output to False when all Inputs are False.
        :return: None
        """
        if self.Inputs.count(True) == 0:
            self._setoutputs(False)
        else:
            self._setoutputs(True)


class XORGate(LogFunc):  # Definition des XOR Gates
    def __init__(self, numberofinputs=2):
        """
        Set the numberofinputs, by default 2, and 1 Output
        :param numberofinputs:
        """
        super().__init__(numberofinputs, 1)

    def execute(self):  # Berechnung der logischen Verknüpfung
        """
        Set The Output to True when there is an uneven count of True Inputs.
        :return: None
        """
        if self.Inputs.count(True) % 2 == 1:
            self._setoutputs(True)
        else:
            self._setoutputs(False)


class NANDGate(LogFunc):  # Definition des NAND Gates
    def __init__(self, numberofinputs=2):
        """
        Set the numberofinputs, by default 2, and 1 Output
        :param numberofinputs:
        """
        super().__init__(numberofinputs, 1)

    def execute(self):  # Berechnung der logischen Verknüpfung
        """
        Set The Output to True if any Input is false.
        :return: None
        """
        self._setoutputs(True)
        if self.Inputs.count(False) == 0:
            self._setoutputs(False)


class NOTGate(LogFunc):  # Definition des NOT Gates
    def __init__(self, numberofinputs=1):
        """
        Set the number of InputOuput Pairs. By default 1.
        :param numberofinputs:
        """
        super().__init__(numberofinputs, numberofinputs)

    def execute(self):  # Berechnung der logischen Verknüpfung
        outputs = [None] * len(self.Outputs)
        for i in range(len(self.Inputs)):
            outputs[i] = not self.Inputs[i]
        self._setoutputs(outputs)


class HALFADDERGate(LogFunc):  # Definition des Halfadder
    def __init__(self):
        """
        set 2 inputs and 2 outputs
        """
        self.__myxor = XORGate(2)
        self.__myand = ANDGate(2)
        super().__init__(2, 2)

    def execute(self):  # Berechnung des Halfadders
        """
        First Output is Carry Bit, Second Output is Sum
        """
        self.__myxor.Inputs = self.Inputs
        self.__myand.Inputs = self.Inputs
        self.__myxor.execute()
        self.__myand.execute()
        self._setoutputs([self.__myand.Outputs, self.__myxor.Outputs])


class FULLADDERGate(LogFunc):  # Definition des Fulladder
    def __init__(self):
        """
        set 3 inputs and 2 outputs
        """
        self.__myhadder1 = HALFADDERGate()
        self.__myhadder2 = HALFADDERGate()
        self.__myor = ORGate()
        super().__init__(3, 2)

    def execute(self):  # Berechnung des Fulladder
        """First Output is Carry Bit, second is Sum Bit"""
        self.__myhadder1.Inputs = [self.Inputs[0], self.Inputs[1]]
        self.__myhadder1.execute()
        self.__myhadder2.Inputs = [self.__myhadder1.Outputs[1], self.Inputs[2]]
        self.__myhadder2.execute()
        self.__myor.Inputs = [self.__myhadder1.Outputs[0], self.__myhadder2.Outputs[0]]
        self.__myor.execute()
        self._setoutputs([self.__myor.Outputs, self.__myhadder2.Outputs[1]])
