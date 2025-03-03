
# Proyecto: Métodos Numéricos

Este proyecto implementa varios métodos numéricos en Python usando **Tkinter** para la interfaz gráfica.

## 📋 Requisitos previos
Antes de ejecutar el programa, asegúrese de tener instalado:
- **Python 3.10 o superior**
- **pip** (gestor de paquetes de Python)

## 🚀 Instalación y ejecución
### 1️⃣ Clonar el repositorio
Si tiene acceso al repositorio en GitHub, clónelo con:
```sh
 git clone https://github.com/tu-usuario/tu-repositorio.git
 cd tu-repositorio
```
Si recibe el código en un archivo **.zip**, extráigalo en una carpeta y acceda a ella.

### 2️⃣ Crear y activar un entorno virtual
```sh
python3 -m venv env  # Crear entorno virtual
source env/bin/activate  # Activar en Linux/macOS
env\Scripts\activate  # Activar en Windows
```

### 3️⃣ Instalar dependencias
Ejecute:
```sh
pip install -r requirements.txt
```
Esto instalará las siguientes bibliotecas necesarias:
- **tkinter** (incluido en Python)
- **ttkbootstrap** (para mejorar la interfaz gráfica)
- **sympy** (para manipulación simbólica de ecuaciones)
- **pydantic** (validación de datos)
- **numpy** (cálculo numérico)

### 4️⃣ Ejecutar el programa
Para iniciar la aplicación, ejecute:
```sh
python main.py
```

## 🛠 Uso del programa
La interfaz tiene tres pestañas:
1. **Newton-Raphson**: Para encontrar raíces de funciones.
2. **Runge-Kutta**: Para resolver ecuaciones diferenciales.
3. **Euler Mejorado**: Para aproximar soluciones de ecuaciones diferenciales.

Ingrese la ecuación, los valores iniciales y la tolerancia, luego presione el botón "Calcular".

## 🐞 Solución de problemas
- Si hay errores de librerías no encontradas, verifique que haya activado el entorno virtual.
- Si **Tkinter** no está disponible en Linux, instálelo con:
  ```sh
  sudo apt install python3-tk  # Debian/Ubuntu
  sudo pacman -S tk            # Arch Linux
  ```

## 📄 Licencia
Este proyecto es solo para propósitos educativos.

---
**Autor:** Tu Nombre
