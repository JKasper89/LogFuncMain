import unittest
from LogFunc import *


class ANDGateTest(unittest.TestCase):
    def testcase_00(self):
        a = ANDGate()
        self.assertFalse(a.Inputs[0], "Class ANDGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class ANDGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs, "Class ANDGate: Testcase 0 failed.")

    def testcase_01(self):
        a = ANDGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class ANDGate: Testcase 1 failed.")

    def testcase_02(self):
        a = ANDGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class ANDGate: Testcase 2 failed.")

    def testcase_03(self):
        a = ANDGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class ANDGate: Testcase 3 failed.")

    def testcase_04(self):
        a = ANDGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class ANDGate: Testcase 4 failed.")

    def testcase_05(self):
        a = ANDGate(4)
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class ANDGate: Testcase 5 failed.")

    def testcase_06(self):
        a = ANDGate(4)
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class ANDGate: Testcase 6 failed.")


class ORGateTest(unittest.TestCase):
    def testcase_00(self):
        a = ORGate()
        self.assertFalse(a.Inputs[0], "Class ORGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class ORGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs, "Class ORGate: Testcase 0 failed.")

    def testcase_01(self):
        a = ORGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class ORGate: Testcase 1 failed.")

    def testcase_02(self):
        a = ORGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class ORGate: Testcase 2 failed.")

    def testcase_03(self):
        a = ORGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class ORGate: Testcase 3 failed.")

    def testcase_04(self):
        a = ORGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class ORGate: Testcase 4 failed.")

    def testcase_05(self):
        a = ORGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class ORGate: Testcase 5 failed.")

    def testcase_06(self):
        a = ORGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class ORGate: Testcase 6 failed.")


class XORGateTest(unittest.TestCase):
    def testcase_00(self):
        a = XORGate()
        self.assertFalse(a.Inputs[0], "Class XORGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class XORGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs, "Class XORGate: Testcase 0 failed.")

    def testcase_01(self):
        a = XORGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class XORGate: Testcase 1 failed.")

    def testcase_02(self):
        a = XORGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class XORGate: Testcase 2 failed.")

    def testcase_03(self):
        a = XORGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class XORGate: Testcase 3 failed.")

    def testcase_04(self):
        a = XORGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class XORGate: Testcase 4 failed.")

    def testcase_05(self):
        a = XORGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = False
        a.execute()
        self.assertFalse(a.Outputs, "Class XORGate: Testcase 5 failed.")

    def testcase_06(self):
        a = XORGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.Inputs[3] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class XORGate: Testcase 6 failed.")


class NANDGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NANDGate()
        self.assertFalse(a.Inputs[0], "Class  NANDGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class  NANDGate: Testcase 0 failed.")
        self.assertTrue(a.Outputs, "Class  NANDGate: Testcase 0 failed.")

    def testcase_01(self):
        a = NANDGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class  NANDGate: Testcase 1 failed.")

    def testcase_02(self):
        a = NANDGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class  NANDGate: Testcase 2 failed.")

    def testcase_03(self):
        a = NANDGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs, "Class  NANDGate: Testcase 3 failed.")

    def testcase_04(self):
        a = NANDGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class  NANDGate: Testcase 4 failed.")

    def testcase_05(self):
        a = NANDGate(4)
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = True
        a.execute()
        self.assertFalse(a.Outputs, "Class  NANDGate: Testcase 5 failed.")

    def testcase_06(self):
        a = NANDGate(4)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.Inputs[3] = False
        a.execute()
        self.assertTrue(a.Outputs, "Class  NANDGate: Testcase 6 failed.")


class NOTGateTest(unittest.TestCase):
    def testcase_00(self):
        a = NOTGate(1)
        self.assertFalse(a.Inputs[0], "Class NOTGate: Testcase 0 failed.")
        self.assertTrue(a.Outputs[0], "Class NOTGate: Testcase 0 failed.")

    def testcase_01(self):
        a = NOTGate(3)
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class NOTGate: Testcase 1 failed.")
        self.assertFalse(a.Outputs[1], "Class NOTGate: Testcase 1 failed.")
        self.assertFalse(a.Outputs[2], "Class NOTGate: Testcase 1 failed.")


class HALFADDERGateTest(unittest.TestCase):
    def testcase_00(self):
        a = HALFADDERGate()
        self.assertFalse(a.Inputs[0], "Class HALFADDERGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class HALFADDERGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs[0], "Class HALFADDERGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs[1], "Class HALFADDERGate: Testcase 0 failed.")

    def testcase_01(self):
        a = HALFADDERGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class HALFADDERGate: Testcase 1 failed.")
        self.assertTrue(a.Outputs[1], "Class HALFADDERGate: Testcase 1 failed.")

    def testcase_02(self):
        a = HALFADDERGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class HALFADDERGate: Testcase 2 failed.")
        self.assertTrue(a.Outputs[1], "Class HALFADDERGate: Testcase 2 failed.")

    def testcase_03(self):
        a = HALFADDERGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class HALFADDERGate: Testcase 3 failed.")
        self.assertFalse(a.Outputs[1], "Class HALFADDERGate: Testcase 3 failed.")


class FULLADDERGateTest(unittest.TestCase):
    def testcase_00(self):
        a = FULLADDERGate()
        self.assertFalse(a.Inputs[0], "Class FULLADDERGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[1], "Class FULLADDERGate: Testcase 0 failed.")
        self.assertFalse(a.Inputs[2], "Class FULLADDERGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs[0], "Class FULLADDERGate: Testcase 0 failed.")
        self.assertFalse(a.Outputs[1], "Class FULLADDERGate: Testcase 0 failed.")

    def testcase_01(self):
        a = FULLADDERGate()
        a.Inputs[0] = False
        a.Inputs[1] = False
        a.Inputs[2] = True
        a.execute()
        self.assertFalse(a.Outputs[0], "Class FULLADDERGate: Testcase 1 failed.")
        self.assertTrue(a.Outputs[1], "Class FULLADDERGate: Testcase 1 failed.")

    def testcase_02(self):
        a = FULLADDERGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class FULLADDERGate: Testcase 2 failed.")
        self.assertTrue(a.Outputs[1], "Class FULLADDERGate: Testcase 2 failed.")

    def testcase_03(self):
        a = FULLADDERGate()
        a.Inputs[0] = False
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class FULLADDERGate: Testcase 3 failed.")
        self.assertFalse(a.Outputs[1], "Class FULLADDERGate: Testcase 3 failed.")

    def testcase_04(self):
        a = FULLADDERGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.Inputs[2] = False
        a.execute()
        self.assertFalse(a.Outputs[0], "Class FULLADDERGate: Testcase 4 failed.")
        self.assertTrue(a.Outputs[1], "Class FULLADDERGate: Testcase 4 failed.")

    def testcase_05(self):
        a = FULLADDERGate()
        a.Inputs[0] = True
        a.Inputs[1] = False
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class FULLADDERGate: Testcase 5 failed.")
        self.assertFalse(a.Outputs[1], "Class FULLADDERGate: Testcase 5 failed.")

    def testcase_06(self):
        a = FULLADDERGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = False
        a.execute()
        self.assertTrue(a.Outputs[0], "Class FULLADDERGate: Testcase 6 failed.")
        self.assertFalse(a.Outputs[1], "Class FULLADDERGate: Testcase 6 failed.")

    def testcase_07(self):
        a = FULLADDERGate()
        a.Inputs[0] = True
        a.Inputs[1] = True
        a.Inputs[2] = True
        a.execute()
        self.assertTrue(a.Outputs[0], "Class FULLADDERGate: Testcase 7 failed.")
        self.assertTrue(a.Outputs[1], "Class FULLADDERGate: Testcase 7 failed.")


if __name__ == "__main__":
    unittest.main()    
