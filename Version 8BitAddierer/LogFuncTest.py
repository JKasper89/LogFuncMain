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

class HalfAdderTest(unittest.TestCase):
    def testcase_00(self):
        a = HALFADDERGate()
        self.assertEqual(False, a.Inputs[0], "Class HalfAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[1], "Class HalfAdderTestcase 0 failed.")
        self.assertEqual(False, a.Outputs[0], "Class HalfAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[1], "Class HalfAdderTestcase 0 failed.")


    def testcase_02(self):
        a = HALFADDERGate()
        testdatas = [
            [False, False, False, False],
            [False, True, False, True],
            [True, False, False, True],
            [True, True, True, False]
        ]
        for testdata in testdatas:
            for i in range(0, 2):
                a.Inputs[i] = testdata[i]
            a.execute()
            self.assertEqual(testdata[2], a.Outputs[0], "Class HalfAdder Testcase 2 failed: "+testdata.__str__())
            self.assertEqual(testdata[3], a.Outputs[1], "Class HalfAdder Testcase 2 failed: "+testdata.__str__())




class FullAdderTest(unittest.TestCase):
    def testcase_00(self):
        a = FULLADDERGate()
        self.assertEqual(False, a.Inputs[0], "Class FullAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[1], "Class FullAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[2], "Class FullAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[0], "Class FullAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[1], "Class FullAdder Testcase 0 failed.")


    def testcase_02(self):
        a = FULLADDERGate()
        testdatas = [
            [False, False, False, False, False],
            [False, False, True, True, False],
            [False, True, False, True, False],
            [False, True, True, False, True],
            [True, False, False, True, False],
            [True, False, True, False, True],
            [True, True, False, False, True],
            [True, True, True, True, True]
        ]
        for testdata in testdatas:
            for i in range(0, 3):
                a.Inputs[i]= testdata[i]
            a.execute()
            self.assertEqual(testdata[3], a.Outputs[1], "Class FullAdder Testcase 2 failed: "+testdata.__str__())
            self.assertEqual(testdata[4], a.Outputs[0], "Class FullAdder Testcase 2 failed: "+testdata.__str__())

class EightBitAdderTest(unittest.TestCase):
    def testcase_00(self):
        a = EightBitAdderGate()
        self.assertEqual(False, a.Inputs[0], "Class EightBitAdder Testcase 0 failed." )
        self.assertEqual(False, a.Inputs[1], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[2], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[3], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[4], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[5], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[6], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[7], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[8], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[9], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[10], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[11], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[12], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[13], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[14], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Inputs[15], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[0], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[1], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[2], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[3], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[4], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[5], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[6], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[7], "Class EightBitAdder Testcase 0 failed.")
        self.assertEqual(False, a.Outputs[8], "Class EightBitAdder Testcase 0 failed.")

    def testcase_02(self):
        a = EightBitAdderGate()
        testdatas = [
            [False, False, False, False, False, False, False, False,
             False, False, False, False, False, False, False, False,
             False,
             False, False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False, True,
             False, False, False, False, False, False, False, False,
             False,
             False, False, False, False, False, False, False, True],
            [False, False, False, False, False, False, False, True,
             False, False, False, False, False, False, False, True,
             False,
             False, False, False, False, False, False, True, False],
            [False, False, False, False, False, False, True, True,
             False, False, False, False, False, False, False, True,
             False,
             False, False, False, False, False, True, False, False]
        ]
        for testdata in testdatas:
            for i in range(0, 16):
                a.Inputs[i] = testdata[i]
            a.execute()
            self.assertEqual(testdata[16], a.Outputs[0], "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[17], a.Outputs[1], "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[18], a.Outputs[2], "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[19], a.Outputs[3], "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[20], a.Outputs[4], "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[21], a.Outputs[5], "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[22], a.Outputs[6], "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[23], a.Outputs[7], "Class FullAdder Testcase 2 failed: " + testdata.__str__())
            self.assertEqual(testdata[24], a.Outputs[8], "Class FullAdder Testcase 2 failed: " + testdata.__str__())

if __name__ == "__main__":
    unittest.main()    