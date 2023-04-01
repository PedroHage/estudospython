#Pedro Lawinscky Hage
#1
print("Alo mundo!")

#2

num = int(input("Digite um número:"))
print(f"O número mostrado foi {num}")

#3

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

soma = num1 + num2
print(f"A soma dos números é igual a {soma}")

#4

print("Coloque as suas notas")
n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
n4 = float(input("Nota 4:"))

res = (n1 + n2 +n3 + n4)/4
print("Essa é sua media:", res)

#5

print("Coloque um valor que será convertido de metros para centímetros")
mtr = int(input("Valor: "))
mtrcm = mtr*100
print(mtrcm, "cm")

#6

raio = float(input("Digite o raio de um círculo:"))
areac = 3.14*raio**2
print(f"Essa é a área do círculo {areac} ")

#7

ladoq = float(input("Digite o tamanho do lado de um quadrado:"))
l = ladoq ** 2
l2 = (ladoq**2)*2
print(f"Essa é a area do quadrado{l}")
print(f"Esse é o dobro da area do quadrado {l2}")

#8
gh = float(input("Quanto você ganha por hora de trabalho (R$)? "))
hm = float(input("Quantas hora você trabalha por mês? "))
salario = gh*hm
print(f"Voce ganha R${salario} por mês")

#9
fh = float(input("Coloque uma temperatura que será convertida de Fahrenheit para Celsius: "))
cs = 5 * ((fh-32) / 9)
print(f"Isso é igual a {cs}°C")

#10

cs2 = float(input("Coloque uma temperatura que será convertida de Celsius para Fahrenheit: "))
fh2 =(cs2*9/5) + 32
print(f"Isso é igual a {fh2}°F")

#11

nu1 = int(input("Coloque um numero inteiro: "))
nu2 = int(input("Coloque um numero inteiro: "))
nu3 = float(input("Coloque um numero Real: "))
a = (nu1*2)*(nu2/2)
b = (nu1*3)+nu3
c = nu3**3
print(f"o produto do dobro do primeiro com metade do segundo = {a}")
print(f"a soma do triplo do primeiro com o terceiro = {b}")
print(f"o terceiro elevado ao cubo {c}")

#12

altura = float(input("Coloque sua altura: "))
pi = (72.7*altura) - 58
print(f"Seu peso ideal é = {pi}")


#13

altura = float(input("Coloque sua altura: "))
sexo = input("Você é m(mulher) ou h(homem)?: ")
pih = (72.7*altura) - 58
pim = (62.1*altura) - 44.7
if sexo == "h":
  print(f"Peso ideal para Homem = {pih}")
else:
  print(f"Peso ideal para Mulher = {pim}")

#14
peixe = float(input("Quantos quilos de peixe foram pescados?: "))
excesso = peixe - 50
multa = excesso * 4

if excesso <= 0:
  print("Você não pagará multa")
else:
  print(f"Você pagará uma multa de R${multa}")

#15

gh1 = float(input("Quanto você ganha por hora de trabalho (R$)? "))
hm1 = float(input("Quantas hora você trabalha por mês? "))
salario1 = gh1*hm1
ir = salario1*0.11
inss = salario1*0.08
sind = salario1*0.05
salariol = salario1-ir-inss-sind

print(f"Voce ganha R${salario1} de salário bruto por mês")
print(f"Imposto de renda (11%): R${ir}")
print(f"INSS (8%): R${inss}")
print(f"Sindicato (5%): R${sind}")
print(f"Você ganha R${salariol} de salario liquido")

#16

apintada = float(input("Qual o tamanho da area a ser pintada(metros quadrados)?: "))
litros = (apintada/3)
latas = litros/18
preco = 80*latas
print(f"A quantidade de latas a serem compradas é {latas}")
print(f"O preço a ser gasto é R${preco}")


#17

apintada1 = float(input("Qual o tamanho da área a ser pintada(metros quadrados)?: "))
litros1 = (apintada1/6)
latas1 = litros1/18
latas2 = litros1/3.6
latas3 = litros1//18
latas03 = latas3
restolatas = litros1%18
latas4 = 0
latas04 = latas4

if restolatas > 0.20:
  latas03 = latas3+1
else:
  latas04 = latas4 +1
preco1 = 80*latas1
preco2 = 25*latas2
print("Caso deseje comprar apenas latas de 18 litros:")
print(f"A quantidade de latas a serem compradas é {latas1} e, o preço é R#{preco1}")
print("Caso deseje comprar apenas galões de 3,6 litros")
print(f"A quantidade de latas a serem compradas é {latas2} e, o preço é R${preco2}")
print("Caso deseje comprar alternadamente galões de 3,6 litros e latas de 18 litros para que tenha menos disperdicio:")
print(f"A quantidade de galões de 3,6 litros é {latas04}, a de latas de 18 litros é {latas03}")

#18

arquivo = float(input("Qual o tamanho do arquivo(MB)?: "))
arquivomb = arquivo*8
link = float(input("Qual a velocidade do link de internet(Mbps)?: "))
tempo = (arquivomb/link)/60
print(f"Para fazer download desse arquivo será necessario {tempo} minutos")
