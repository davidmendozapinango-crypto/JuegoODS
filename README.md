# Proyecto Tombola Descripcion

### 🗂️ Estructura del Tablero de Tareas

Para optimizar el desarrollo en Python y la redacción del informe, propongo dividir el trabajo en **4 bloques principales**, asignando a cada integrante un Reto de desarrollo y una sección equivalente del informe escrito.

Como el **Reto 5 (ODS)** es transversal, cada integrante será responsable de aplicar los lineamientos ecológicos dentro de su propio módulo.

---

#### 👤 Bloque A (Sugerido para el Integrante 1)

**Desarrollo: Módulo 1 (Registro de Jugadores) + Base del Reto 5**

* **Programación:** Crear la función para registrar jugadores verificando que la cédula no se repita.


* **Algoritmia:** Implementar la validación de la contraseña mediante un algoritmo recursivo (6 a 10 caracteres, uso de mayúsculas/minúsculas, números, caracteres especiales y sin repetir más de 3 veces).


* **Archivos:** Generar y gestionar el archivo binario `JUGADORES.bin`.


* **Reto 5:** Crear la estructura base del `modulo_ods.py` y diseñar el "Banner de Bienvenida Ecológico" para el registro.


* **Informe:** Redactar la Introducción y la Formulación del Problema.



#### 👤 Bloque B (Sugerido para el Integrante 2)

**Desarrollo: Módulo 2 (Creación de Tarjetas)**

* **Validación:** Leer credenciales desde `JUGADORES.bin` y presentar el menú de ODS.


* **Estructura de Datos:** Desarrollar la lógica para crear las matrices de dimensión $N \times N$ (asegurando que $N$ sea impar y $N \ge 5$).


* **Lógica Visual:** Programar el emparejamiento de la tarjeta principal con su complemento y asignar la secuencia de llenado del Anexo A.


* **Reto 5:** Implementar los códigos de color ANSI y el resumen reflexivo del ODS seleccionado antes de pedir las dimensiones.


* **Informe:** Desarrollar el Análisis del problema y la Carta modular de la aplicación.



#### 👤 Bloque C (Sugerido para el Integrante 3)

**Desarrollo: Módulo 3 (Jugando la Tómbola)**

* **Motor del Juego:** Generar los números aleatorios sin repetición de 1 a $N \times N$ y crear la lógica para marcar las casillas coincidentes en los cartones.


* **Condición de Victoria:** Implementar el escaneo continuo para detectar cuándo una tarjeta completa su figura, mostrando "GANADOR" y calculando los puntos acumulados.


* **Archivos:** Crear y actualizar el archivo binario `JUEGOS.bin` con el historial de cada partida (sin guardar totales ni ganadores, solo los crudos).


* **Reto 5:** Programar la aparición de mensajes alusivos a los ODS durante los sorteos y el mensaje de "misión de sostenibilidad" al ganar.


* **Informe:** Diagramar los Algoritmos (diseño) de los módulos centrales y redactar la Guía de uso (manual de usuario).



#### 👤 Bloque D (Sugerido para el Integrante 4)

**Desarrollo: Módulo 4 (Generando Reportes)**

* **Lectura de Datos:** Extraer información estructurada de `JUGADORES.bin` y `JUEGOS.bin`.


* **Procesamiento:** Programar la lógica para calcular en tiempo real los puntos de las partidas guardadas y determinar ganadores históricos.


* **Salidas (TXT):** Desarrollar los 4 subprogramas de reportes, incluyendo el filtrado por fechas, el Top 5 de jugadores (usando un método de ordenamiento) y el Diagrama de Gantt de los 10 números más frecuentes.


* **Reto 5:** Incorporar encabezados ecologistas en los archivos de texto exportados.


---

### 🚀 Nueva Estructura de Trabajo: Desarrollo en Paralelo

#### Fase 1: Núcleo Lógico (Retos 1, 2 y 3)

*El objetivo es que los cuatro integrantes trabajen simultáneamente usando datos de prueba predefinidos para avanzar rápido.*

* **Integrante 1 (Reto 1):** Lógica de registro, validación recursiva de clave y manejo del archivo `JUGADORES.bin`.


* **Integrante 2 (Reto 2):** Creación de las matrices $N \times N$, lógica de llenado de números y emparejamiento principal/complemento.


* **Integrante 3 (Reto 3):** Motor del juego (sorteo de números sin repetición), lógica de marcado de casillas y detección de "GANADOR".


* **Integrante 4 (Reto 3/Integrador):** Creación de las estructuras de datos auxiliares para el `JUEGOS.bin` y apoyo en la validación de los datos que los otros tres módulos necesitan para comunicarse entre sí.



#### Fase 2: Front-end (Interfaz en Consola) y Reportes

*Una vez terminada la lógica, el equipo se reconfigura para optimizar la visualización y las tareas administrativas.*

* **Front-end (Integrante 1, 2 y 3):**
* **Menú y Registro:** Diseñar el flujo de pantallas del Reto 1, integrando el "Banner de Bienvenida" del Reto 5.


* **Visualización de Cartones:** Implementar los códigos de color ANSI para diferenciar casillas vacías de números y mostrar el ODS seleccionado.


* **Interfaz de Juego:** Lograr que la pantalla se mantenga actualizada, mostrando los números sorteados y los mensajes alusivos a las ODS durante la partida.


* **Reportes (Integrante 4):**
* Diseñar los cuatro subprogramas (estadísticas de jugadores, ranking de números frecuentes con Diagrama de Gantt, detalle de juegos y Top 5 de jugadores).


* Generar los archivos de texto (`.txt`) con los reportes solicitados en los requerimientos.


#### Fase 3: Documentación y Unificación

* **Cada integrante:** Documenta su propio código, algoritmos y diseño según lo que desarrolló en las Fases 1 y 2.


* **Responsable final:** Se encarga de ensamblar el informe escrito (Introducción, formulación, carta modular, programa fuente, etc.).
