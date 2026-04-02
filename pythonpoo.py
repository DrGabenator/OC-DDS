class Veiculo:
    def __init__(self, velocidadeMaxima, quilometragem):
        self.velocidadeMaxima = velocidadeMaxima
        self.quilometragem = quilometragem

modeloTeste = Veiculo(200, 1000)
#print(modeloTeste.velocidadeMaxima, modeloTeste.quilometragem)

class Ave:
    def __init__(self, pena, bico, perna, asa):
        self.pena = pena
        self.bico = bico
        self.perna = perna
        self.asa = asa

flamingo = Ave(True, True, "2", "1")

#print(f"O flamingo tem penas? {flamingo.pena}\nO flamingo tem bico? {flamingo.bico}\nQuantas pernas o flamingo tem? {flamingo.perna}\nQuantas asas o flamingo tem? {flamingo.asa}")

class Veiculo:
    def __init__(self, rodas, cor, modelo, tipoDeMotor, seTemMotor, ano):
        self.rodas = rodas
        self.cor = cor
        self.modelo = modelo
        self.tipoDeMotor = tipoDeMotor
        self.seTemMotor = seTemMotor
        self.ano = ano

    def ocupacaoVeiculo(self, bancos=4):
        return f"O veiculo {self.modelo} tem ocupacao para {bancos} passageiros"

ferrari = Veiculo(4, "vermelha", "LaFerrari", "V12 6.3", True, "2018")

print(f"O meu veiculo é uma Ferrari.\nEla tem {ferrari.rodas} rodas\nTem a cor {ferrari.cor}\nÉ do modelo {ferrari.modelo}\nPossui o motor {ferrari.tipoDeMotor}\nE ela possui um motor? {ferrari.seTemMotor}")
print(ferrari.ocupacaoVeiculo())

class Onibus(Veiculo):
    def ocupacaoVeiculo(self, bancos = 50):
        return super().ocupacaoVeiculo(bancos)
onibusEscolar = Onibus(4, "amarelo", "Volvo", "Motor de onibus", True, 2026)
print(f"{onibusEscolar.ocupacaoVeiculo()}")

#fazer classe Bicicleta que herda de Veiculo
