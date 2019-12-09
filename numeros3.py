#######
#Autor: Cristiano Porfirio da Silva
#written: 30/11/2019
#hour:12:29
#Proram : quantidade de numeros não primos
#
######################
import numpy as np


def calcIndex(numero):
	index=np.floor((numero-2)/30)
	qtnp=(1/7)+(6/(7*11))+((6*10)/(7*11*13))+((6*10*12)/(7*11*13*17))+((6*10*12*16)/(7*11*13*17*19))+((6*10*12*16*18)/(7*11*13*17*19*23))+((6*10*12*16*18*22)/(7*11*13*17*19*23*29))+((6*10*12*16*18*22*28)/(7*11*13*17*19*23*29*31))
	qtnp*=index
	qtnp=np.floor(8*qtnp)
	qtnp+=20+22*index
	return qtnp


def numeros23(numero):
	index=np.floor((numero-2)/30)
	return 20 + 23*index

def numeros91(numero):
	a=np.array([91])
	result=np.floor((numero-a+210)/210)
	return np.sum(result)

def numeroGerador11(numero):
	if numero<121:
		return 0
	g=np.array([407, 121, 143, 187, 209, 253, 319, 341])
	result=np.floor((numero-g+330)/330)
	return np.sum(result)



def numeroGerador13(numero):
	if numero<169:
		return 0
	g=np.array([481, 533, 169, 221, 247, 299, 377, 403])
	result=np.floor((numero-g+390)/390)
	return np.sum(result)

def numeroGerador17(numero):
	if (numero<(17*17)):
		return 0
	k=np.array([37,41,43,17,19,23,29,31])
	g=17*k
	result=np.floor((numero-g+(17*30))/(17*30))
	return np.sum(result)


def numeroGerador19(numero):
	if numero<(19*19):
		return 0
	k=np.array([37,41,43,47,19,23,29,31])
	g=19*k
	result=np.floor((numero-g+(19*30))/(19*30))
	return np.sum(result)



def numeroGerador23(numero):
	if numero<(23*23):
		return 0
	k=np.array([37,41,43,47,79,23,29,31])
	g=23*k
	result=np.floor((numero-g+(23*30))/(23*30))
	return np.sum(result)



def numeroGerador29(numero):
	if (numero<(29*29)):
		return 0
	k=np.array([37,41,43,47,79,53,29,31])
	g=29*k
	result=np.floor((numero-g+(29*30))/(29*30))
	return np.sum(result)



def numeroGerador31(numero):
	if (numero<(31*31)):
		return 0
	k=np.array([37,41,43,47,79,53,59,31])
	g=31*k
	result=np.floor((numero-g+930)/930)
	return np.sum(result)


def numeroGerador37(numero):
	if (numero<(37*37)):
		return 0
	k=np.array([37,41,43,47,79,53,59,61])
	g=37*k
	result=np.floor((numero-g+(37*30))/(37*30))
	return np.sum(result)

def calculoA(numero):
	a=0
	a+=numeroGerador11(numero)
	a+=numeroGerador13(numero)
	a+=numeroGerador17(numero)
	a+=numeroGerador19(numero)
	a+=numeroGerador23(numero)
	a+=numeroGerador29(numero)
	a+=numeroGerador31(numero)
	#a+=numeroGerador37(numero)
	a+=numeros23(numero)
	a+=numeros91(numero)
	return a


#valor=541
#print(valor)
#print( calculoA(valor))
#print( calcIndex(valor))

#valor=7921
#print(valor)
#print( calculoA(valor))
#print( calcIndex(valor))


#valor=1000000000
#print(valor)
#print( calculoA(valor))
#print( calcIndex(valor))
#print(valor-50000000)
