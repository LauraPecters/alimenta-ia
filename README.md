# ALIMENTA-IA — Taller educativo

Prototipo académico con **datos sintéticos** para registrar lotes, calcular tasas de defectos, consultar por producto, visualizar un tablero textual e identificar anomalías mediante IsolationForest.

**Integrantes:** Laura Pecters Martínez y Juan Pablo Cepeda.
**Repositorio:** https://github.com/LauraPecters/alimenta-ia
**Liberación académica publicada:** [v1.0.0](https://github.com/LauraPecters/alimenta-ia/releases/tag/v1.0.0), commit `848e58b`.

## Instalación y ejecución

Recomendado: Python 3.12.

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m src.app
```

Para registrar un lote desde Python:

```python
from src.produccion import Lote
from src.app import guardar_lote

guardar_lote(Lote('L-100', '2026-10-27', 'Pan', 200, 4, 72.0))
```

**Aviso:** `guardar_lote` escribe en el CSV indicado (por defecto, el dataset de ejemplo). Para conservar intactos los datos de evaluación, usa una copia del CSV al realizar pruebas manuales.

## Funcionalidades y requisitos

- **RF-01:** registro y validación de lotes con identificador único.
- **RF-02:** tasa de defectos por lote.
- **RF-03:** historial y resumen filtrado por producto.
- **RF-04:** tablero textual de indicadores.
- **RF-05:** alertas IA con aviso de carácter orientativo.

La matriz de trazabilidad se encuentra en `docs/trazabilidad.md`.

## Resultados reproducibles

- **17/17 pruebas pytest aprobadas** (100 % de los casos ejecutados).
- **5/5 requisitos funcionales con pruebas asociadas**; esta cifra **no equivale** a cobertura de líneas de código.
- **36 lotes** sintéticos, con **13.888 unidades producidas** y **407 defectuosas**: tasa global **2,931 %**.
- Detector: **24 lotes** de entrenamiento y **12** de evaluación; semilla `42`, contaminación `0.15`.
- Matriz de confusión: VP=4, FN=0, FP=5, VN=3. **Recall: 100 %**; **precisión: 44,44 %**.

La IA genera cinco falsas alertas en el conjunto de evaluación. **No debe utilizarse para decisiones de inocuidad alimentaria** ni reemplaza controles de laboratorio o profesionales.

## Gestión de configuración

Siete Pull Requests revisados y fusionados: [#2](https://github.com/LauraPecters/alimenta-ia/pull/2), [#4](https://github.com/LauraPecters/alimenta-ia/pull/4), [#6](https://github.com/LauraPecters/alimenta-ia/pull/6), [#7](https://github.com/LauraPecters/alimenta-ia/pull/7), [#8](https://github.com/LauraPecters/alimenta-ia/pull/8), [#9](https://github.com/LauraPecters/alimenta-ia/pull/9) y [#10](https://github.com/LauraPecters/alimenta-ia/pull/10). Revisión colaborativa: `JcepedaM`.

Las ramas de los PR #4, #6, #7 y #8 fueron encadenadas; el PR #9 consolidó los módulos en `main`. El PR #10 integró README y auditoría. La liberación `v1.0.0` fue publicada sobre el commit `848e58b`.

**Nota sobre esta documentación:** estas correcciones aclaran el estado posterior a la liberación histórica `v1.0.0`. Deben integrarse mediante un nuevo PR; no modifican retroactivamente esa etiqueta.

## Estructura

- `src/`: código fuente.
- `tests/`: pruebas automatizadas.
- `data/`: dataset sintético.
- `docs/`: requisitos, riesgos, planes, auditoría y trazabilidad.
- `evidencias/`: resultados pytest, indicadores y evaluación de IA.

## Limitaciones

Prototipo educativo sin validación en un entorno industrial real. La verificación básica de secretos no sustituye una auditoría de seguridad completa; tampoco se dispone de una medición verificable del cumplimiento del proyecto sobre un tablero completo de tareas.
