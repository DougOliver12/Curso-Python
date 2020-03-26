"""

Exercicios curso python parte 1 por Douglas Magalhães

"""

import math

# 1 faca um programa que leia um numero inteiro e o imprima
numero = 44
print(type(numero))
print(numero)

# 2 faca um programa que leia um numero real e o imprima
numero = 44.3
print(type(numero))
type(numero)

# 3 peca para o usuario digitar 3 valores inteiros e imprima a soma deles

numero_1 = input("Primeiro numero:")
numero_2 = input("Segundo numero:")
numero_3 = input("Terceiro numero:")
t = (int(numero_1) + int(numero_2) + int(numero_3))
print(t)

# 4 leia um numero real e imprima o resultado ddo quadrado desse numero

var1 = int(input("Digite um inteiro: "))
var2 = int(input("Digite outro inteiro: "))
exp = var1 ** var2
print(exp)

# 5 leia um numero real e imprima a quinta parte desse numero

var3 = int(input("Digite um inteiro: "))
exp2 = var3 / 5
print(exp2)

# 6 E 7 leia uma temperatura em celsius e converta para fahrenheit E VICE E VERSA

celsius = int(input("Digite a temperatura em graus: "))
conversao = celsius * (9.0/5.0) + 32.0
print(conversao)
conversao2 = 5.0 * (conversao - 32.0) / 9.0
print(conversao2)

# 8 E 9 leia uma temperatura em kelvin e converta para celsius E VICE E VERSA

kelvin = int(input("Digite a temperatura em kelvin: "))
conversao3 = kelvin - 273.15
print(conversao3)
conversao4 = conversao3 + 273.15
print(conversao4)

# 10 E 11 leia uma velocidade em km/h e converta para m/s E VICE E VERSA
km = int(input("Digite a distancia em km/h : "))
conversao5 = km / 3.6
print(conversao5)
conversao6 = conversao5 * 3.6
print(conversao6)

# 12 E 13 leia uma distancia em milhas e converta para kilometros E VICE E VERSA

milhas = int(input("Digite a distancia em milhas : "))
conversao7 = 1.61 * milhas
print(conversao7)
conversao8 = conversao7 / 1.61
print(conversao8)

# 14 e 15 leia um angulo em graus e converta em radianos E VICE E VERSA

pi = 3.14
graus = int(input("Digite o angulo em graus : "))
conversao9 = graus * (pi / 180)
print(conversao9)
conversao10 = conversao9 * (180 / pi)
print(conversao10)

# 16 E 17 leia um comprimento em polegadas e converta em centimetros E VICE E VERSA

polegadas = int(input("Digite o comprimento em polegadas : "))
conversao11 = polegadas * 2.54
print(conversao11)
conversao12 = conversao11 / 2.54
print(conversao12)

# 18 E 19 leia um volume em metros cubicos e converta para litros E VICE E VERSA

mcub = int(input("Digite o volume em metros cubicos : "))
conversao13 = 1000 * mcub
print(conversao13)
conversao14 = conversao13 / 1000
print(conversao14)

# 20 E 21 leia um valor de massa em quilograma e converta em libras E VICE E VERSA

qgrama = int(input("Digite a massa em quilogramas : "))
conversao15 = qgrama / 0.45
print(conversao15)
conversao16 = conversao15 * 0.45
print(conversao16)

# 22 E 23 leia um comprimento em jardas e converta em metros E VICE E VERSA

jardas = int(input("Digite o comprimento em jardas : "))
conversao17 = 0.91 * jardas
print(conversao17)
conversao18 = conversao17 / 0.91
print(conversao18)

# 24 E 25 leia um valor de area em metros quadrados e converta em acres E VICE E VERSA


mquad = int(input("Digite a area em metros quadrados : "))
conversao19 = mquad * 0.000247
print(conversao19)
conversao20 = conversao19 * 4048.58
print(conversao20)

# 26 E 27 leia um valor de area em metros quadrados e converta em hectares E VICE E VERSA

mquad2 = int(input("Digite a area em metros quadrados : "))
conversao21 = mquad2 * 0.0001
print(conversao21)
conversao22 = conversao21 * 100000
print(conversao22)

# 28 faca a leitura de tres numeros e apresente a soma dos quadrados dos mesmos

num4 = int(input("Digite o primeiro numero : "))
num5 = int(input("Digite o segundo numero : "))
num6 = int(input("Digite o terceiro numero : "))
somaquad = ((num4 ** 2) + (num5 ** 2) + (num6 ** 2))
print(somaquad)

# 29 faca media de quatro notas

num7 = int(input("Digite uma nota : "))
num8 = int(input("Digite uma nota : "))
num9 = int(input("Digite uma nota : "))
num10 = int(input("Digite uma nota : "))
medianota = ((num7 + num8 + num9 + num10) / 4)
print("A media e :", medianota)

# 30 ler valor do real e cotacao do dolar,, imprimir valor em dolares

real = int(input("Digite o valor em reais : "))
cotdolar = float(input("Digite a cotacao do dolar : "))
conversaoreal = real / cotdolar
print(conversaoreal)

# 31 leia um numero inteiro e imprima o seu antecessor e o seu sucessor

num = int(input("Digite um numero : "))
antecessor = num - 1
sucessor = num + 1
print("Antecessor", antecessor)
print("Sucessor", sucessor)

# 32 leia um numero inteiro e apresente a soma do sucessor de seu triplo com o antecessor de seu dobro

numint = int(input("Digite um numero : "))
somatrisuc = (((numint * 3) + 1) + ((numint * 2) - 1))
print(somatrisuc)

# 33 leia o tamanho do lado de um quadrado e imprima como resultado sua area

ladoquad = int(input("Digite o valor do lado : "))
areaquad = ladoquad * ladoquad
print(areaquad)

# 34 leia o valor de raio de um circulo e imprima o valor dda area do circulo

raiocirc = int(input("Digite o valor do raio : "))
areacirc = (pi * (raiocirc ** 2))
print(areacirc)



