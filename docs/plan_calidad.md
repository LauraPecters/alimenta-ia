# Plan de calidad — ALIMENTA-IA

**Objetivos:** prevenir registros inválidos, asegurar trazabilidad de cambios y comunicar las limitaciones de las alertas IA.

| Objetivo de calidad | Control preventivo | Evidencia | Responsable por rol | Criterio de aceptación |
|---|---|---|---|---|
| Evitar registros inválidos | Validar tipo, fecha, unicidad y rangos | `tests/test_produccion.py`; `tests/test_app.py` | Desarrollo / QA | 100 % de pruebas obligatorias aprobadas |
| Cambios trazables | Issue, ramas, commits y revisión de PR | PR #2, #4, #6, #7, #8, #9 y #10 | Configuración / QA | 100 % de PR integrados revisados |
| IA responsable | Separar entrenamiento/evaluación; semilla fija; aviso de uso | `evidencias/evaluacion_ia.csv`, `tests/test_ia.py`, `tests/test_app.py` | IA / QA | Recall y falsas alertas informados; sin prometer seguridad sanitaria |

## Plan de pruebas

- Validaciones de cantidades, fechas, códigos y tipos; cálculo de tasas.
- Resumen y filtrado por producto.
- Carga, guardado y detección de duplicados en CSV de prueba temporal.
- Tablero textual y advertencia explícita de alertas orientativas.
- Pruebas de regresión: `python -m pytest -q`.

## Evidencias y criterios de salida

- Pruebas **17/17** aprobadas en `main` tras el PR #10.
- **7/7** Pull Requests revisados y fusionados, según las evidencias del equipo en GitHub.
- Dependencias declaradas y datos sintéticos versionados.
- Se publicó la liberación académica **v1.0.0** (commit `848e58b`).
- **Limitación de auditoría:** no se dispone de un registro independiente que demuestre formalmente «cero defectos críticos abiertos». No debe inferirse este criterio solo de que pytest haya pasado. Ver `docs/registro_defectos.md`.

**Decisión:** publicación académica efectuada dentro del alcance sintético, con limitaciones expresas; no constituye aceptación industrial del producto.
