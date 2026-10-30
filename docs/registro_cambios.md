# Registro de cambios e integración — ALIMENTA-IA

| Ticket | Motivo | SCI afectados | Riesgo / impacto | Decisión y resultado | PR / evidencia |
|---|---|---|---|---|---|
| GH-01 | Registro/validación | `src/produccion.py`, `tests/test_produccion.py` | Alto: integridad de datos | Integrado y revisado | [PR #2](https://github.com/LauraPecters/alimenta-ia/pull/2); 8 pruebas de validación |
| GH-02 | Indicadores | `src/calidad.py`, `tests/test_calidad.py` | Medio: cálculo y reporte | Integrado y revisado | [PR #4](https://github.com/LauraPecters/alimenta-ia/pull/4); 3 pruebas |
| GH-03 | Detección IA | `src/detector_ia.py`, `tests/test_ia.py` | Alto: falsas alertas | Integrado; limitado a uso orientativo | [PR #6](https://github.com/LauraPecters/alimenta-ia/pull/6); `evaluacion_ia.csv` |
| Integración | App y tablero | `src/app.py`, `tests/test_app.py` | Medio: integración | Integrado y revisado | [PR #7](https://github.com/LauraPecters/alimenta-ia/pull/7) y [PR #8](https://github.com/LauraPecters/alimenta-ia/pull/8) |
| Consolidación | Unir módulos a `main` | Código, pruebas, evidencias | Alto: entrega incompleta | Integrado y revisado | [PR #9](https://github.com/LauraPecters/alimenta-ia/pull/9) |
| Cierre documental | README y auditoría | `README.md`, `docs/informe_auditoria.md` | Medio: coherencia | Integrado y revisado | [PR #10](https://github.com/LauraPecters/alimenta-ia/pull/10) |

**Nota:** las integraciones iniciales se hicieron sobre ramas encadenadas; la incorporación definitiva de todos los módulos a `main` se efectuó mediante el PR #9. La release académica `v1.0.0` apunta al commit `848e58b`.
