class FuncionesEspeciales:
    @staticmethod
    def es_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True

    @staticmethod
    def valor_modal(lista):
        frecuencias = {}
        for elemento in lista:
            frecuencias[elemento] = frecuencias.get(elemento, 0) + 1

        modos = [key for key, value in frecuencias.items() if value == max(frecuencias.values())]
        return modos

    @staticmethod
    def convertir_grados(valor, medida_origen, medida_destino):
        if medida_origen == "C" and medida_destino == "F":
            return valor * 9/5 + 32
        elif medida_origen == "C" and medida_destino == "K":
            return valor + 273.15
        elif medida_origen == "F" and medida_destino == "C":
            return (valor - 32) * 5/9
        elif medida_origen == "F" and medida_destino == "K":
            return (valor + 459.67) * 5/9
        elif medida_origen == "K" and medida_destino == "C":
            return valor - 273.15
        elif medida_origen == "K" and medida_destino == "F":
            return valor * 9/5 - 459.67
        else:
            return valor 

    @staticmethod
    def calcular_factorial(num):
        if isinstance(num, int) and num >= 0:
            resultado = 1
            for i in range(1, num + 1):
                resultado *= i
            return resultado
        else:
            return None 

funciones_especiales = FuncionesEspeciales()

# Verificar primo
print(funciones_especiales.es_primo(7))

# Valor modal
lista_valores = [1, 2, 2, 3, 4, 5, 5, 5]
print(funciones_especiales.valor_modal(lista_valores))

# Conversión de grados
print(funciones_especiales.convertir_grados(25, "C", "F"))

# Factorial
print(funciones_especiales.calcular_factorial(5))