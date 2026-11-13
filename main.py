# main.py
# Importamos las funciones desarrolladas en operaciones.py
import operaciones
import conversion

def ejecutar_programa():
    print("=== SISTEMA DE PRUEBAS DE MÓDULOS ===")

    # Probando la función de saludo
    operaciones.saludar_estudiante("Estudiante TP")

    # Probando la función de suma
    suma_val = operaciones.sumar(15, 25)
    print(f"El resultado de la suma es: {suma_val}")

    # Probando la función de promedio
    prom = operaciones.calcular_promedio(6.0, 5.5, 7.0)
    print(f"El promedio calculado es: {prom}")

    # Probando la función par/impar
    numero_evaluar = 8
    print(f"El número {numero_evaluar} es par?: {operaciones.es_par(numero_evaluar)}")

    # Probando la conversión de temperatura
    temperatura = conversion.celsius_a_fahrenheit(25)
    print(f"25 grados Celsius equivalen a {temperatura} grados Fahrenheit.")

if __name__ == "__main__":
    ejecutar_programa() 