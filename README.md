# 📦 Sistema de Gestión de Inventario Pro

## 📝 Descripción del Sistema
El sistema es una aplicación de consola desarrollada en **Python** diseñada para resolver la necesidad de automatización en el control de stock de una empresa tecnológica. Permite el registro, visualización y análisis financiero de productos de manera eficiente, asegurando la integridad de la información.



---

## 🛠️ Estructuras de Datos Utilizadas

Para este proyecto, se seleccionaron las estructuras de datos nativas de Python que mejor se adaptan a la manipulación de información estructurada:

* **Diccionarios (`dict`):** Se utilizó para representar cada producto como una entidad única, permitiendo almacenar pares clave-valor (ej: `nombre`, `precio`, `stock`).
* **Listas (`list`):** Utilizada como contenedor global para almacenar la colección de diccionarios (productos), facilitando el orden dinámico y el acceso secuencial.
* **Tuplas (`tuple`):** Empleadas para definir categorías fijas o constantes (como tipos de moneda o categorías de productos) que no deben cambiar durante la ejecución del programa.



---

## 🚀 Funcionalidades Implementadas

1.  **Registro con Validación:** Captura de datos mediante `input()` integrada con manejo de excepciones `try-except` para evitar errores de tipo de dato.
2.  **Visualización Formateada:** Implementación de `f-strings` para generar reportes y tablas de datos limpias y fáciles de leer en la consola.
3.  **Cálculo de Activos:** Función modular que recorre las estructuras de datos para calcular y devolver el valor total (financiero) del inventario actual.



---

## ⚙️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Control de Versiones:** Git & GitHub
* **Metodología:** Programación Modular

---

## 🧑‍💻 Instrucciones de Uso
1. Clona este repositorio.
2. Ejecuta el archivo principal:
   ```bash
   python main.py