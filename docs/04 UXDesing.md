# Title: Tombola Game - UI UX Pygame Desktop Application
## Summary

>[!Abstract]
>
>
>.

---
## 1. Control de Versiones y Configuración de Ventana

Dado que Pygame renderiza en una ventana nativa del sistema operativo, es fundamental definir el lienzo inicial.

* **Configuración de Pantalla Inicial:**
* **Resolución base:** Ej. `1280 x 720` píxeles (Relación de aspecto 16:9).
* **Modo:** ¿Ventana fija, redimensionable (`pygame.RESIZABLE`) o pantalla completa (`pygame.FULLSCREEN`)?
* **Comportamiento al redimensionar:** Si el usuario estira la ventana, ¿el contenido se escala proporcionalmente (letterboxing/pillarboxing) o se expande el área visible?

* **Enlaces Clave:** Links a mockups visuales, carpeta compartida con assets de audio/gráficos y repositorio de código.

---

## 2. Flujo de Estados de la Aplicación (State Machine)

El flujo de control lógico en Pygame debe implementarse mediante un bucle de eventos que actualice e invoque los módulos de dibujo según la variable estado_actual:

```
			   +---------------+
               |     LOGIN     |<---------------+
               +---------------+                | (Cerrar sesión)
                       | (Autenticación)        |
                       v                        |
               +---------------+                |
               |   DASHBOARD   |----------------+
               +---------------+
                 |           |
    (Configurar) |           | (Ver Reportes)
                 v           v
          +-----------+ +-----------+
          | GAMEPLAY  | |  METRICS  |
          +-----------+ +-----------+
```

### Especificación de Comportamiento por Estado:

1. **LOGIN (Acceso):** Menú para seleccionar la cédula del jugador (cargada desde JUGADORES.bin) y un teclado táctil numérico de botones de 55x55 píxeles en pantalla para ingresar de forma segura la clave de 4 dígitos.
2. **REGISTER (Nuevo Jugador):** Formulario para ingresar Cédula, Nombre Completo, Edad, Género y Estado de Venezuela, serializando sincrónicamente el registro en el archivo de base de datos.
3. **DASHBOARD (Control Central):** Ajuste de dimensiones del cartón (Matriz  : 5, 7, 9 u 11), selección del algoritmo de llenado y elección del ODS temático a resolver.
4. **GAMEPLAY (Tómbola):** Animación del bombo de bolas en el lado izquierdo. Al detenerse el giro, se expulsa una bola física numerada. A la derecha, se renderiza el cartón interactivo para la detección de clics del usuario.
5. **METRICS (Simbiosis Histórica):** Muestra el ranking nacional mediante gráficas de barras e imprime el log descodificado en tiempo real de JUEGOS.bin.

---

## 3. Guía de Estilos Visuales y Gestión de Assets
### Configuración de Ventana y Motor Gráfico
Para asegurar una réplica simétrica perfecta del prototipo web en una aplicación de escritorio nativa, se debe inicializar el motor de Pygame con las siguientes especificaciones físicas de hardware:
- Resolución Fija Base: 1024 x 768 píxeles (Proporción estándar de aspecto 4:3 para pantallas de uso escolar).
- Modo de Ventana: Fijo con buffer doble (pygame.DOUBLEBUF) para evitar parpadeos visuales (tearing) durante las animaciones de la tómbola.
- Tasa de Refresco: Limitada de forma estricta a 60 FPS mediante un reloj del sistema para estabilizar los ciclos de actualización del procesador de hardware:

```Python
reloj = pygame.time.Clock()
dt = reloj.tick(60) / 1000.0  # Delta time para animaciones fluidas basadas en tiempo
```

### Paleta de Colores de la Interfaz (Formato RGB)
 Todo se define mediante tuplas de color RGB y coordenadas de rectángulos (`pygame.Rect`).

Para que los colores en Pygame coincidan exactamente con la estética "eye-safe" (diseñada para el descanso visual estudiantil) del prototipo web, se deben declarar las siguientes constantes en tu archivo de Python:

#### A. Colores Base del Tema (Corporativos)

| Constante Python | Valor RGB (Enteros de 8 bits) |  Hexadecimal | Uso en la Interfaz de Pygame                                         |
| ---------------- | ----------------------------- | ----------- | -------------------------------------------------------------------- |
| COLOR_PINE       | (56, 102, 65)                 | #386641     | Títulos principales, fondo de botones activos y cabeceras de tablas. |
|COLOR_MOSS	|(167, 201, 87)|	#a7c957	|Bordes del cartón, indicador de aciertos y botones de confirmación.|
|COLOR_MINT	|(242, 247, 244)|	#f2f7f4	|Fondo de pantalla principal (Lienzo de descanso ocular).|
|COLOR_CHARCOAL	|(27, 46, 30)|	#1b2e1e	|Textos primarios, leyendas de ODS y contornos de tarjetas.|
|COLOR_WHITE	|(255, 255, 255)|	#ffffff|	Fondo de celdas numéricas de la tómbola de juego.|
|COLOR_SAGE_LIGHT|	(215, 225, 210)|	#d7e1d2|	Bordes de paneles, líneas divisorias y estados desactivados.|
|COLOR_RED_ALERT|	(220, 80, 80)|	#dc5050	|Mensajes de error, botón de borrado de logs y LED de lectura.|
|COLOR_AMBER_LED|	(245, 180, 50)|	#f5b432	|LED indicador de escritura sincrónica en el almacenamiento binario.|


* **Tipografía:** * Fuentes en formato `.ttf` o `.otf` que se empaquetarán con la app (ej. `Ubuntu-Regular.ttf`).
* Tamaños definidos en puntos para los objetos `pygame.font.Font` (ej. Títulos: 32pt, Botones: 24pt, Cuerpo: 16pt).


* **Sprites y Elementos Gráficos:** Formato obligatorio `.png` con canal alfa (transparencia). Especificar el tamaño en píxeles exacto para evitar que Pygame consuma CPU escalando imágenes en tiempo real mediante `pygame.transform.scale`.
#### B. Colores de Identidad para los Objetivos de Desarrollo Sostenible (ODS)

Cada cartón cambiará dinámicamente de color de marca cuando el jugador seleccione un ODS específico en el panel de control. El programador debe mapear la matriz de aciertos con estas constantes:

```python
COLOR_ODS = {
    1:  (229, 36, 59),   # ODS 1: Fin de la Pobreza (Rojo)
    2:  (221, 166, 58),  # ODS 2: Hambre Cero (Mostaza)
    3:  (76, 159, 56),   # ODS 3: Salud y Bienestar (Verde ODS)
    4:  (199, 33, 47),   # ODS 4: Educación de Calidad (Rojo Oscuro)
    5:  (239, 64, 43),   # ODS 5: Igualdad de Género (Naranja)
    6:  (38, 189, 226),  # ODS 6: Agua Limpia y Saneamiento (Celeste)
    7:  (252, 195, 11),  # ODS 7: Energía Asequible (Amarillo ODS)
    8:  (162, 25, 66),   # ODS 8: Trabajo Decente (Vinotinto)
    9:  (243, 111, 33),  # ODS 9: Industria, Innovación (Naranja Brillante)
    10: (221, 19, 103),  # ODS 10: Reducción de Desigualdades (Fucsia)
    11: (249, 157, 37),  # ODS 11: Ciudades Sostenibles (Anaranjado Cálido)
    12: (207, 141, 42),  # ODS 12: Producción y Consumo Responsable (Ocre)
    13: (63, 126, 68),   # ODS 13: Acción por el Clima (Verde Oscuro)
    14: (10, 151, 217),  # ODS 14: Vida Submarina (Azul ODS)
    15: (86, 192, 43),   # ODS 15: Vida de Ecosistemas Terrestres (Verde Claro)
    16: (19, 106, 124),  # ODS 16: Paz, Justicia e Instituciones (Azul Petróleo)
    17: (24, 72, 116),   # ODS 17: Alianzas para Lograr los Objetivos (Azul Marino)
}
```

---

## 4. Especificaciones de Componentes UI Propios (Custom Widgets)

Como Pygame no incluye botones o inputs nativos, se programan desde cero analizando colisiones con `rect.collidepoint(event.pos)`. Debes especificar su diseño y comportamiento:

* **Botones (Buttons):**
* *Normal:* Rectángulo plano o con sprite base.
* *Hover:* Cambio de color de fondo o adición de un borde resaltado cuando el puntero del ratón colisiona con el área.
* *Click:* Desplazamiento del texto 2 píxeles hacia abajo/derecha para simular profundidad física.


* **Campos de Texto (Inputs):**
* *Inactivo:* Borde gris.
* *Activo (Foco):* Borde del color primario y presencia de un cursor parpadeante (`|`). Especificar límite de caracteres y comportamiento si se presionan teclas prohibidas.


* **Barras de Desplazamiento / Sliders (ej. Control de Volumen):**
* Diseño del riel, diseño del marcador de posición (*handle*) y cálculo del valor flotante entre `0.0` y `1.0` según la posición `X` del ratón al arrastrar.



---

## 5. Mapa de Controles (Inputs)

Es vital mapear cómo interactúa el usuario con la aplicación de escritorio a nivel de hardware.

| Acción en la UI | Evento de Ratón (Mouse) | Tecla Alternativa (Teclado) |
| --- | --- | --- |
| Seleccionar / Hacer clic | `pygame.MOUSEBUTTONDOWN` (Izquierdo) | `K_RETURN` (Intro) o `K_SPACE` |
| Navegar entre elementos | Mover cursor sobre elementos | `K_UP` / `K_DOWN` / `K_TAB` |
| Volver atrás / Cancelar | Clic en botón "Atrás" | `K_ESCAPE` |
| Desplazamiento (Scroll) | Rueda del ratón (`BUTTON_WHEELUP/DOWN`) | `K_PAGEUP` / `K_PAGEDOWN` |

---

## 6. Rendimiento y Tasas de Refresco (FPS)

La fluidez de la UI depende del reloj del sistema (`pygame.time.Clock`).

* **FPS Objetivo:** Fijado a `60 FPS` estables (`clock.tick(60)`).
* **Animaciones Basadas en Tiempo:** Si hay transiciones de pantallas (fades) o movimiento de elementos de la interfaz, especificar si se usarán deltas de tiempo (`dt`) para asegurar que la UI se mueva a la misma velocidad independientemente de la potencia del procesador del usuario.

---

## 7. Textos, Contenidos y Mensajes del Sistema

Cada string de texto debe almacenarse en un diccionario o archivo JSON centralizado para facilitar el renderizado y futuras traducciones.

* **Textos del Menú:** "Iniciar", "Configuración", "Salir".
* **Mensajes de Alerta:** ¿Qué ocurre si la app no detecta un archivo de guardado o la resolución no es soportada? Diseñar la caja de diálogo interna que se dibujará sobre la pantalla actual.

---

## 8. Criterios de Accesibilidad en Entornos Gráficos

Al ser un lienzo libre, la accesibilidad debe programarse explícitamente:

* **Indicador Visual de Foco:** Si el usuario decide navegar la interfaz con las flechas del teclado, el elemento seleccionado actualmente debe tener un borde exterior muy visible o un icono indicador al lado (ej. una flecha o un asterisco).
* **Frecuencia de Parpadeo:** Asegurar que los cursores o elementos parpadeantes no superen los 3 Hz para evitar problemas de fotosensibilidad.

---

## 9. Protocolo de Hand-off para Desarrolladores Pygame

Cómo entregar las pantallas al programador de Python.

* **Estructura de Carpetas Sugerida para Assets:**
```text
assets/
├── fonts/      # Archivos .ttf
├── graphics/   # UI Sprites, fondos, iconos (.png)
└── sfx/        # Efectos de sonido para clics o transiciones (.wav)

```


* **Coordenadas Absolutas:** Proveer la posición `(X, Y)` de la esquina superior izquierda de cada elemento importante respecto a la resolución base (`1280x720`).

---