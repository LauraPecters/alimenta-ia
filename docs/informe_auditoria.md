# Auditoría y decisión de liberación — ALIMENTA-IA

**Evaluación local:** 12 pruebas automatizadas aprobadas; 36 lotes sintéticos; tasa global 2.931 %. Detector evaluado en 12 lotes etiquetados: 4 VP, 0 FN, 5 FP y 3 VN; recall 100 %, precisión 44.44 %. Alta tasa de falsas alertas: requiere ajuste y evidencia adicional antes de uso fuera del aula. No hay defectos críticos identificados por estas pruebas, pero estas no garantizan ausencia total.

## Checklist del taller

- [x] Requisitos documentados localmente; aprobación formal y versionado Git pendiente.
- [ ] Ramas y commits con convención: pendiente de Git.
- [ ] PR revisados y vinculados a tickets: pendiente de GitHub.
- [x] Pruebas ejecutadas con evidencia: `resultado_pytest.txt`.
- [x] Dependencias declaradas y datos sintéticos reproducibles: `requirements.txt`, CSV, semilla 42; fijar entorno real al ejecutar.
- [x] Proyecto entregado sin credenciales ni datos reales conocidos; verificar en repo antes de publicar.
- [x] Reporte de métricas y análisis incluido.
- [ ] Tag y notas de release coherentes: pendiente de aprobación y GitHub.

**Decisión:** APLAZAR liberación v1.0.0. Razones: no existe PR revisado con aprobación ni historial de integración verificable, requisito RNF-02 y criterio de salida obligatorio. Se entrega incremento académico local funcional y se recomienda cerrar GH-01/02/03 con PR revisados, nuevas pruebas de aceptación y auditoría final antes de etiquetar.

**Retrospectiva:** Funcionaron las validaciones y las pruebas reproducibles. Mejorar trazabilidad remota, cobertura integral de aceptación RF-04/RF-05 y precisión del detector.
