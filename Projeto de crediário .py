print(' Lojão do Descontão')

print('Sou Matheus  Robert Santana Schon, responsável pelo crédito na loja. Vou verificar a liberação ou não de limite')

print('Qual é a sua profissão?  ')
str1=input()
print("profissão", str1)

print('Quanto é seu salário ?    ')
str2 = input()
print("salário", str2)


from datetime import date
data_atual= date.today()
str4 = data_atual.year

print( (str1) + " " + (str2) + " " + (str3))

str5 = int(str4) - int(str3)

print("idade", str5)

str6 = int(str2)*(int(str5)/1000)+100
print(str6)

#coding=latin-1
from math import*
from string import*

nomes = ["Henrique Junior Marcondes"]
idade = (str5)
n = [nome.strip().split(' ')[0] for nome in nomes]

print ('Qual o nome do produto ?:')
str7 = input()
print ('Qual o preço do produto ?:')
str8 = input()

limite = (str6)

qtcom = len(nomes[0])
qtpr = len(n[0])

porct = (float(str8)/float(str6))

if porct <= 0.6:
    print("Liberado!")
elif porct > 0.6 and porct <= 0.9:
    print("Liberado ao parcelar em até 2 vezes")
elif porct >= 0.91 and porct <= 1:
    print("Liberado ao parcelar em até 3 ou mais vezes")
else:
    print("Bloqueado")

if qtcom == (str5):
    valormax = qtcom
    valormin = (str5)
if qtcom > (str5):
    valormax = qtcom
    valormin = (str5)
if qtcom < (str5):
    valormax = (str5)
    valormin = qtcom

comdest = (str8) - qtpr

if valor >= valormin and valor <= valormax:
    print("Você tem um desconto de",qtpr)
    print("O Valor do seu produto ficou:",comdest)
