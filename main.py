class CalculadoraReservaEmergencia:
    def __init__(self):
        self.salario = 0.0
        self.despesasfixas = 0.0
        self.despesasvariaveis = 0.0
        self.reserva = 0.0

    def obter_dados(self):
        self.salario = float(input("Quanto você ganha bruto por mês? "))
        self.despesasfixas = float(input("Quanto você gasta por mês em despesas essenciais? "))
        self.despesasvariaveis = float(input("Quanto você gasta por mês em despesas não essenciais? "))

    def calcular_reserva(self):
        despesas = self.despesasfixas + self.despesasvariaveis
        restante = self.salario - despesas
        self.reserva = restante * 6
        print(f"Você teve R${despesas:.2f} de despesas e sobraram R${restante:.2f}.")
        print(f"Você deve ter uma reserva de emergência de R${self.reserva:.2f}.")

# Instancia a classe e chama os métodos
calculadora = CalculadoraReservaEmergencia()
calculadora.obter_dados()
calculadora.calcular_reserva()
