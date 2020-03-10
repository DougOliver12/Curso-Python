"""
Exercises curse python session 1 por Douglas


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
