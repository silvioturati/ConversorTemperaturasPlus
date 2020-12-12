def celius_to_kelvin(temp_c):
    """
    Função para converter o valor da temperatura de Celsius para Kelvin
    :param temp_c:
    :return: temp_k
    """
    temp_k = temp_c + 273.15
    return temp_k

def celsius_to_fahrenheit(temp_c):
    """
    Funão para converter o valor da temperatura de Celsius para Fahrenheit
    :param temp_c:
    :return: temp_f
    """
    temp_f = (temp_c * (9/5))+32
    return temp_f

def kelvin_to_celsius(temp_k):
    """
    Função para converter o valor da temperatura de Kelvin para Celsius
    :param temp_k:
    :return: temp_c
    """
    temp_c = temp_k - 273.15
    return temp_c

def kelvin_to_fahrenheit(temp_k):
    """
    Função para converter o valor da temperatura de Kelvin para Fahrenheit
    :param temp_k:
    :return: tem_f
    """
    temp_f = ((temp_k - 273.15)*(9/5))+32
    return temp_f

def fahrenheit_to_celsius(temp_f):
    """
    Função para converter o valor da temperatura de Fahrenheit para Celsius
    :param temp_f:
    :return: temp_c
    """
    temp_c = (temp_f - 32)*(5/9)
    return temp_c

def fahrenheit_to_kelvin(temp_f):
    """
    Função para converter o valor da temperatura de Fahrenheit para Kelvin
    :param temp_f:
    :return: temp_k
    """
    temp_k = ((temp_f - 32)*(5/9))+273.15
    return temp_k