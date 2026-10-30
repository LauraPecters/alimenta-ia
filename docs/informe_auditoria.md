# Auditoría y decisión de liberación — ALIMENTA-IA

## 1. Resultados de la evaluación

El prototipo ALIMENTA-IA fue evaluado mediante pruebas automatizadas y datos sintéticos.

- Pruebas automatizadas: 17 aprobadas de 17 ejecutadas (100 %).
- Requisitos funcionales con pruebas asociadas: 5 de 5 (100 %).
- Lotes sintéticos analizados: 36.
- Unidades producidas: 13.888.
- Unidades defectuosas: 407.
- Tasa global de defectos de producción: 2,931 %.
- Detector de IA: 4 verdaderos positivos, 0 falsos negativos, 5 falsos positivos y 3 verdaderos negativos.
- Recall: 100 %.
- Precisión: 44,44 %.

Las 17 pruebas automatizadas fueron aprobadas después de integrar el proyecto en la rama principal `main`. Esto demuestra que los casos evaluados funcionan correctamente, aunque no garantiza la ausencia total de defectos.

## 2. Checklist de auditoría

- [x] Requisitos documentados y versionados.
- [x] Ramas y commits creados siguiendo convenciones.
- [x] Pull Requests revisados y aprobados por el compañero.
- [x] Pruebas automatizadas ejecutadas: 17/17 aprobadas.
- [x] Dependencias declaradas y datos sintéticos disponibles.
- [ ] Verificación final de ausencia de secretos y datos sensibles.
- [x] Métricas de software, producción e IA documentadas.
- [x] Integración de los cambios a la rama principal `main`.
- [ ] Tag y notas de liberación v1.0.0.

## 3. Gestión de configuración

Se crearon, revisaron y fusionaron seis Pull Requests:

- PR #2: Registro y validación de lotes (GH-01).
- PR #4: Indicadores de producción y calidad (GH-02).
- PR #6: Detector de anomalías mediante IA (GH-03).
- PR #7: Integración de la aplicación.
- PR #8: Pruebas de integración y evidencias.
- PR #9: Integración final del proyecto ALIMENTA-IA a `main`.

Las revisiones fueron realizadas por el colaborador JcepedaM y quedaron registradas en GitHub.

El Pull Request #9 permitió consolidar los módulos, pruebas, datos y documentos en la rama principal.

Después de la integración, se ejecutaron nuevamente las pruebas automatizadas y se obtuvo un resultado de 17 pruebas aprobadas, sin fallos.

El repositorio local quedó sincronizado con `origin/main`, sin cambios pendientes al momento de la verificación.

Repositorio: https://github.com/LauraPecters/alimenta-ia

## 4. Hallazgos

**Fortalezas:**

- Implementación funcional de los módulos principales.
- Cumplimiento de los cinco requisitos funcionales mediante pruebas asociadas.
- Aprobación de las 17 pruebas automatizadas.
- Control de versiones mediante Git y GitHub.
- Trazabilidad de cambios mediante tickets, ramas, commits y Pull Requests.
- Revisión colaborativa del código.
- Documentación de indicadores y resultados de inteligencia artificial.

**Limitaciones:**

- El detector de IA presentó cinco falsos positivos en la evaluación con datos sintéticos.
- Las pruebas automatizadas no garantizan la ausencia de errores en escenarios no evaluados.
- La evaluación del modelo no permite extrapolar sus resultados a procesos industriales reales.
- Está pendiente completar la verificación final de seguridad y publicar la versión etiquetada.

## 5. Decisión de liberación

**Decisión propuesta: APROBAR la liberación académica v1.0.0, condicionada a completar las verificaciones finales.**

**Evidencias verificadas:**

- Los seis Pull Requests fueron integrados.
- Se registraron revisiones y aprobaciones en GitHub.
- La rama `main` contiene los módulos funcionales y las evidencias.
- Se ejecutaron 17 pruebas automatizadas, todas aprobadas.
- Los requisitos funcionales cuentan con pruebas asociadas.
- Se documentaron los resultados de medición y evaluación de IA.

**Limitaciones:** el detector presenta cinco falsos positivos y sus alertas son únicamente orientativas. No debe utilizarse para tomar decisiones de inocuidad alimentaria.

**Pendiente antes de liberar v1.0.0:**

- Verificar la ausencia de secretos y datos sensibles.
- Actualizar el archivo README con el estado definitivo del proyecto.
- Confirmar la coherencia de la documentación con la versión final.
- Crear el tag `v1.0.0` y sus notas de liberación.

Hasta completar estas actividades, la liberación permanece pendiente de aprobación definitiva.

## 6. Retrospectiva

El desarrollo de ALIMENTA-IA permitió aplicar prácticas de aseguramiento de calidad, medición de software y gestión de configuración.

Se logró implementar un prototipo funcional y verificable, con pruebas automatizadas y control de cambios mediante GitHub.

Como oportunidades de mejora se identificaron la necesidad de reducir las falsas alertas del modelo de IA, ampliar los escenarios de pruebas y automatizar la ejecución de pruebas mediante integración continua.

