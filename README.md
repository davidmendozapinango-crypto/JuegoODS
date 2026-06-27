# Proyecto Tombola Descripcion
¡Entendido! Organizar un proyecto de esta magnitud mientras cursan otras materias es un verdadero reto, pero con una buena estructura es totalmente manejable. La idea de usar Notion es excelente para este caso; la gestión visual mediante tableros tipo Kanban (Por hacer, En progreso, En revisión, Completado) mantendrá a todo el equipo alineado y evitará cuellos de botella.

Con la entrega final programada para el 12 de julio de 2026, y considerando la presión extra que siempre traen los cierres de semestre con los fuertes exámenes de álgebra lineal y demás materias, la clave aquí es que los cuatro integrantes (David, Natalia, Cameron y tú) puedan trabajar en paralelo la mayor cantidad de tiempo posible.

Aquí tienes una propuesta detallada para estructurar el espacio de trabajo y dividir las responsabilidades.

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


* **Informe:** Compilar el Programa fuente de la aplicación para el documento, unificar el formato del informe y redactar el Resumen de actividades del equipo.



---

### 📅 Cronograma Sugerido (Restan ~2.5 Semanas)

Para que todo fluya sin que colapse con las clases diarias:

* **Días 1 a 4 (Base):** Integrantes 1 y 2 terminan los Módulos 1 y 2. Sin esto, el Módulo 3 no puede arrancar formalmente con datos reales.


* **Días 5 a 10 (Core):** Integrante 3 desarrolla el motor del juego completo. Integrante 4 puede ir programando las funciones de ordenamiento y formatos de impresión usando datos "dummy" (falsos) hasta que el archivo `JUEGOS.bin` esté listo.


* **Días 11 a 14 (Integración):** Todos unen sus códigos. Se ajustan los colores y mensajes del `modulo_ods.py` en conjunto.


* **Días 15 al 17 (Cierre):** Pruebas exhaustivas para prepararse para la defensa grupal y finalización del informe escrito.



Esta estructura les permite avanzar a todos desde el día uno y asegura que la carga del código y del informe esté balanceada.

¿Qué integrante crees que se adapta mejor a la lógica de matrices del Reto 2 y quién prefieres que se encargue del motor del juego en el Reto 3?
