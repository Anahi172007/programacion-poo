class DiaClima:
    def __init__(self, temperatura):
        self.temperatura = temperatura

class SemanaClima:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, temperatura):
        self.dias.append(DiaClima(temperatura))

    def calcular_promedio(self):
        total = sum(dia.temperatura for dia in self.dias)
        return total / len(self.dias) if self.dias else 0

def main():
    print("=== Promedio Semanal del Clima (POO - Sin input) ===")
    semana = SemanaClima()

    # Lista simulada de temperaturas
    temperaturas = [22.0, 23.5, 21.0, 24.5, 25.0, 22.5, 23.0]

    for i, temp in enumerate(temperaturas):
        print(f"Día {i+1}: {temp}°C")
        semana.agregar_dia(temp)

    promedio = semana.calcular_promedio()
    print(f"\nPromedio semanal: {promedio:.2f}°C")

if __name__ == "__main__":
    main()