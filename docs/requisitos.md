# Requisitos y criterios — ALIMENTA-IA

| ID | Criterio de aceptación / verificación |
|---|---|
| RF-01 | Registrar identificador único, fecha ISO, producto, unidades producidas y defectuosas; validación de entradas. `test_lote_valido`, `test_codigo_duplicado`. |
| RF-02 | Tasa de defectos = defectuosas / producidas × 100; 200 y 6 produce 3 %. `test_tasa_normal`. |
| RF-03 | Consultar historial de lotes y filtrar por producto: `cargar_lotes` y `resumen(lotes, producto)`. `test_filtro`. |
| RF-04 | Tablero textual de conteo y tasa global por producto: `mostrar_tablero`. Evidencia en `evidencias/tablero_y_alertas.txt`. |
| RF-05 | Detector IsolationForest con advertencia de uso orientativo. `test_detector_longitud_y_binario`; evaluación en CSV. |
| RNF-01 | No aceptar cantidades negativas, cero producidas o defectuosas mayores. Pruebas de validación. |
| RNF-02 | Cada cambio integrado debe tener ticket, PR y pruebas asociadas. **Pendiente de GitHub**; no verificado. |
| RNF-03 | Dependencias declaradas en requirements.txt, datos sintéticos versionables y semilla 42; ejecución repetible. |
| RNF-04 | .gitignore y muestra sin datos reales ni credenciales; revisión local, verificar de nuevo antes de publicar. |

## Riesgos priorizados

Escala 1 a 5, producto P×I, valoraciones de planificación (no medición):

| Riesgo | P | I | Prioridad | Mitigación |
|---|---:|---:|---:|---|
| Aceptación de cantidades inválidas | 3 | 5 | 15 | Validación y pruebas negativas |
| Cambios sin revisión o trazabilidad GitHub | 4 | 4 | 16 | Issue/PR obligatorios, revisión antes de integrar |
| Falsos positivos de detector de IA | 4 | 4 | 16 | Separación de datos, matriz de confusión y aviso orientativo |
