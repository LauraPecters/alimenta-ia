# Matriz de trazabilidad — ALIMENTA-IA

| Requisito | Implementación | Pruebas / evidencia | Cambio GitHub | Estado verificado |
|---|---|---|---|---|
| RF-01 | `src/produccion.py`, `src/app.py` | `test_lote_valido`, `test_codigo_duplicado`, `test_guardar_lote`, `test_rechazar_lote_duplicado` | GH-01, PR #2, PR #9 | Pruebas aprobadas |
| RF-02 | `src/produccion.py` | `test_tasa_normal`, `test_resumen` | GH-01/02, PR #2/#4 | Pruebas aprobadas |
| RF-03 | `src/calidad.py`, `src/app.py` | `test_filtro`, `test_cargar_lotes` | GH-02, PR #4/#9 | Pruebas aprobadas |
| RF-04 | `src/app.py` | `test_mostrar_tablero`; `evidencias/tablero_y_alertas.txt` | PR #7/#8/#9 | Pruebas aprobadas |
| RF-05 | `src/detector_ia.py`, `src/app.py` | `test_detector_longitud_y_binario`, `test_rf05_alertas_y_advertencia`, `evidencias/evaluacion_ia.csv` | GH-03, PR #6/#8/#9 | Pruebas aprobadas; cinco falsos positivos |
| RNF-01 | `src/produccion.py` | `test_negativos`, `test_cero_producidas`, `test_defectuosas_mayor` | PR #2 | Pruebas aprobadas |
| RNF-02 | Convenciones y revisión | PR #2, #4, #6, #7, #8, #9, #10 | GitHub | Siete PR revisados y fusionados; revisar trazabilidad por integración |
| RNF-03 | `requirements.txt`, `data/`, `tests/` | `pytest -q`: 17/17; CSV sintético y semilla 42 | PR #8/#9 | Evidencia reproducible en el entorno revisado |
| RNF-04 | `.gitignore`, CSV de prueba | Búsqueda básica de términos asociados a credenciales | PR #9 | Sin hallazgos sospechosos; no equivale a auditoría exhaustiva |

**Alcance:** trazabilidad funcional y evidencia de pruebas asociadas; no constituye cobertura completa de ramas o líneas de código, ni garantiza ausencia de defectos.
