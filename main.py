def main():
    # Lista de temperaturas para cada día de la semana
    temperaturas = [25, 27, 26, 24, 28, 26, 27]

    # Imprimir las temperaturas de cada día
    print("Temperaturas de la semana:")
    for i in range(len(temperaturas)):
        print(f"Día {i + 1}: {temperaturas[i]} grados Celsius")

    # Calcular temperatura promedio
    promedio = sum(temperaturas) / len(temperaturas)
    print(f"Temperatura promedio de la semana: {promedio:.2f} grados Celsius")

    # Encontrar la temperatura máxima y mínima
    maxima = max(temperaturas)
    minima = min(temperaturas)
    print(f"Temperatura máxima de la semana: {maxima} grados Celsius")
    print(f"Temperatura mínima de la semana: {minima} grados Celsius")
