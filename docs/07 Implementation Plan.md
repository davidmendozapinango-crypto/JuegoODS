# Plan de Implementación

## 1. Visión general
Define las fases, tareas, responsables y cronograma para desarrollar la aplicación Tómbola ODS cumpliendo con los cinco retos académicos.

## 2. Fases del proyecto

### Fase 1: Análisis y planificación
- Revisar enunciado del proyecto y documentación existente.
- Definir roles del equipo.
- Completar documentación base: objetivos, funcionalidades, stack, UX, flujo, backend y plan.
- Establecer convenciones de código y estructura del proyecto.

**Entregable:** documentación completa en `docs/`.

### Fase 2: Configuración del entorno
- Crear estructura de carpetas del proyecto.
- Configurar repositorio Git.
- Crear `requirements.txt` y `pyproject.toml`.
- Preparar carpeta de assets (imágenes, fuentes, sonidos).

**Entregable:** proyecto base funcional y versionado.

### Fase 3: Módulo de autenticación (Reto 1)
- Implementar registro de jugadores.
- Implementar validación recursiva de claves.
- Implementar inicio de sesión.
- Implementar lectura/escritura de `JUGADORES.bin`.

**Entregable:** jugadores pueden registrarse e iniciar sesión.

### Fase 4: Módulo de cartones (Reto 2)
- Implementar generación de cartones NxN.
- Implementar selección de temática ODS.
- Implementar visualización de secuencia de llenado.
- Implementar autenticación previa para acceder.

**Entregable:** jugador puede crear y visualizar sus cartones.

### Fase 5: Módulo del juego (Reto 3)
- Implementar sorteo de números aleatorios no repetidos.
- Implementar marcado automático de números en cartones.
- Detectar cartón ganador al completar la figura.
- Calcular suma del cartón ganador.
- Guardar cada partida en `JUEGOS.bin`.

**Entregable:** juego funcional de principio a fin.

### Fase 6: Módulo de reportes (Reto 4)
- Implementar listado de jugadores y partidas.
- Implementar gráfico de Gantt de frecuencias.
- Implementar histórico de juegos.
- Implementar TOP 5 de jugadores.
- Exportar reportes a archivos físicos.

**Entregable:** reportes generados correctamente desde los archivos binarios.

### Fase 7: Integración ambiental (Reto 5)
- Integrar imágenes, colores y esloganes de los ODS.
- Mostrar mensajes educativos durante el juego.
- Asegurar que toda la interfaz gráfica esté en español.
- Pulir animaciones y transiciones visuales.

**Entregable:** interfaz gráfica completa y alineada con los ODS.

### Fase 8: Integración frontend con pygame
- Desarrollar pantallas en Pygame.
- Conectar eventos de usuario con la lógica del juego.
- Adaptar la interfaz a diferentes dimensiones de cartón.
- Realizar pruebas de usabilidad.

**Entregable:** aplicación gráfica funcional.

### Fase 9: Pruebas y depuración
- Ejecutar corridas de prueba con diferentes dimensiones.
- Verificar persistencia correcta de datos.
- Revisar validaciones de clave y registros duplicados.
- Corregir errores detectados.

**Entregable:** versión estable sin errores críticos.

### Fase 10: Entrega final
- Redactar informe escrito.
- Elaborar manual de usuario.
- Preparar resumen de actividades por integrante.
- Empaquetar código fuente y documentación.

**Entregable:** producto final listo para defensa y demostración.

## 3. Asignación de responsabilidades

| Módulo | Responsable sugerido |
|---|---|
| Documentación general | Todo el equipo |
| Autenticación y persistencia | Miembro 1 |
| Cartones y figuras ODS | Miembro 2 |
| Lógica del juego y sorteo | Miembro 3 |
| Reportes y estadísticas | Miembro 4 |
| Interfaz gráfica con Pygame | Miembro 5 |
| Pruebas y ajustes finales | Todo el equipo |

## 4. Cronograma sugerido

| Fase | Duración estimada |
|---|---|
| Fase 1 | 3 días |
| Fase 2 | 2 días |
| Fase 3 | 4 días |
| Fase 4 | 4 días |
| Fase 5 | 5 días |
| Fase 6 | 4 días |
| Fase 7 | 4 días |
| Fase 8 | 5 días |
| Fase 9 | 4 días |
| Fase 10 | 4 días |

**Duración total estimada:** aproximadamente 6 semanas.

## 5. Riesgos y mitigación

| Riesgo | Mitigación |
|---|---|
| Pérdida de datos binarios | Realizar copias de respaldo frecuentes |
| Dificultad con validación recursiva | Diseñar y probar el algoritmo por partes |
| Problemas de rendimiento con cartones grandes | Probar con dimensiones máximas desde etapas tempranas |
| Integración tardía de Pygame | Crear prototipos visuales desde la fase 3 |
| Inconsistencias en documentación | Revisar docs al final de cada fase |

## 6. Criterios de finalización
- Los cinco retos funcionan correctamente de forma independiente.
- La aplicación gráfica está en español y es estable.
- Los archivos binarios almacenan y recuperan la información sin errores.
- La documentación está completa, coherente y actualizada.
- El informe escrito, manual de usuario y resumen de actividades están listos.
