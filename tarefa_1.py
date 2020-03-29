"""

Exercicios Curso Python Udemy parte 1 por Douglas Magalhães

"""

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

# 20 E 21 leia um valor de massa em quilogramas e converta em libras E VICE E VERSA

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

num7 = float(input("Digite uma nota : "))
num8 = float(input("Digite uma nota : "))
num9 = float(input("Digite uma nota : "))
num10 = float(input("Digite uma nota : "))
medianota = ((num7 + num8 + num9 + num10) / 4)
print("A media e :", medianota)

# 30 ler valor do real e cotacao do dolar,, imprimir valor em dolares

real = int(input("Digite o valor e""m reais : "))
cotdolar = float(input("Digite a cotacao do dolar : "))
conversaoreal = real / cotdolar
print("O valor em dolares e: ", conversaoreal)

# 31 leia um numero inteiro e imprima o seu antecessor e o seu sucessor

num = int(input("Digite um numero : "))
antecessor = num - 1
sucessor = num + 1
print("Antecessor: ", antecessor)
print("Sucessor: ", sucessor)

# 32 leia um numero inteiro e apresente a soma do sucessor de seu triplo com o antecessor de seu dobro

numint = int(input("Digite um numero : "))
somatrisuc = (((numint * 3) + 1) + ((numint * 2) - 1))
print(somatrisuc)

# 33 leia o tamanho do lado de um quadrado e imprima como resultado sua area

ladoquad = int(input("Digite o valor do lado : "))
areaquad = ladoquad * ladoquad
print("A area do Quadrado e: ", areaquad)

# 34 leia o valor de raio de um circulo e imprima o valor dda area do circulo

raiocirc = int(input("Digite o valor do raio : "))
areacirc = (pi * (raiocirc ** 2))
print("A area do Circulo e: ", areacirc)

# 35 sejam a e b catetos e um triangulo, calcule a hipotenusa

import math
cat1 = int(input("Digite o valor do cateto 1 : "))
cat2 = int(input("Digite o valor do cateto 2 : "))
hip1 = cat1 ** 2 + cat2 ** 2
hip2 = math.sqrt(hip1)
print("A Hipotenusa e: ", hip2)

# 36 leia a altura e o raio de um cilindro circular e imprima o volume

aut1 = float(input("Digite o valor da altura do cilindro : "))
raio2 = float(input("Digite o valor do raio do cilindro : "))
volcilindro = (pi * ((raio2 ** 2) * aut1))
print("O volume e: ", volcilindro)

# 37 faca um programa que leia um valor de um produto e imprima com 12 % de desconto

valorproduto = float(input("Digite o valor do produto : "))
novovalorproduto = valorproduto * 0.88
print("O valor com desconto e: ", novovalorproduto)

# 38 leia o salario e imprima o mesmo com 25% de aumento

valorsalario = float(input("Digite o valor do salario : "))
novossal = valorsalario * 0.25
print("Seu salario novo e: ", novossal + valorsalario)

# 39 780.000.00 divididos para 3 jogadores, o primeiro 46%, o segundo 32% e o terceiro o restante, imprima os valores

primcoloq = 780000.00 * 0.46
print("O primeiro colocado ganhou: ", primcoloq)
seccoloq = 780000.00 * 0.32
print("O segundo colocado ganhou: ", seccoloq)
terccoloq = 780000.00 - primcoloq-seccoloq
print("O terceiro colocado ganhou: ", terccoloq)
print("Total: ", primcoloq+seccoloq+terccoloq)

# 40 um encanador ganha R$ 30.00 por dia aplique 8% de imposto de renda sobre os dias trabalhados e imprima o resultado

dias = float(input("Digite a quantidade de dias trabalhados: "))
salariototal = dias * 30.00
impostorenda = salariototal *0.92
print(salariototal - impostorenda,"a menos no salario.")

# 41 faca um programa que leia o valor da hora trabalhada e o numero de horas no mes, imprima o valor total com 10% de bonus

valhoras = float(input("Digite o valor da hora trabalhada: "))
horas = float(input("Digite a quantidade de horas trabalhados: "))
valtotalhoras = horas * valhoras
print("Total de horas: ", valtotalhoras)
valbonus = valtotalhoras * 0.1
print("Valor do bonus: R$ ", valbonus)

# 42 receba o salario base de um funcionario. Calcule e imprima o salario a receber  com 5% de gratificacao e 7% de imposto

salario = float(input("Digite o salario: "))
grat = salario * 0.05
salbruto = salario + grat
print("O valor com gratificacao: R$ ", salbruto)
desc = salbruto * 0.93
print("O valor do desconto e: R$ ", salbruto - desc)

# 43 a partir de um valo lido: total a pagar com 10%, o valor de cada parcela 3x sem juros, comissao de 5% do vendedor
# sobre o valor com desconto se for a vista e 5% do vendedor sobre valor total no caso de ser parcelada

valcompra =float(input("Digite o valor do produto em R$: "))
string1 = input("a vista? ")
if string1 == "S" or string1 == "Sim":
        print("A vista tem 10% de desconto, o valor sera de R$: ", valcompra * 0.9)
elif string1 == "N" or string1 == "Nao":
        print("A prazo somente por 3 x sem juros cada parcela de de R$: ", valcompra / 3)

# 44 receba a altura do degrau de uma escada e altura que o usuario deseja subir utilizando a escada,imprima a quantidade de degraus
# ele devera subir para chegar ate o topo

alturaegral = float(input("Digite a altura do degral: "))
alturasubir = float(input("Digite a altura que deseja chegar: "))
degraus =alturasubir / alturaegral
print("É necessario de", degraus," degrais!!!")

# 45 faça um programa para converter uma letra maiuscula em letra minuscula, use a tabela ascii
stringletra = input("Digite a letra em maiusculo: ")
print(stringletra.lower())

# 46 E 47 faca um programa que leia um numero inteiro positivo de tres digitos e gere um outro numero invertido imprima
# um digito por linha

seq = []
while True:
    n = int(input("Digite n: "))
    if n == 0: break
    seq.append(n)
for i in reversed(seq):
    print(i)

# 48 leia um valor em segundos e imprima em minutos e horas e segundos

segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundos // 86400
segundos_rest = segundos % 86400
horas = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
minutos = segundos_rest // 60
segundos_rest = segundos_rest % 60

print(dias,"dias,",horas,"horas,",minutos,"minutos e",segundos_rest,"segundos.")

# 49 cronometro

import time, sys

for i in range(0, 10):
    sys.stdout.write("\r{}".format(i))
    sys.stdout.flush()
    time.sleep(1)

print ("\nFim")

# 50 implemente um programa que calcule o ano do nascimento atraves da idade e ano atual

idatual = int(input("Digite a idade atual: "))
anoatual = int(input("Digite o ano atual: "))
anonasc = anoatual - idatual
print("Voce nasceu em", anonasc)

# 51 escreva um programa que leia as coordenadas X e Y, de  pontos no R ao quadrado e calcule sua distancia da origem

import math

px = int(input("Digite o ponto x: "))
py = int(input("Digite o ponto y: "))

d = math.sqrt(px ** 2 + py ** 2)
print("A distancia e:",d)

# 52 tres amigos jogaram na loteria, caso eles ganhem, o premio sera distribuido proporcionamente ao valor da aposta
# leia qual o valor da aposta, e imprima o valor do premio para cada apostador

ap1 = int(input("Apostador 1, qual é o valor da sua aposta?: "))
ap2 = int(input("Apostador 2, qual e o valor da sua aposta?: "))
ap3 = int(input("Apostador 3, qual e o valor da sua aposta?: "))
aptotal = ap1 + ap2 + ap3
p1 = ap1 * 100 / aptotal
p2 = ap2 * 100 / aptotal
p3 = ap3 * 100 / aptotal
print(p1)
print(p2)
print(p3)

# 53 faca um programa para ler as dimensoes de um terreno, comprimento e largura bem ccomo o preco o metro, imprima o
# custo para cercar o terreno

comprimento = float(input("Comprimento o terreno: "))
largura = float(input("Largura o terreno: "))
valorcerca = float(input("Valor da cerca: "))

valorfinal = (comprimento * largura) * valorcerca
print("O valor total a cerca e de:", valorfinal)



