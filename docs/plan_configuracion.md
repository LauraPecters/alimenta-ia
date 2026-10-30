# Plan de gestión de configuración — ALIMENTA-IA

## Elementos de configuración

| SCI | Elemento | Ubicación | Responsable por rol | Línea base |
|---|---|---|---|---|
| SCI-01 | Código | `src/` | Desarrollo | `v1.0.0` / `848e58b` |
| SCI-02 | Pruebas | `tests/` | QA | `v1.0.0` / `848e58b` |
| SCI-03 | Datos sintéticos | `data/` | IA / medición | `v1.0.0` / `848e58b` |
| SCI-04 | Documentación | `docs/` | Configuración | `v1.0.0` / `848e58b` |

**Integrantes del equipo:** Laura Pecters Martínez y Juan Pablo Cepeda. Las responsabilidades técnicas se consignan por rol, sin atribuir cargos individuales no documentados.

## Convenciones

- Rama base: `main`.
- Ramas de trabajo: `feature/GH-01-registro-lotes`, `feature/GH-02-indicadores`, `feature/GH-03-detector-ia`, `feature/app-integrada`, `test/pruebas-integracion` y `docs/cierre-auditoria`.
- Commits descriptivos (`feat`, `test`, `docs`); PR revisado antes de integrar.
- Tickets GH-01, GH-02 y GH-03; trazabilidad detallada en `docs/trazabilidad.md`.

## Historia de integración

- PR #2 (registro), #4 (indicadores), #6 (IA), #7 (app) y #8 (integración/pruebas): revisados y fusionados en ramas de trabajo encadenadas.
- PR #9: consolidación del código y evidencias hacia `main`.
- PR #10: actualización de README y auditoría en `main`.
- **Línea base liberada:** tag anotado `v1.0.0`, commit `848e58b`, publicado como release académica.

Repositorio: https://github.com/LauraPecters/alimenta-ia
Release: https://github.com/LauraPecters/alimenta-ia/releases/tag/v1.0.0

**Control de cambios posteriores:** documentar revisiones mediante un PR nuevo. No reescribir ni mover el tag histórico `v1.0.0`.
