"""
Programa em Python para converter temperaturas
"""

import helpers
import sys

if __name__ == '__main__':
    print("********* Conversor de temperaturas *********")
    print("Digite SAIR a qualquer momento para finalizar")
    while True:
        ###bloco para receber e testar o valor da temperatura
        while True:
            try:
                temperatura_digitada = input("\nDigite a temperatura: ")
                if temperatura_digitada.lower() == "sair":
                    sys.exit("Obrigado por usar o sistema, até a próxima!")
                else:
                    temperatura = float(temperatura_digitada)
                    break
            except ValueError:
                print("Você precisa digitar um número ou a palavra SAIR")

        ###bloco para receber, testar a unidade de medida e retornar os valores
        while True:
            unidade = input("Digite a unidade de medida (C, K ou F): ")
            if unidade.lower() == "sair":
                sys.exit("Obrigado por usar o sistema, até a próxima!")
            elif unidade.lower() == "c":
                print(f"\nVocê digitou {temperatura}º{unidade.upper()}")
                print(f"O mesmo que {helpers.celius_to_kelvin(temperatura)}ºK (Kelvin).")
                print(f"O mesmo que {helpers.celsius_to_fahrenheit(temperatura)}ºF (Fahrenheit).")
                break
            elif unidade.lower() == "k":
                print(f"\nVocê digitou {temperatura}º{unidade.upper()}")
                print(f"O mesmo que {helpers.kelvin_to_celsius(temperatura)}ºC (Celsius).")
                print(f"O mesmo que {helpers.kelvin_to_fahrenheit(temperatura)}ºF (Fahrenheit).")
                break
            elif unidade.lower() == "f":
                print(f"\nVocê digitou {temperatura}º{unidade.upper()}")
                print(f"O mesmo que {helpers.fahrenheit_to_celsius(temperatura)}ºC (Celsius).")
                print(f"O mesmo que {helpers.fahrenheit_to_kelvin(temperatura)}ºK (Kelvin).")
                break
            else:
                print("Você precisa digitar uma das unidades C para Celsius ou K para Kelvin ou F para Fahrenheit")