#######
#Autor: Cristiano Porfirio da Silva
#written: 31/01/2020
#hour:16:47h
#Proram : quantidade de numeros não primos Aprocimação Teoria de conjuntos
#
######################


import unittest
import numeros7
class ContaNaoPrimos(unittest.TestCase):
	def test_conta23(self):
		self.assertEqual(numeros7.calIndex2022(31),20)
		self.assertEqual(numeros7.calIndex2022(61),42)
		self.assertEqual(numeros7.calIndex2022(91),64)


	def test_conta91(self):
		self.assertEqual(numeros7.calcQTResto(31,31),0)
		self.assertEqual(numeros7.calcQTResto(91,31),1)
		self.assertEqual(numeros7.calcQTResto((91+210),31),3)
		self.assertEqual(numeros7.calcQTResto((91+420),31),8)
		self.assertEqual(numeros7.calcQTResto((91+210*5),31),18)

	def test_contaLinear(self):
		self.assertEqual(numeros7.nextNaoPrimo(32,31),91)
		self.assertEqual(numeros7.nextNaoPrimo(61,31),91)
		self.assertEqual(numeros7.nextNaoPrimo(91,31),121)
		self.assertEqual(numeros7.nextNaoPrimo(121,31),301)
		self.assertEqual(numeros7.nextNaoPrimo(541,31),721)
		self.assertEqual(numeros7.nextNaoPrimo(7921,31),7981)
		self.assertEqual(numeros7.nextNaoPrimo(1021,31),1081)
	def test_conta1bilhao(self):
		self.assertTrue(numeros7.quantidadePrimos(541)<=(100))
		self.assertEqual(numeros7.quantidadePrimos(541),(100))
		self.assertTrue(numeros7.quantidadePrimos(7919)<=(1000))
		self.assertEqual(numeros7.quantidadePrimos(7919),(1000))
		self.assertTrue(numeros7.quantidadePrimos(1000000)<=(78498))
		self.assertEqual(numeros7.quantidadePrimos(1000000),(78498))

if __name__== '__main__': 
	unittest.main(warnings='ignore')

