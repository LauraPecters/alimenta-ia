# Plan de medición y análisis — ALIMENTA-IA

| Ámbito / indicador | Fórmula / método | Fuente | Meta | Responsable |
|---|---|---|---|---|
| Software: aprobación de pruebas | Aprobadas / ejecutadas × 100 | pytest | 100 % | QA |
| Software: RF con pruebas asociadas | RF probados / RF totales × 100 | Matriz de trazabilidad | ≥90 % | QA |
| Proceso: PR revisados | PR aprobados / PR integrados × 100 | GitHub | 100 % | Configuración |
| Proyecto: cumplimiento | Tareas terminadas / comprometidas × 100 | Tablero de tareas | ≥80 % | Líder |
| Producción: tasa global de defectos | Unidades defectuosas / producidas × 100 | CSV sintético | Analizar tendencia | Desarrollo |
| IA: recall | VP / (VP + FN) | CSV sintético etiquetado | Informar valor y límites | IA / QA |

## Resultados

| Indicador | Valor | Interpretación / acción |
|---|---|---|
| Aprobación pytest | **17/17 = 100 %** | Meta cumplida; mantener regresión |
| Requisitos funcionales con pruebas | **5/5 = 100 %** | Trazabilidad completa por asociación; **no es cobertura de código** |
| PR revisados e integrados | **7/7 = 100 %** | PR #2, #4, #6, #7, #8, #9 y #10; mantener revisión por pares |
| Cumplimiento del proyecto | **N/D** | No se verificó un tablero con tareas comprometidas y terminadas; no inventar porcentaje |
| Producción alimentaria simulada | **407/13.888 = 2,9305876 % (≈2,931 %)** | Comparar por lote/producto; no confundir con defectos de software |
| Detección IA | VP=4, FN=0, FP=5, VN=3 | Recall **100 %**; precisión **44,44 %**; nueve alertas, cinco falsas |

## Diseño de la evaluación IA

- Datos sintéticos: **36 lotes**; entrenamiento **24**, evaluación **12**.
- Detector `IsolationForest`, semilla `42`, contaminación `0.15`, 100 estimadores; `StandardScaler` ajustado solo sobre entrenamiento.
- La etiqueta sintética de evaluación se utiliza para calcular la matriz de confusión; no representa validación sanitaria real.
- **Precisión** = VP/(VP+FP) = 4/9 = 44,44 %; **recall** = VP/(VP+FN) = 4/4 = 100 %.
- La alta proporción de falsas alertas exige mejorar el modelo antes de considerar aplicaciones reales.

## Acciones de mejora

1. Reducir falsos positivos mediante análisis de variables/umbrales y evaluación ampliada.
2. Automatizar las pruebas en integración continua (CI), sin afirmar que CI ya está implementada.
3. Crear un tablero con tareas comprometidas/terminadas para poder medir cumplimiento del proyecto.
4. Documentar defectos, su severidad y estado con evidencia verificable.

**Fuentes:** `evidencias/metricas.txt`, `evidencias/evaluacion_ia.csv`, `evidencias/resultado_pytest.txt`, `data/lotes_ejemplo.csv` y PR de GitHub.
