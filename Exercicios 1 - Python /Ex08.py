# Faça três algoritimos:
# 1) Transforme a temperatura em Celsius para Fahrenheit.
# 2) Transforme a temperatura em Fahrenheit para Celius.
# 3) Transforme a temperatura em Celsius para Kelvin


def toFahrenheit(temperatura):
    fahrenheit = (temperatura * 1.8) + 32
    print(f"A temperatura {temperatura} °C equivale a {fahrenheit} F")
    print("-------------------------------------------------------------------------")


def toCelsius(temperatura):
    celsius = (temperatura - 32) / 1.8
    print(f"A temperatura {temperatura} F equivale a {celsius:.4f} °C")
    print("-------------------------------------------------------------------------")


def toKelvin(temperatura):
    kelvin = temperatura + 273
    print(f"A temperatura {temperatura} °C equivale a {kelvin}K")
    print("-------------------------------------------------------------------------")


toFahrenheit(32)
toCelsius(0)
toKelvin(0)