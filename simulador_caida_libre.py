import numpy as np
import matplotlib.pyplot as plt

def simular_caida_libre(altura, gravedad=9.81, intervalo=0.1):
    tiempo_total = np.sqrt(2 * altura / gravedad)
    tiempos = np.arange(0, tiempo_total, intervalo)
    alturas = altura - 0.5 * gravedad * tiempos**2
    return tiempos, alturas

def graficar_resultados(tiempos, alturas):
    plt.figure(figsize=(10, 5))
    plt.plot(tiempos, alturas, color='blue')
    plt.title('Simulación de Caída Libre')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Altura (m)')
    plt.axhline(0, color='red', linestyle='--')  # Indicar el nivel del suelo
    plt.grid()
    plt.show()

def menu_principal():
    print("===================================")
    print("      Simulador de Caída Libre")
    print("===================================")
    print("1. Comenzar simulación")
    print("2. Salir")
    print("===================================")

if __name__ == "__main__":
    while True:
        menu_principal()
        opcion = input("Selecciona una opción (1 o 2): ")

        if opcion == '1':
            try:
                altura_inicial = float(input("Ingresa la altura inicial (en metros): "))
                if altura_inicial < 0:
                    print("Error: La altura debe ser positiva. Inténtalo nuevamente.")
                    continue
                tiempos, alturas = simular_caida_libre(altura_inicial)
                graficar_resultados(tiempos, alturas)
            except ValueError:
                print("Error: Por favor, ingresa un número válido.")
        elif opcion == '2':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Error: Opción no válida. Por favor, intenta de nuevo.")
