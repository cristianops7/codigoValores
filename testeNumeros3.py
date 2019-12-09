import unittest
import numeros3
class ContaNaoPrimos(unittest.TestCase):
	def test_conta23(self):
		self.assertEqual(numeros3.numeros23(31),20)
		self.assertEqual(numeros3.numeros23(61),43)
		self.assertEqual(numeros3.numeros23(91),66)


	def test_conta91(self):
		self.assertEqual(numeros3.numeros91(31),0)
		self.assertEqual(numeros3.numeros91(91),1)
		self.assertEqual(numeros3.numeros91(91+210),2)
		self.assertEqual(numeros3.numeros91(91+420),3)
		self.assertEqual(numeros3.numeros91(91+210*5),6)
	
	def test_contaLinear(self):
		self.assertEqual(numeros3.calculoA(31),20)
		self.assertEqual(numeros3.calculoA(61),(20+23))
		self.assertEqual(numeros3.calculoA(91),(20+(23*2)+1))
		self.assertEqual(numeros3.calculoA(121),(20+(23*3)+1+1))
		self.assertEqual(numeros3.calculoA(541),441)
		self.assertEqual(numeros3.calculoA(7921),(7921-1000))
		self.assertEqual(numeros3.calculoA(1021),(1021-172))
	def test_conta1bilhao(self):
		self.assertTrue(numeros3.calculoA(1000000000)<(1000000000-50847534))
		self.assertEqual(numeros3.calculoA(1000000000),(1000000000-50847534))

if __name__== '__main__': 
	unittest.main(warnings='ignore')

