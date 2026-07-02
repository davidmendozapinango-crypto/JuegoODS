# JuegoODS - Tómbola de los Objetivos de Desarrollo Sostenible

## 1. Título y Descripción

**JuegoODS** es una aplicación de escritorio desarrollada en Python con Pygame que implementa un juego de tómbola (bingo) educativo inspirado en los 17 Objetivos de Desarrollo Sostenible (ODS) de las Naciones Unidas. El proyecto fue creado como trabajo académico para la asignatura de Algoritmos y Programación de la Universidad Católica Andrés Bello.

El juego permite registrar jugadores, generar cartones temáticos por ODS, realizar sorteos automáticos o manuales, detectar cartones ganadores, guardar el historial de partidas en archivos binarios y generar reportes en texto plano. Toda la interfaz gráfica está en español.

## 2. Características Principales

- **Registro e inicio de sesión de jugadores** con validación recursiva de claves de acceso.
- **Gestión de perfil**: visualizar, actualizar y eliminar la cuenta del jugador.
- **Generación de cartones N×N** con números únicos y temática de ODS (dimensiones impares entre 5 y 15).
- **Juego de tómbola** con sorteo de números aleatorios no repetidos y marcado automático.
- **Detección de ganador** mediante máscaras de figura configurables.
- **Persistencia en archivos binarios** (`JUGADORES.bin` y `JUEGOS.bin`).
- **Reportes exportables** en texto plano: resumen de jugadores, frecuencia de números, histórico de juegos y TOP 5 de puntajes.
- **Interfaz gráfica en español** integrada con colores, esloganes e imágenes de los ODS.
- **Pruebas automatizadas** con pytest.

## 3. Prerrequisitos e Instalación

### Prerrequisitos

- Python 3.9 o superior.
- pip (administrador de paquetes de Python).

### Instalación

1. Clona o descarga el repositorio en tu equipo.
2. Abre una terminal en la carpeta raíz del proyecto.
3. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate        # Windows
   source .venv/bin/activate     # Linux/macOS
   ```

4. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## 4. Instrucciones de Ejecución

Para iniciar la aplicación gráfica:

```bash
python src/main.py
```

Para ejecutar el conjunto de pruebas:

```bash
python -m pytest
```

Para ejecutar un módulo de pruebas específico:

```bash
python -m pytest tests/test_auth.py
```

## 5. Controles y Uso de la Aplicación

### Pantalla de bienvenida

- **Registrarse**: crea una nueva cuenta de jugador.
- **Iniciar sesión**: accede con cédula y clave.
- **Salir**: cierra la aplicación.

### Registro

Completa los campos solicitados:

- Cédula
- Nombre completo
- Sexo (`m` o `f`)
- Fecha de nacimiento (`YYYY-MM-DD`)
- Estado (código de 3 caracteres, por ejemplo `CCS`)
- Clave de acceso (6-10 caracteres, al menos una mayúscula, una minúscula, un número y un carácter especial `*`, `=`, `%` o `_`; máximo 3 caracteres iguales consecutivos)

Usa `Tab` para moverte entre campos y `Enter` para confirmar.

### Menú principal

- **Jugar**: genera cartones e inicia una partida.
- **Perfil**: consulta, edita o elimina tu perfil.
- **Reportes**: genera archivos de reporte.
- **Cerrar sesión**: vuelve a la pantalla de bienvenida.

### Creación de cartones

- Ingresa una dimensión impar entre 5 y 15.
- Selecciona uno de los 17 ODS con las flechas `←` y `→`.
- Presiona `Espacio` para continuar.

### Durante el juego

- Presiona `M` para modo manual (sorteo con `Espacio`).
- Presiona `1` para sorteo automático cada 1 segundo.
- Presiona `2` para sorteo automático cada 2 segundos.
- Presiona `Enter` al finalizar para ver los resultados.
- Presiona `Esc` para volver al menú.

### Reportes

- Selecciona el tipo de reporte con `←` y `→`.
- Ingresa opcionalmente un rango de fechas (`YYYY-MM-DD`).
- Presiona `Espacio` para generar el archivo `.txt`.

## 6. Estructura del Proyecto

```text
JuegoODS/
├── src/
│   ├── main.py              # Punto de entrada de la aplicación
│   ├── config.py            # Constantes y configuración
│   ├── common/
│   │   └── errors.py        # Excepciones compartidas
│   ├── auth/
│   │   ├── player.py        # Modelo de jugador
│   │   ├── registration.py  # Registro
│   │   ├── login.py         # Autenticación
│   │   ├── profile.py       # Gestión de perfil
│   │   └── validator.py     # Validador recursivo de claves
│   ├── core/
│   │   ├── card.py          # Generación de cartones
│   │   ├── game.py          # Lógica del juego
│   │   └── points.py        # Cálculo de puntos
│   ├── persistence/
│   │   ├── players.py       # Persistencia de jugadores
│   │   └── games.py         # Persistencia de juegos
│   ├── reports/
│   │   ├── summary.py       # Reporte de jugadores
│   │   ├── gantt.py         # Frecuencia de números
│   │   ├── logs.py          # Histórico de juegos
│   │   ├── ranking.py       # TOP 5
│   │   └── export.py        # Exportación a texto plano
│   ├── ui/
│   │   ├── app.py           # Bucle principal de Pygame
│   │   ├── screens.py       # Pantallas de la aplicación
│   │   ├── renderer.py      # Renderizado de cartones y textos
│   │   ├── assets.py        # Carga de imágenes y fuentes
│   │   └── messages.py      # Catálogo de mensajes en español
│   └── ods/
│       ├── data.py          # Catálogo de ODS
│       └── messages.py      # Mensajes educativos rotativos
├── tests/                   # Pruebas con pytest
├── assets/                  # Imágenes y fuentes
├── data/                    # Archivos binarios de runtime
├── docs/                    # Documentación del proyecto
├── specs/                   # Especificaciones y planificación
├── requirements.txt         # Dependencias
├── pyproject.toml           # Configuración del proyecto
└── README.md                # Este archivo
```

## 7. Créditos y Licencia

**Autores**: David Mendoza, Albert Gonzales, Cameron Montoya, Natalia Azocar.

**Inspiración**: Objetivos de Desarrollo Sostenible de las Naciones Unidas.

**Tecnologías utilizadas**:

- Python 3.9+
- Pygame 2.5+
- pytest

**Licencia**: Este proyecto es de uso educativo. Consulta a los autores antes de redistribuir o utilizar con fines comerciales.
