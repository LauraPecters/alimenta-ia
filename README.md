# ALIMENTA-IA — taller educativo

Prototipo con **datos sintéticos** para registro de lotes, cálculo de tasa de defectos, consulta por producto, tablero textual e identificación de anomalías orientativas.

## Ejecutar

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m src.app
```

Para registrar un lote desde Python: `guardar_lote(Lote('L-100','2026-10-27','Pan',200,4,72.0))` (importar de `src.app` y `src.produccion`). El programa valida identificadores únicos, fechas, cantidades y temperaturas. El tablero muestra historial filtrable desde `resumen(lotes, producto='Pan')`.

## Alcance y limitaciones

Las alertas de IsolationForest son *orientativas*; **no** sustituyen evaluación de laboratorio, inocuidad ni profesionales responsables. Datos y etiquetas simulados. La separación para la evaluación es 24 lotes de entrenamiento y 12 de prueba. La etiqueta simulada es una referencia experimental, no verdad clínica o industrial.

## Estado GitHub

No se ha creado ni conectado un repositorio remoto. Issues, PR, revisión, URL y tag remoto requieren ejecución real por el equipo; no se presentan como completados.

## Estructura

`src/`, `tests/`, `data/`, `docs/`, `evidencias/`.
