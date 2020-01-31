#######
#Autor: Cristiano Porfirio da Silva
#written: 31/01/2020
#hour:16:46h
#Proram : quantidade de numeros não primos Aprocimação Teoria de conjuntos
#
######################
import numpy as np

def calIndex2022(numero):
	a=np.array([2,3,5])
	qtnpLinear=np.sum(np.floor((numero-a)/30))
	b=np.array([4,6,8,9,10,12,14,15,16,18,20,21,22,24,25,26,27,28,30])
	qtnpLinear+=np.sum(np.floor((numero-b+30)/30))
	return qtnpLinear+1


def calcIndex30(numero):
#Quantidade de numeros não primos a cada 30 números
	return 20+22*np.floor((numero-2)/30)

def calcNaoPrimo(k,j,x,a):
#calcula um número não primo  dado k , j , x, a
# k={2,4,5,7,8,10,13,14}
# j e x  números das classes de trinta em trinta são 8 não primos possíveis
# a justes garente o resto
# (2*k+3+30*j)*(2*k+3+30*j+30*x+a)=2*b+1 um número impar não primo
	classe=2*k+3
	multiplicador=classe+30*j
	multiplicando=multiplicador+30*x+a
	return int(multiplicador*multiplicando )


def calculaMaxJ(numero):
#Relacionado ao crivo de Erastostes
#Supor x=0
	jmax=np.floor(np.sqrt(numero)/30)

	return int(jmax)

def calculaMaxJKA(numero,k,a):
#Relacionado ao crivo de Erastostes
#Supor x=0
        jmax=(np.sqrt(numero+(a*a))-2*k+3)/30
        return int(jmax)



def calculaMaxX(numero,k,j,a):
#Relacionado ao números de números não primos
#um máximo para cada x
# o maior X k=2 ; j=0; a=0
	xmax=np.floor(( numero/(2*k+3+30*j)-(2*k+3+30*j+a))/30)
	return int(xmax)


def quantidadePrimos(numero):
	#quantidade pela contagem de números não primos
	total=numero -(calcQTRestos731(numero)+calIndex2022(numero))
	return total

def calcQTRestos731(numero):
	qtnp=0
	qtnp+=calcQTResto(numero,7)
	qtnp+=calcQTResto(numero,11)
	qtnp+=calcQTResto(numero,13)
	qtnp+=calcQTResto(numero,17)
	qtnp+=calcQTResto(numero,19)
	qtnp+=calcQTResto(numero,23)
	qtnp+=calcQTResto(numero,29)
	qtnp+=calcQTResto(numero,31)
	return qtnp



def calcQTResto(numero,resto):
	soma=0
	menor=32
	menor=nextNaoPrimo(menor,resto)
	while (menor<=numero):
		soma+=1
		menor=nextNaoPrimo(menor,resto)
	return soma

def nextNaoPrimo(menorAnterior,resto):
	k=np.array([2,4,5,7,8,10,13,14])
	a7=np.array([24, 6,6,-6,-6,6,-6,-24])
	a11=np.array([16,20,4,-4,10,-16,-10,-20])
	a13=np.array([12,12,18,12,-12,-12,-12,-18])
	a17=np.array([4,-4,16,14,4,-4,-16,-14])
	a19=np.array([0,18,0,0,12,0,-18,-12])
	a23=np.array([22,2,-2,2,-2,8,-22,-8])
	a29=np.array([10,8,10,-10,-8,-10,2,-2])
	a31=np.array([6,0,-6,6,0,-6,0,0])
	next=np.array([0,0,0,0,0,0,0,0])
	if resto==7:
		a=a7
	elif resto==11:
		a=a11
	elif resto==13:
		a=a13
	elif resto==17:
		a=a17
	elif resto==19:
		a=a19
	elif resto==23:
		a=a23
	elif resto==29:
		a=a29
	elif resto==31:
		a=a31
	jmaior=calculaMaxJ(menorAnterior)
	menor=menorAnterior
	infimoAnterior=menor*302  # força o primeiro menor
	menorAnterior+=1
	passo=0
	for j in range(0,jmaior+1):
		for i in  range(0,8):
			x=calculaMaxX(menorAnterior,k[i],j,a[i])
			x+=1
			next[i]=calcNaoPrimo(k[i],j,x,a[i])
			#while(next[2*i]<menorAnterior):
		infimo=next.min()
		if (infimo < infimoAnterior):
			menor=infimo
			infimoAnterior=infimo
	return menor

def calcTermo30(numero):
	return np.floor(22*calcIndex30(numero))


def calcQuantidade(numero):
	qtnp= 1/(7) \
		+(6/(7*11)) \
		+((6*10)/(7*11*13)) \
		+((6*10*12)/(7*11*13*17)) \
		+((6*10*12*16)/(7*11*13*17*19))	\
		+((6*10*12*16*18)/(7*11*13*17*19*23)) \
		+((6*10*12*16*18*22)/(7*11*13*17*19*23*29)) \
		+((6*10*12*16*18*22*28)/(7*11*13*17*19*23*29*31)) \
		+((6*10*12*16*18*22*28*30)/(7*11*13*17*19*23*29*31*37)) \
		+((6*10*12*16*18*22*28*30*36)/(7*11*13*17*19*23*29*31*37*41)) \
		+((6*10*12*16*18*22*28*30*36*40)/(7*11*13*17*19*23*29*31*37*41*43)) \
		+((6*10*12*16*18*22*28*30*36*40*42)/(7*11*13*17*19*23*29*31*37*41*43*47)) \
		+((6*10*12*16*18*22*28*30*36*40*42*46)/(7*11*13*17*19*23*29*31*37*41*43*47*53)) \
		+((6*10*12*16*18*22*28*30*36*40*42*46*52)/(7*11*13*17*19*23*29*31*37*41*43*47*53*59)) \
		+((6*10*12*16*18*22*28*30*36*40*42*46*52*58)/(7*11*13*17*19*23*29*31*37*41*43*47*53*59*61))


	qtnp=np.floor( numero*qtnp)
	return qtnp
#valor=541
#valor =7919
#valor=1339  #1369
#valor=961
#valor=61
#valor=1000000
#print("valor", valor)


#print("2022", calIndex2022(valor))
#print("restos", calcQTRestos731(valor))
#print("resto 7",calcQTResto(valor,7))
#print("resto 11",calcQTResto(valor,11))
#print("resto 13",calcQTResto(valor,13))
#print("resto 17",calcQTResto(valor,17))
#print("resto 19",calcQTResto(valor,19))
#print("resto 23",calcQTResto(valor,23))
#print("resto 29",calcQTResto(valor,29))
#print("resto 31",calcQTResto(valor,31))
#print( nextNaoPrimo(valor,19))
#print("primos",valor -(calcQTRestos731(valor)+calIndex2022(valor)))
#print(calculaMaxJ(valor))
#qti=0
#numero=32
#for i in range(1,1000):
#	numero=nextNaoPrimo(numero,31)
#	print(numero,";") 
