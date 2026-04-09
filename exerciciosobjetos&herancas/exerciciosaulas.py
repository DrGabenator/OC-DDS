#class Veiculo:
#    def __init__(self, marca, modelo, ano):
#        self.marca = marca
#        self.modelo = modelo
#        self.ano = ano

#    def exibir_detalhes(self):
#        print(f"A marca do Veículo é: {self.marca}\nO modelo do veículo é: {self.modelo}\nO ano do veículo é: {self.ano}")

#civic = Veiculo(marca="Honda", modelo="Civic", ano="2025")

#civic.exibir_detalhes()

#class Cachorro:
#    def __init__(self, nome, raca):
#        self.nome = nome
#        self.raca = raca

#    def latir(self):
#        print(f"{self.nome}: Au au!")

#rex = Cachorro(nome = "Rex", raca = "Husky")

#rex.latir()

#class ContaBancaria:
#    def __init__(self, titular, saldo = 0.0):
#        self.titular = titular
#        self.saldo = saldo

#    def depositar(self, valor):
#        self.saldo += valor

#    def mostrar_saldo(self):
#        print(f"O titular: {self.titular} possui saldo de R${self.saldo}")

#minhaConta = ContaBancaria(titular="Gabriel Santos")

#minhaConta.depositar(50.00)

#minhaConta.mostrar_saldo()

#class Retangulo:
#    def __init__(self, base: int, altura: int):
#        self.base = base
#        self.altura = altura

#    def calcular_area(self):
#        return self.base * self.altura
    
#meuRetangulo = Retangulo(base=5, altura=10)

#print(f"A área do retângulo é: {meuRetangulo.calcular_area()}")

#class Aluno:
#    def __init__(self, nome: str, nota1: float, nota2: float):
#        self.nome = nome
#        self.nota1 = nota1
#        self.nota2 = nota2
    
#    def calcular_media(self):
#        return (self.nota1 + self.nota2) / 2
    
#    def mostrar_situacao(self):
#        if(self.calcular_media() >= 6 and self.calcular_media() <= 10):
#            print(f"O aluno {self.nome} está aprovado com média {self.calcular_media()}")
#        elif(self.calcular_media() < 6 and self.calcular_media() >= 0):
#            print(f"O aluno {self.nome} está reprovado com média {self.calcular_media()}")
#        else:
#            print(f"A média é inválida!")

#meuAluno = Aluno("Gabriel Santos", 7.5, 4.5)

#meuAluno.mostrar_situacao()

#class Livro:
#    def __init__(self, titulo, autor, paginas: int):
#        self.titulo = titulo
#        self.autor = autor
#        self.paginas = paginas

#    def ler_livro(self):
#        print(f"Você está lendo o livro {self.titulo}, do autor {self.autor} e ele possui {self.paginas} páginas.")

#asCronicasDeGeloEFogo = Livro("As Crônicas de Gelo e Fogo", "George R. R. Martin", 835)

#asCronicasDeGeloEFogo.ler_livro()

#class Produto:
#    def __init__(self, nome: str, preco: float, quantidade_em_estoque: int):
#        self.nome = nome
#        self.preco = preco
#        self.quantidade_em_estoque = quantidade_em_estoque

#    def calcular_valor_total(self):
#        return self.quantidade_em_estoque * self.preco
    
#teclado = Produto("Teclado", 100.00, 5)

#print(f"Nós temos um estoque de {teclado.quantidade_em_estoque} de {teclado.nome} e o preço unitário de cada é: R${teclado.preco}\nO valor total em estoque desse produto é de: R${teclado.calcular_valor_total()}")

#class Calculadora:
#    def somar(a: int, b: int):
#        return a + b

#    def subtrair(a: int, b: int):
#        return a - b
    
#    def multiplicar(a: int, b: int):
#        return a * b
    
#    def divisao(a: int, b: int):
#        if(b == 0):
#            return "Não é possível dividir por 0"
#        else:
#            return a / b
        
#print(f"Soma: {Calculadora.somar(10, 5)}")
#print(f"Subtração: {Calculadora.subtrair(50, 15)}")
#print(f"Multiplicação: {Calculadora.multiplicar(27, 43)}")
#print(f"Divisão: {Calculadora.divisao(100, 2)}")

#class Animal:
#    def __init__(self, nome):
#        self.nome = nome

#    def emitir_som(self):
#        print("Barulho de animal")

#class Gato(Animal):
#    def emitir_som(self):
#        print(f"{self.nome} diz: Miau!")

#gatinho = Gato("Sr Bigodes")

#gatinho.emitir_som()

#animalQualquer = Animal("Sr Animal")

#animalQualquer.emitir_som()

#class Veiculo:
#    def __init__(self, velocidade):
#        self.velocidade = velocidade

#    def mostrar_velocidade(self):
#        print(f"O veículo está com velocidade: {self.velocidade}km/h")

#class Carro(Veiculo):
#    def abrir_porta(self):
#        print(f"Abrindo porta do carro...")

#ferrari = Carro(300)

#ferrari.mostrar_velocidade()
#ferrari.abrir_porta()

#class Funcionario:
#    def __init__(self, salario):
#        self.salario = salario

#    def calcular_bonus(self, bonusSalarial = 0.1, papel = "Funcionário"):
#        bonus = self.salario * bonusSalarial
#        print(f"O bônus do {papel} com salário R${self.salario}, é de R${bonus}")

#class Gerente(Funcionario):
#    def calcular_bonus(self):
#        return super().calcular_bonus(bonusSalarial=0.2, papel = "Gerente")
    
#funcionario = Funcionario(2500)
#print(f"Segue abaixo as informações do Funcionário!")
#funcionario.calcular_bonus()

#gerente = Gerente(5000)
#print(f"Segue abaixo as informações do Gerente!")
#gerente.calcular_bonus()

#class Forma:
#    def area(self):
#        return 0
    
#class Quadrado(Forma):
#    def __init__(self, lado):
#        self.lado = lado
    
#    def area(self):
#        return self.lado * self.lado
    
#q1 = Quadrado(5)
#q2 = Quadrado(10)
#q3 = Quadrado(6)

#print(f"O quadrado 1 tem lados {q1.lado} e área total {q1.area()}")
#print(f"O quadrado 2 tem lados {q2.lado} e área total {q2.area()}")
#print(f"O quadrado 3 tem lados {q3.lado} e área total {q3.area()}")

#class Conta:
#    def __init__(self, saldo):
#        self.saldo = saldo
    
#    def sacar(self, valor):
#        if valor <= self.saldo:
#            self.saldo -= valor
#            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
#        else:
#            print("Saldo insuficiente!")
    
#class ContaCorrente(Conta):
#    def __init__(self, limite, saldo):
#        super().__init__(saldo)
#        self.limite = limite

#    def sacar(self, valor):
#        if valor <= (self.saldo + self.limite):
#            self.saldo -= valor
#            print(f"Saque de {valor} realizado. Saldo atual: {self.saldo}")
#        else:
#            print("Saldo + limite insuficientes!")

# Conta corrente com limite
#cc = ContaCorrente(100, 50)
#cc.sacar(120)  # OK (usa limite)

#class Pessoa:
#    def __init__(self, nome = str, idade = int):
#        self.nome = nome
#        self.idade = idade

#    def apresentar(self):
#        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

#class Aluno(Pessoa):
#    def __init__(self, nome = str, idade = int, nota = float):
#        super().__init__(nome, idade)
#        self.nota = nota

#    def apresentar(self):
#        print(f"Meu nome é {self.nome}, tenho {self.idade} anos e tenho nota {self.nota} em Desenvolvimento de Sistemas.")

#aluno = Aluno("Gabriel", 32, 8.5)

#aluno.apresentar()

#class Dispositivo:
#    def ligar(self):
#        print(f"Ligando dispositivo...")

#class Celular(Dispositivo):
#    def tirar_foto(self):
#        print(f"Tirando foto...")

#s26ultra = Celular()

#s26ultra.ligar()

#s26ultra.tirar_foto()

#class Produto:
#    def __init__(self, nome, preco):
#        self.nome = nome
#        self.preco = preco

#class ProdutoDesconto(Produto):
#    def __init__(self, nome, preco):
#        super().__init__(nome, preco)

#    def aplicar_desconto(self, percentual):
#        print(f"Produto é {self.nome} com preço original de R${self.preco:.2f}")
#        desconto = self.preco * (percentual / 100)
#        self.preco -= desconto
#        print(f"Desconto de {percentual}% aplicado -> R${desconto:.2f} de desconto\nNovo preço é de R${self.preco:.2f}")

#produtoComDesconto = ProdutoDesconto("Celular", 3149)
#produtoComDesconto.aplicar_desconto(28)

#class Animal:
#    def comer(self):
#        print(f"Comendo...")

#class Gato(Animal):
#    def comer(self):

#        print(f"Comendo ração...")

#srBigodes = Gato()

#srBigodes.comer()

#class Transporte:
#    def mover(self):
#        print(f"Movendo-se...")

#class Onibus(Transporte):
#    def mover(self):
#        print(f"Andando na estrada...")

#meuOnibus = Onibus()

#meuOnibus.mover()
