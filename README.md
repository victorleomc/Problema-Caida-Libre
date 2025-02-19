# Simulador de Caída Libre

Este es un programa en Python que simula la caída libre de un objeto bajo la influencia de la gravedad. 
Permite al usuario ingresar la altura inicial desde la cual el objeto es soltado y visualiza la trayectoria de su caída.

## Características

- Simulación de la caída libre de un objeto.
- Gráfica de la altura en función del tiempo.
- Interfaz de línea de comandos sencilla.

## Requisitos

- Python 3.x
- NumPy
- Matplotlib

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/victorleomc/Problema-Caida-Libre/
   ```

2. Navega a la carpeta del repositorio:
   ```
   cd Problema-Caida-Libre
   ```

3. (Opcional) Crea un entorno virtual y activa el entorno:
   ```
   python -m venv venv
   source venv/bin/activate  # En Linux/Mac
   venv\Scripts\activate     # En Windows
   ```

4. Instala las dependencias:
   ```
   pip install numpy matplotlib
   ```

## Uso

1. Ejecuta el script:
   ```
   python simulador_caida_libre.py
   ```

2. Selecciona la opción para iniciar la simulación.
3. Ingresa la altura inicial desde la cual quieres simular la caída.

## Ejemplo de salida

```
===================================
      Simulador de Caída Libre
===================================
1. Comenzar simulación
2. Salir
===================================
Selecciona una opción (1 o 2): 1
Ingresa la altura inicial (en metros): 10
```

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de enviar un pull request o abrir un issue.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
