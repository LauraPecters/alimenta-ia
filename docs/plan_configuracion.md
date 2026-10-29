# Plan de gestión de configuración

**SCI:** SCI-01 `src/` (código); SCI-02 `tests/` (pruebas); SCI-03 `data/` (datos sintéticos); SCI-04 `docs/` (documentos). Responsable asignado por rol: desarrollo, QA, IA/medición y configuración, respectivamente. **No se cuenta con nombres de integrantes.**

**Convenciones:** rama base `main`; ramas `feature/GH-01-registro-lotes`, `feature/GH-02-indicadores`, `feature/GH-03-detector-ia`; commits `feat(GH-01): ...`, `test(GH-01): ...`, `docs: ...`; PR enlazadas a cada issue GH-01/02/03 con descripción, pruebas y revisión obligatoria. Línea base inicial propuesta: `main` tras revisión; versión objetivo `v1.0.0` solo después de cumplir criterios de salida.

**Estado real:** proyecto entregado en ZIP, sin remoto GitHub, ramas, PR ni tag remoto comprobables. No afirmar liberación hasta contar con URL, historial, revisiones y pruebas registradas.

**Comandos orientativos tras crear repo remoto:**

```bash
git init
git branch -M main
git add .
git commit -m "chore: estructura inicial ALIMENTA-IA"
git remote add origin URL_DEL_REPOSITORIO
git push -u origin main
# Crear issues y ramas; abrir y revisar PR para GH-01, GH-02 y GH-03.
# Solo cuando la auditoria apruebe liberar:
git tag -a v1.0.0 -m "Primera version educativa"
git push origin v1.0.0
```
