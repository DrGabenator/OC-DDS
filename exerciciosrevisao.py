#1- Escreva um programa que mostre na tela a frase:
#Olá, mundo da programação!
def mensagem():
    print("Olá, mundo da programação!")

#2- Crie um programa que declare uma variável chamada nome, armazene seu nome nela e mostre a mensagem:
#Olá, [nome]!
def nome():
    nome: str = "Gabriel"
    print(f"Olá, {nome}")

#3- Escreva um programa que declare duas variáveis inteiras, a e b, atribua valores a elas e mostre na tela a soma dos dois números.
def soma():
    valor1: int = 5
    valor2: int = 10
    print(f"A soma de {valor1} e de {valor2} é {valor1 + valor2}")

#4- Crie um programa que receba um número inteiro e mostre o dobro desse número.
def dobro():
    numero: int = int(input("Digite um número inteiro para ver o dobro desse número.\n"))
    resultado = numero * 2
    print(f"O dobro de {numero} é {resultado}")

#5- Escreva um programa que receba dois números e mostre na tela:
#•	a soma
#•	a subtração
#•	a multiplicação
def operacoes():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    print(f"A soma de {numero1} e {numero2} é {numero1 + numero2}")
    print(f"A subtração de {numero1} e {numero2} é {numero1 - numero2}")
    print(f"A multiplicação de {numero1} e {numero2} é {numero1 * numero2}")

#6- Crie um programa que leia a idade de uma pessoa e mostre a mensagem:
#Você tem [idade] anos.
def idade():
    idade = int(input("Digite a sua idade: "))
    print(f"Você tem {idade} anos!")

#7- Escreva um programa que receba um número e informe se ele é par ou ímpar.
def parouimpar():
    numero = int(input("Digite um número para descobrir se ele é par ou impar: "))
    if(numero % 2 == 0):
        print(f"O número {numero} é par!")
    else:
        print(f"O número {numero} é impar!")

#8- Crie um programa que receba a nota de um aluno e mostre:
#•	Aprovado se a nota for maior ou igual a 7
#•	Reprovado caso contrário.
def notaaluno():
    nota = int(input("Digite a nota do aluno: "))
    if(nota >= 7 and nota <= 10):
        print(f"O aluno está aprovado com nota {nota}")
    elif(nota >= 0 and nota < 7):
        print(f"O aluno está reprovado com nota {nota}!")
    else:
        print(f"A nota do aluno {nota} é uma nota inválida!")

#9- Escreva um programa que mostre na tela os números de 1 até 10 usando uma estrutura de repetição.
def contador():
    contador = 1
    while contador <= 10:
        print(f"{contador}")
        contador += 1

#10- Crie um programa que peça um número ao usuário e mostre a tabuada desse número de 1 a 10.
def tabuada():
    numero = int(input("Digite um número para saber sua tabuada: "))
    contador = 1
    while contador <= 10:
        print(f"{numero} multiplicado por {contador} é: {numero * contador}")
        contador += 1

#11- Escreva um programa que leia 5 números e mostre a soma 
# de todos eles.
def somaCincoNumeros():
    listaDeNumeros = []
    contador = 1
    while contador <= 5:
        numeroDigitado = int(input(f"Digite o número {contador} da lista: "))
        listaDeNumeros.append(numeroDigitado)
        if(contador == 5):
            print(f"O resultado total dos números digitados é de: {sum(listaDeNumeros)}")
        contador += 1

#12- Crie um programa que receba um número e mostre todos os 
# números de 1 até esse número.
def contadorDeNumeroAteX():
    numero = int(input("Digite um número para mostrar todos os números de 1 até o número digitado: "))
    contador = 1
    while contador <= numero:
        print(f"{contador}")

#13- Escreva um programa que receba três números e mostre 
# qual deles é o maior.
def maiorDentreTresNumeros():
    listaDeNumeros = []
    for numero in range(1, 4):
        numeroDigitado = int(input(f"Digite o número {numero}: "))
        listaDeNumeros.append(numeroDigitado)
    print(f"O maior número da lista é: {max(listaDeNumeros)}")

#14- Crie um programa que peça ao usuário uma senha.
#Se a senha digitada for "1234", mostre Acesso permitido.
#Caso contrário, mostre Senha incorreta.
def verificadorDeSenha():
    senhaDigitada = input("Digite uma senha: ")
    if(senhaDigitada == "1234"):
        print("Acesso permitido")
    else:
        print("Senha incorreta")
        
#15- Escreva um programa que conte de 10 até 1 e depois mostre 
# a mensagem:
#Fim da contagem.
def contadorInverso():
    for number in range(10, 0, -1):
        print(f"{number}")
        if(number == 1):
            print("Fim da contagem.")

#1-	Peça ao usuário uma palavra e mostre quantas vogais ela tem.
def contadorVogais():
    palavra = input("Digite uma palavra: ")

    vogais = ["a", "e", "i", "o", "u"]
    
    contador = 0
    
    for letra in palavra:
        for vogal in vogais:
            if(letra == vogal):
                contador += 1
    
    print(f"A palavra {palavra} tem {contador} vogais.")
#2-	Peça ao usuário para digitar 6 números e mostre 
# apenas os números pares digitados.
def numerosPares():
    contador = 1
    numerosParesDigitados = []
    while contador <= 6:
        numero = int(input(f"Digite o {contador}: "))
        if(numero % 2 == 0):
            numerosParesDigitados.append(numero)
        contador += 1
    if(len(numerosParesDigitados) == 0):
        print("Nenhum número par foi digitado.")
    else:
        print(f"O número de pares digitados foi de: {len(numerosParesDigitados)}")
        print("Os números pares digitados foram:", *numerosParesDigitados)

#3-	Solicite as notas de 4 provas e mostre a média.
def calcularMedia():
    contador = 1
    listaDeNotas = []
    while contador <= 4:
        nota = float(input(f"Digite a {contador} nota: "))
        listaDeNotas.append(nota)
        contador += 1
    mediaAluno = sum(listaDeNotas) / len(listaDeNotas)
    print("As notas do aluno foram:", *listaDeNotas)
    print(f"A média do aluno foi: {mediaAluno}")
#4-	Peça ao usuário uma palavra e mostre ela ao contrário.
def reverterPalavra():
    palavraDigitada = input("Digite uma palavra: ")
    palavraDigitada[::-1]
    print(f"O inverso da palavra {palavraDigitada} é: {palavraDigitada[::-1]}")
#5-	Peça um número ao usuário e diga se ele é múltiplo de 3.
#6-	Peça ao usuário para digitar 3 nomes e mostre todos 
# eles em ordem alfabética.

#DESAFIO
#Peça ao usuário para digitar 4 números 
# e mostre qual é o maior e qual é o menor.