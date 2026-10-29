\# Auditoría y decisión de liberación — ALIMENTA-IA



\## 1. Resultados de la evaluación



El prototipo ALIMENTA-IA fue evaluado mediante pruebas automatizadas y datos sintéticos.



\- Pruebas automatizadas: 17 aprobadas de 17 ejecutadas (100 %).

\- Requisitos funcionales con pruebas asociadas: 5 de 5 (100 %).

\- Lotes sintéticos analizados: 36.

\- Tasa global de defectos de producción: 2,931 %.

\- Detector de IA: 4 verdaderos positivos, 0 falsos negativos, 5 falsos positivos y 3 verdaderos negativos.

\- Recall: 100 %.

\- Precisión: 44,44 %.



Las pruebas existentes fueron aprobadas, aunque esto no garantiza la ausencia de defectos no detectados.



\## 2. Checklist de auditoría



\- \[x] Requisitos documentados y versionados.

\- \[x] Ramas y commits creados siguiendo convenciones.

\- \[ ] Pull Requests revisados y aprobados por el compañero.

\- \[x] Pruebas automatizadas ejecutadas: 17/17 aprobadas.

\- \[x] Dependencias declaradas y datos sintéticos disponibles.

\- \[ ] Verificación final de ausencia de secretos y datos sensibles.

\- \[x] Métricas de software, producción e IA documentadas.

\- \[ ] Integración de los cambios a la rama principal.

\- \[ ] Tag y notas de liberación v1.0.0.



\## 3. Gestión de configuración



Se crearon cinco Pull Requests:



\- PR #2: Registro y validación de lotes (GH-01).

\- PR #4: Indicadores de producción y calidad (GH-02).

\- PR #6: Detector de anomalías mediante IA (GH-03).

\- PR #7: Integración de la aplicación.

\- PR #8: Pruebas de integración.



Los Pull Requests permanecen pendientes de revisión formal e integración.



\## 4. Hallazgos



\*\*Fortalezas:\*\* se implementaron los módulos principales, se ejecutaron correctamente las pruebas automatizadas y se estableció trazabilidad mediante ramas, commits y Pull Requests.



\*\*Limitaciones:\*\* falta completar las revisiones independientes y la integración. Además, el detector de IA presenta cinco falsas alertas en la evaluación sintética.



\## 5. Decisión de liberación



\*\*Decisión: APLAZAR la versión v1.0.0.\*\*



Aunque el prototipo funciona y las pruebas ejecutadas fueron aprobadas, todavía no se cumplen todos los criterios de liberación establecidos en el taller.



Antes de liberar deben completarse las revisiones, integrar los cambios, ejecutar nuevamente las pruebas y verificar el cumplimiento del checklist.



\## 6. Retrospectiva



El proyecto permitió aplicar aseguramiento de calidad, medición de software, control de versiones y detección de anomalías mediante inteligencia artificial.



Como oportunidades de mejora se identifican la necesidad de fortalecer las revisiones de código, mejorar la precisión del detector y automatizar las pruebas en GitHub.

