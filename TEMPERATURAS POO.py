class SemanaTemperaturas:
    def __init__(self, temperaturas):
        self.temperaturas = temperaturas

    def imprimir_temperaturas(self):
        print("Temperaturas de la semana:")
        for i in range(len(self.temperaturas)):
            print(f"Día {i + 1}: {self.temperaturas[i]} grados Celsius")

    def temperatura_promedio(self):
        promedio = sum(self.temperaturas) / len(self.temperaturas)
        return promedio

    def temperatura_maxima(self):
        return max(self.temperaturas)

    def temperatura_minima(self):
        return min(self.temperaturas)


def main():
    # Lista de temperaturas para cada día de la semana
    temperaturas_semana = [25, 27, 26, 24, 28, 26, 27]

    # Crear objeto de la clase SemanaTemperaturas
    semana = SemanaTemperaturas(temperaturas_semana)

    # Utilizar los métodos de la clase para obtener resultados
    semana.imprimir_temperaturas()
    print(f"Temperatura promedio de la semana: {semana.temperatura_promedio():.2f} grados Celsius")
    print(f"Temperatura máxima de la semana: {semana.temperatura_maxima()} grados Celsius")
    print(f"Temperatura mínima de la semana: {semana.temperatura_minima()} grados Celsius")
