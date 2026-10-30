# Registro de defectos y hallazgos — ALIMENTA-IA

| Identificador | Hallazgo | Severidad / alcance | Estado | Evidencia y acción |
|---|---|---|---|---|
| QA-01 | Cinco falsas alertas del detector en la evaluación sintética | Limitación funcional de IA; no es un defecto de inocuidad demostrado | Abierto como oportunidad de mejora | `evidencias/evaluacion_ia.csv`; ajustar y revalidar modelo |
| QA-02 | Documentación de la versión liberada contiene estados anteriores (PR y release pendientes) | Documental, no crítico del ejecutable | Corrección documental preparada; **pendiente de PR** | Comparación de archivos `docs/` y `README.md` con GitHub |
| QA-03 | No existe registro independiente completo de defectos críticos antes del tag | Brecha de evidencia de auditoría | Pendiente de formalización | Registrar revisión de incidencias abiertas y severidades en GitHub |

**Importante:** 17/17 pruebas aprobadas no permite afirmar por sí solo que existen cero defectos críticos abiertos. Los hallazgos QA-01 a QA-03 no deben presentarse como cerrados sin su evidencia correspondiente.
