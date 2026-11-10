
# operaciones.py

def saludar_estudiante(nombre):
    """Funcion que recibe un nombre e imprime un saludo."""
    print(f"Hola {nombre}! Bienvenido al taller de programación.")


def sumar(a, b):
    """Funcion que retorna la suma de dos números."""
    resultado = a + b
    return resultado


def calcular_promedio(nota1, nota2, nota3):
    """Calcula y retorna el promedio de tres notas."""
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio


def es_par(numero):
    """Retorna True si el número es par, o False si es impar."""
    return numero % 2 == 0
