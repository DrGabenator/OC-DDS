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